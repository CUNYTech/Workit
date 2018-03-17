import sys
import os
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/')

from flask_api import status
from backend.controller import userController
from views import userRoutes
from model import users
from backend import create_app
import json
import unittest


#--------------------------------------- File Description ------------------------------------------------------#
# This file tests various functions from the userController.py file												#
# --------------------------------------------------------------------------------------------------------------#

# tests logic
class CreateNewUser(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_checkUser(self):
		newUser = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}
		code = userController.createUser(json.dumps(newUser))
		user = users.User.query.filter_by(username='bob123').first()
		weight = users.Weight.query.filter_by(weight = 156, weightUnit = "lb", bmi = 20).first()
		joinTable = users.WeightUserJoin.query.filter_by(user_id = user.id, weight_id = weight.id).first()

		self.assertTrue(code == status.HTTP_201_CREATED)
		self.assertTrue(users.User.query.filter_by(username= "bob123").count() == 1)
		self.assertTrue(user.checkPassword("1234567") == True)
		self.assertTrue(user.username == "bob123")

		self.assertTrue(users.Weight.query.filter_by(weight = 156).count() == 1)
		self.assertTrue(joinTable.user_id == user.id)
		self.assertTrue(joinTable.weight_id == weight.id)

#tests the routes
class CreateNewUserRoute(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created through routes
	def test_checkUserRoute(self):
		newUser = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}
		
		response = self.app.post('/user/new',data=json.dumps(newUser), content_type='application/json', follow_redirects=True)
		self.assertTrue(response.status_code == 201)
#tests the routes
class addNewWeight(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created through routes
	def test_addWeight(self):
		newUser = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}
		
		newWeight = {
			"username" : "bob123",
			"weight": 157.0,
			"weightUnit": "lb",
			"bmi": 21.0 
		}

		userController.createUser(json.dumps(newUser))
		userController.addWeight(newWeight)

		checkWeight = users.Weight.query.filter_by(weightUnit = newWeight["weightUnit"], weight= newWeight["weight"], bmi = newWeight["bmi"]).first()

		self.assertTrue(checkWeight != None)

class checkWeightProgress(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created through routes
	def test_checkProgress(self):
		newUser = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}
		
		newWeight = [{
			"username" : "bob123",
			"weight": 157.0,
			"weightUnit": "lb",
			"bmi": 21.0 
		},

		{
			"username" : "bob123",
			"weight": 154.0,
			"weightUnit": "lb",
			"bmi": 21.0 
		},
		{
			"username" : "bob123",
			"weight": 145.0,
			"weightUnit": "lb",
			"bmi": 19.0 
		},

		]

		userController.createUser(json.dumps(newUser))
		for weight in newWeight:
			userController.addWeight(weight)

		checkWeights = userController.getWeightProgress("bob123")

		for idx, weight in enumerate(checkWeights):
			if idx > 0:
				self.assertTrue(newWeight[idx]["weight"] == weight["weight"])
				self.assertTrue(newWeight[idx]["weightUnit"] == weight["weightUnit"])
				self.assertTrue(newWeight[idx]["bmi"] == weight["bmi"])



		

if __name__ == '__main__':
	unittest.main()  
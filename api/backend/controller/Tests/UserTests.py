import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api')

import unittest
from backend.controller import userController
from model import users
from backend import create_app
import unittest

#--------------------------------------- File Description ------------------------------------------------------#
# This file tests various functions from the userController.py file												#
# --------------------------------------------------------------------------------------------------------------#


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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		user = users.User.query.filter_by(username='bob123').first()
		weight = users.Weight.query.filter_by(weight = 156, weightUnit = "lb", bmi = 20).first()
		joinTable = users.WeightUserJoin.query.filter_by(user_id = user.id, weight_id = weight.id).first()

		self.assertTrue(users.User.query.filter_by(username= "bob123").count() == 1)
		self.assertTrue(user.checkPassword("1234567") == True)
		self.assertTrue(user.username == "bob123")

		self.assertTrue(users.Weight.query.filter_by(weight = 156).count() == 1)
		self.assertTrue(joinTable.user_id == user.id)
		self.assertTrue(joinTable.weight_id == weight.id)

	
	# # tests verifyUser function
	# def test_verfiyUserfunction(self):
	# 	self.assertTrue(userController.verifyUser("bob123", "1234567") != False)

	# # tests changeEmail function
	# def test_changeEmail(self):
	# 	userController.changeEmail("bob123", "lazerhawk@email.com")
	# 	user = users.User.query.filter_by(username='bob123').first()
	# 	self.assertTrue(user.email_address == "lazerhawk@email.com")
	# # tests change username function
	# def test_changeUsername(self):
	# 	userController.changeUsername("bob123", "Synthwave6969")
	# 	user = users.User.query.filter_by(username= "Synthwave6969").first()
	# 	self.assertTrue(users.User.query.count() == 1)
	# 	self.assertTrue(user.username == "Synthwave6969")

	# # tests two function one change first name of use and the other the last name
	# def test_changeFirstAndLastName(self):
	# 	userController.changeFirstName("bob123", "Poopyhead")
	# 	userController.changeLastName("bob123", "Von Toilet")
	# 	user = users.User.query.filter_by(username= "bob123").first()
	# 	self.assertTrue(users.User.query.count() == 1)
	# 	self.assertTrue(user.fname == "Poopyhead")
	# 	self.assertTrue(user.lname == "Von Toilet")


	
class TestAddWeights(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()

	def test_addWeights(self):
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		userController.addWeight()

		

if __name__ == '__main__':
	unittest.main()  
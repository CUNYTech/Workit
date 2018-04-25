import sys
import os
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/')

import unittest
from backend.controller import userController, DatesController
from model import users,workouts
from backend import create_app
import unittest
from datetime import datetime
from flask_api import status
import json


class GetList(unittest.TestCase):
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
	def test_getList(self):
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

		newWorkout1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"tag": "weight lifting"
		}

		newWorkout2 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "inlcined chest press",
			"tag": "weight lifting"
		}

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout1)
		DatesController.enterExercise(newWorkout1)
		DatesController.enterExercise(newWorkout2)
		getList = DatesController.getExerciseList(newUser['username'], newWorkout1['date'],newWorkout1['time'])
		
		
		self.assertTrue(getList[0]['name'] == newWorkout1['exerciseName'])
		self.assertTrue(getList[1]['name'] == newWorkout2['exerciseName'])

class GetSet(unittest.TestCase):
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
	def test_getSet(self):
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

		newWorkout1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest press",
			"tag": "weight lifting"
		}

		newWorkout2 = {
			"username" : "bob123", 
			"date": "28-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest press",
			"tag": "weight lifting"
		}

		newWorkout3 = {
			"username" : "bob123", 
			"date": "3-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest press",
			"tag": "weight lifting"
		}

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout1)
		DatesController.scheduleNewWorkout(newWorkout2)
		DatesController.scheduleNewWorkout(newWorkout3)
		DatesController.enterExercise(newWorkout1)
		DatesController.enterExercise(newWorkout2)
		DatesController.enterExercise(newWorkout3)
		getList = DatesController.getSetExercises(newUser['username'])
		
		
		self.assertTrue(len(getList) == 1)
	

class GetSetList(unittest.TestCase):
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
	def test_addSet(self):
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

		newWorkout = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "chest Press"
		}
		set1 = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 1,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}]

		set2 = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}]

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterSetWeight(set1)
		DatesController.enterSetWeight(set2)
		sets = DatesController.getSets(newUser['username'], newWorkout['date'], newWorkout['time'], newWorkout['exerciseName'])

		self.assertTrue(set1[0]['setNum'] == sets[0]['setNumber'])
		self.assertTrue(set2[0]['setNum'] == sets[1]['setNumber'])
		self.assertTrue(set1[0]['reps'] == sets[0]['reps'])
		self.assertTrue(set2[0]['reps'] == sets[1]['reps'])
		


if __name__ == '__main__':
	unittest.main()  
		

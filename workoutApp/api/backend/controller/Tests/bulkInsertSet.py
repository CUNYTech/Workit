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

class EnterSetsExerciseWorkoutRoute(unittest.TestCase):
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
		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 1,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"

		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 3,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}
		]

		
		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterSetWeight(sets)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = "chest").first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.SetExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getSetWeight1 = workouts.SetWeight.query.filter_by(setNumber = 1, reps = 10, weight = 50, weightUnit = 'lb').first()
		getSetWeight2 = workouts.SetWeight.query.filter_by(setNumber = 2, reps = 10, weight = 50, weightUnit = 'lb').first()
		getSetWeight3 = workouts.SetWeight.query.filter_by(setNumber = 3, reps = 10, weight = 50, weightUnit = 'lb').first()
		
		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].setWeight_id == getSetWeight1.id)
		self.assertTrue(setJoin[1].setWeight_id == getSetWeight2.id)
		self.assertTrue(setJoin[2].setWeight_id == getSetWeight3.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == "chest Press")
		self.assertTrue(exerciseJoin is not None)

class EnterCardiosExerciseWorkout(unittest.TestCase):
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
	def test_addCardio(self):
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
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		}
		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length": 5,
			"lengthUnit": "miles"
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length": 6,
			"lengthUnit": "miles"
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length": 7,
			"lengthUnit": "miles"
		}]

		

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterCardio(sets)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = newWorkout["workout"]).first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = newWorkout["exerciseName"]).first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.CardioExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getCardio = workouts.CardioSet.query.filter_by(length = sets[0]["length"], lengthUnit = sets[0]["lengthUnit"]).first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].cardio_id == getCardio.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == newWorkout["exerciseName"])
		self.assertTrue(exerciseJoin is not None)

class EnterCalisthenicExerciseWorkout(unittest.TestCase):
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
	def test_addCalisthenic(self):
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
			"workout":"push up",
			"tag": "calisthenic",
			"exerciseName" : "push up"
		}
		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"push up",
			"tag": "calisthenic",
			"exerciseName" : "push up",
			"setNum": 1,
			"reps": 55
		},{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"push up",
			"tag": "calisthenic",
			"exerciseName" : "push up",
			"setNum": 2,
			"reps": 55
		},{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"push up",
			"tag": "calisthenic",
			"exerciseName" : "push up",
			"setNum": 3,
			"reps": 55
		}]

		

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterCalisthenic(sets)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = newWorkout["workout"]).first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = newWorkout["exerciseName"]).first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.CalisthenicExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getCalisthenic1 = workouts.CalisthenicSet.query.filter_by(setNumber = sets[0]["setNum"], reps = sets[0]["reps"]).first()
		getCalisthenic2 = workouts.CalisthenicSet.query.filter_by(setNumber = sets[1]["setNum"], reps = sets[1]["reps"]).first()
		getCalisthenic3 = workouts.CalisthenicSet.query.filter_by(setNumber = sets[2]["setNum"], reps = sets[2]["reps"]).first()


		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].calisthenic_id == getCalisthenic1.id)
		self.assertTrue(setJoin[1].calisthenic_id == getCalisthenic2.id)
		self.assertTrue(setJoin[2].calisthenic_id == getCalisthenic3.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == newWorkout["exerciseName"])
		self.assertTrue(exerciseJoin is not None)

if __name__ == '__main__':
	unittest.main()  
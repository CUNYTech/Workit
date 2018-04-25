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



class ScheduleWorkout(unittest.TestCase):
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
	def test_scheduleNewWorkout(self):
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
			"workout":"chest"
		} 

		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"tag": "weight lifting",
			"bodyPart" : ["chest","tricipes"],
			"setNum" : 1,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"

		}]

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(sets[0])
		DatesController.enterSetWeight(sets)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = "chest").first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		
		getPart1 = workouts.BodyPart.query.filter_by(name = "chest").first()
		getPart2 = workouts.BodyPart.query.filter_by(name = "tricipes").first()
		getBodyExerciseJoin = workouts.BodyPartExerciseJoin.query.filter_by(exercise_id = getExercise.id, bodyPart_id =getPart1.id).first()
		

		self.assertTrue(getExercise is not None)
		
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == "chest Press")
		self.assertTrue(exerciseJoin is not None)
		self.assertTrue(getPart1.name == "chest")
		self.assertTrue(getPart2.name == "tricipes")
		self.assertTrue(getBodyExerciseJoin is not None)


class newExercise(unittest.TestCase):
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
	def test_newExercise(self):
		exercise = {
			"exerciseName" : "chest press",
			"tag" : "weight lifting",
			"bodyPart" : ["chest"]
		}

		DatesController.newExercise(exercise)
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()

		getPart1 = workouts.BodyPart.query.filter_by(name = "chest").first()
		getBodyExerciseJoin = workouts.BodyPartExerciseJoin.query.filter_by(exercise_id = getExercise.id, bodyPart_id =getPart1.id).first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == "chest press")
		self.assertTrue(getPart1.name == "chest")
		self.assertTrue(getBodyExerciseJoin is not None)


class newExerciseRoutes(unittest.TestCase):
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
	def test_newExerciseRoutes(self):
		exercise = {
			"exerciseName" : "chest press",
			"tag" : "weight lifting",
			"bodyPart" : ["chest"]
		}

		# DatesController.newExercise(exercise)
		

		
		response = self.app.post('/date/new/exercise',data=json.dumps(exercise), content_type='application/json', follow_redirects=True)
		
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()
		getPart1 = workouts.BodyPart.query.filter_by(name = "chest").first()
		getBodyExerciseJoin = workouts.BodyPartExerciseJoin.query.filter_by(exercise_id = getExercise.id, bodyPart_id =getPart1.id).first()
		checkUser = user = users.User.query.filter_by(username = 'bob123').first()
		
		self.assertTrue(response.status_code == 201)
		self.assertTrue(checkUser is None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == "chest press")
		self.assertTrue(getPart1.name == "chest")
		self.assertTrue(getBodyExerciseJoin is not None)

if __name__ == '__main__':
	unittest.main()  

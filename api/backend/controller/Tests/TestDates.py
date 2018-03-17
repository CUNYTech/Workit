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

		userController.createUser(newUser)
		code = DatesController.scheduleNewWorkout(newWorkout)

		user = users.User.query.filter_by(username=newUser["username"]).first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = newWorkout["workout"]).first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime(newWorkout["date"] + " " +  newWorkout["time"], '%d-%m-%Y %I:%M%p')).first()
		checkJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()

		self.assertTrue(code == status.HTTP_201_CREATED)
		self.assertTrue(checkWorkout is not None)
		self.assertTrue(checkDate is not None)
		self.assertTrue(checkJoin.datetime_id == checkDate.id)
		self.assertTrue(checkJoin.workoutName_id == checkWorkout.id)

class ScheduleWorkoutRoute(unittest.TestCase):
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
	def test_scheduleNewWorkoutRoute(self):
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

		userController.createUser(newUser)
		response = self.app.post('/date/new/workout',data=json.dumps(newWorkout), content_type='application/json', follow_redirects=True)
		self.assertTrue(response.status_code == 201)


		


class GetScheduleWorkout(unittest.TestCase):
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

		newWorkouts = [
			{
			"username" : "bob123", 
			"date": "27-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		{
			"username" : "bob123", 
			"date": "18-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		{
			"username" : "bob123", 
			"date": "20-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		{
			"username" : "bob123", 
			"date": "21-3-2018", 
			"time": "2:00pm", 
			"workout":"back"
		},
		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"legs"
		},
		{
			"username" : "bob123", 
			"date": "22-3-2018", 
			"time": "2:00pm", 
			"workout":"back"
		},
		{
			"username" : "bob123", 
			"date": "23-3-2018", 
			"time": "2:00pm", 
			"workout":"arms"
		},

		]

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkouts[0])
		DatesController.scheduleNewWorkout(newWorkouts[1])
		DatesController.scheduleNewWorkout(newWorkouts[2])
		DatesController.scheduleNewWorkout(newWorkouts[3])
		DatesController.scheduleNewWorkout(newWorkouts[4])
		DatesController.scheduleNewWorkout(newWorkouts[5])
		DatesController.scheduleNewWorkout(newWorkouts[6])
		
		dates = []
		workouts = []
		for workout in newWorkouts:
			dates.append(datetime.strptime(workout["date"] + " " +  workout["time"], '%d-%m-%Y %I:%M%p'))
			workouts.append(workout["workout"])
			

		schedule = DatesController.getUserSchedule("bob123", "26-2-2018", '7:00pm')

		self.assertTrue(dates[1] == schedule[0]["date"])
		self.assertTrue(dates[4] == schedule[1]["date"])
		self.assertTrue(dates[2] == schedule[2]["date"])
		self.assertTrue(dates[3] == schedule[3]["date"])
		self.assertTrue(dates[5] == schedule[4]["date"])

class EnterExerciseWorkout(unittest.TestCase):
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
	def test_addExercise(self):
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
			"exerciseName" : "chest Press",
			"tag": "weight lifting"
		}
		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = "chest").first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(exerciseJoin is not None)

class EnterExerciseWorkoutRoute(unittest.TestCase):
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
	def test_addExercise(self):
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

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		response = self.app.post('/date/new/exercise',data=json.dumps(newWorkout), content_type='application/json', follow_redirects=True)
		self.assertTrue(response.status_code == 201)


class EnterSetsExerciseWorkout(unittest.TestCase):
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
		set1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 1,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}

		set2 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterSetWeight(set1)
		DatesController.enterSetWeight(set2)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = "chest").first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = "chest Press").first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.SetExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getSetWeight1 = workouts.SetWeight.query.filter_by(setNumber = 1, reps = 10, weight = 50, weightUnit = 'lb').first()
		getSetWeight2 = workouts.SetWeight.query.filter_by(setNumber = 2, reps = 10, weight = 50, weightUnit = 'lb').first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].setWeight_id == getSetWeight1.id)
		self.assertTrue(setJoin[1].setWeight_id == getSetWeight2.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == "chest Press")
		self.assertTrue(exerciseJoin is not None)
		# self.assertTrue(getSetWeight is not None)
		# self.assertTrue(getSetWeight.setNumber == 1)

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
		set1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 1,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}

		
		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		response = self.app.post('/date/new/exercise/set',data=json.dumps(set1), content_type='application/json', follow_redirects=True)
		self.assertTrue(response.status_code == 201)

class CheckProgress(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()

	def test_progress(self):
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

		workoutsched = [{
			"username" : "bob123", 
			"date": "27-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "chest Press"
		},
		{
			"username" : "bob123", 
			"date": "28-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "chest Press"
		},
		{
			"username" : "bob123", 
			"date": "29-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "chest Press"
		},
		{
			"username" : "bob123", 
			"date": "1-4-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "chest Press"
		}]

		sets = [{
			"username" : "bob123", 
			"date": "27-3-2018", 
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
			"date": "27-3-2018", 
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
			"date": "28-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 55,
			"weightUnit" : "lb"
		},
		{
			"username" : "bob123", 
			"date": "28-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 60,
			"weightUnit" : "lb"
		},
		{
			"username" : "bob123", 
			"date": "29-3-2018", 
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
			"date": "29-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 65,
			"weightUnit" : "lb"
		},
		{
			"username" : "bob123", 
			"date": "1-4-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 40,
			"weightUnit" : "lb"
		},
		{
			"username" : "bob123", 
			"date": "1-4-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"exerciseName" : "chest Press",
			"setNum" : 2,
			"reps" : 10,
			"weight" : 50,
			"weightUnit" : "lb"
		}]

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(workoutsched[0])
		DatesController.scheduleNewWorkout(workoutsched[1])
		DatesController.scheduleNewWorkout(workoutsched[2])
		DatesController.scheduleNewWorkout(workoutsched[3])

		DatesController.enterExercise(workoutsched[0])
		DatesController.enterExercise(workoutsched[1])
		DatesController.enterExercise(workoutsched[2])
		DatesController.enterExercise(workoutsched[3])
		
		DatesController.enterSetWeight(sets[0])
		DatesController.enterSetWeight(sets[1])

		DatesController.enterSetWeight(sets[2])
		DatesController.enterSetWeight(sets[3])

		DatesController.enterSetWeight(sets[4])
		DatesController.enterSetWeight(sets[5])

		DatesController.enterSetWeight(sets[6])
		DatesController.enterSetWeight(sets[7])

		progresses = DatesController.getWeightLiftingProgress("bob123", "chest Press")

		
		self.assertTrue(progresses[0]["set Number"] == 1)
		self.assertTrue(progresses[1]["set Number"] == 2)
		self.assertTrue(progresses[2]["set Number"] == 2)
		self.assertTrue(progresses[3]["set Number"] == 2)
		# self.assertTrue(progresses[0]["set Number"] == 1)

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
		set1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length": 5,
			"lengthUnit": "miles"
		}

		

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterCardio(set1)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = newWorkout["workout"]).first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = newWorkout["exerciseName"]).first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.CardioExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getCardio = workouts.CardioSet.query.filter_by(length = set1["length"], lengthUnit = set1["lengthUnit"]).first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].cardio_id == getCardio.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == newWorkout["exerciseName"])
		self.assertTrue(exerciseJoin is not None)
		# self.assertTrue(getSetWeight is not None)
		# self.assertTrue(getSetWeight.setNumber == 1)

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
		set1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"push up",
			"tag": "calisthenic",
			"exerciseName" : "push up",
			"setNum": 1,
			"reps": 55
		}

		

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterCalisthenic(set1)
		
		user = users.User.query.filter_by(username = 'bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = newWorkout["workout"]).first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkDateJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()
		getExercise = workouts.Exercise.query.filter_by(name = newWorkout["exerciseName"]).first()
		exerciseJoin = workouts.ExerciseDateJoin.query.filter_by(dateJoin_id =  checkDateJoin.id, exercise_id = getExercise.id).first()
		setJoin = workouts.CalisthenicExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
		getCalisthenic = workouts.CalisthenicSet.query.filter_by(setNumber = set1["setNum"], reps = set1["reps"]).first()

		self.assertTrue(getExercise is not None)
		self.assertTrue(setJoin[0].calisthenic_id == getCalisthenic.id)
		self.assertTrue(checkDateJoin is not None)
		self.assertTrue(getExercise is not None)
		self.assertTrue(getExercise.name == newWorkout["exerciseName"])
		self.assertTrue(exerciseJoin is not None)
		# self.assertTrue(getSetWeight is not None)
		# self.assertTrue(getSetWeight.setNumber == 1)

class EnterCardiosExerciseWorkoutRoute(unittest.TestCase):
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
		set1 = {
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length": 5,
			"lengthUnit": "miles"
		}

		

		userController.createUser(newUser)
		DatesController.scheduleNewWorkout(newWorkout)
		DatesController.enterExercise(newWorkout)
		DatesController.enterCardio(set1)
		response = self.app.post('/date/new/exercise/cardio',data=json.dumps(set1), content_type='application/json', follow_redirects=True)
		self.assertTrue(response.status_code == 201)

class GetCardiosExerciseProgress(unittest.TestCase):
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

		newWorkouts = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		},
		{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		},
		{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		},
		{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog"
		},
		]
		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"exerciseName" : "jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length" : 6,
			"lengthUnit" : "mls"
		},
		{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"exerciseName" : "jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length" : 5,
			"lengthUnit" : "mls"
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length" : 6,
			"lengthUnit" : "mls"
		},
		{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length" : 8,
			"lengthUnit" : "mls"
		},
		{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"tag": "cardio",
			"exerciseName" : "jog",
			"length" : 5,
			"lengthUnit" : "mls"
		}]

		userController.createUser(newUser)

		for workouts in newWorkouts:
			DatesController.scheduleNewWorkout(workouts)
		for cardioSet in sets:
			DatesController.enterExercise(cardioSet)
			DatesController.enterCardio(cardioSet)

		progresses = DatesController.getCardioProgress("bob123", "jog")

		for idx,progress in enumerate(progresses):
			self.assertTrue(datetime.strptime(sets[idx]["date"] + " " +  sets[idx]["time"], '%d-%m-%Y %I:%M%p') == progress["date"])
			self.assertTrue(sets[idx]["length"] == progress["length"])
			self.assertTrue(sets[idx]["lengthUnit"] == progress["lengthUnit"])

class GetCalisthenicExerciseProgress(unittest.TestCase):
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

		newWorkouts = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups"
		},
		{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups"
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups"
		},
		{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups"
		},
		{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups"
		},
		]
		sets = [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum": 1,
			"reps" : 35
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 30
		},
		{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 50
		},
		{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 55
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 40
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 40
		},
		{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 60
		},
		{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 69
		},
		{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 60
		},
		{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 60
		}]

		maxSets= [{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum": 1,
			"reps" : 35
		},{
			"username" : "bob123", 
			"date": "1-3-2018", 
			"time": "2:00pm", 
			"workout":"jog",
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 55
		},
		{
			"username" : "bob123", 
			"date": "2-3-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 40
		},{
			"username" : "bob123", 
			"date": "2-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 2,
			"reps" : 69
		},{
			"username" : "bob123", 
			"date": "5-4-2018", 
			"time": "2:00pm", 
			"workout":"push ups",
			"tag": "calisthenic",
			"exerciseName" : "push ups",
			"setNum" : 1,
			"reps" : 60
		},]

		userController.createUser(newUser)

		for workouts in newWorkouts:
			DatesController.scheduleNewWorkout(workouts)
		for calisthenicSet in sets:
			DatesController.enterExercise(calisthenicSet)
			DatesController.enterCalisthenic(calisthenicSet)

		progresses = DatesController.getCalisthenicProgress("bob123", "push ups")

		for idx,progress in enumerate(progresses):
			#self.assertTrue(datetime.strptime(sets[idx]["date"] + " " +  sets[idx]["time"], '%d-%m-%Y %I:%M%p') == progress["date"])
			self.assertTrue(maxSets[idx]["setNum"] == progress["setNumber"])
			self.assertTrue(maxSets[idx]["reps"] == progress["reps"])


if __name__ == '__main__':
	unittest.main()  

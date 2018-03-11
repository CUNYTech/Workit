import sys
import os
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/')

import unittest
from backend.controller import userController, DatesController
from model import users,workouts
from backend import create_app
import unittest
from datetime import datetime


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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		DatesController.scheduleNewWorkout("bob123", "27-2-2018", "2:00pm", "chest")

		user = users.User.query.filter_by(username='bob123').first()
		checkWorkout = workouts.WorkoutName.query.filter_by(name = "chest").first()
		checkDate = workouts.Datetime.query.filter_by(datetime = datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p')).first()
		checkJoin = workouts.DateUserWorkoutJoin.query.filter_by(user_id = user.id).first()

		self.assertTrue(checkWorkout is not None)
		self.assertTrue(checkDate is not None)
		self.assertTrue(checkJoin.datetime_id == checkDate.id)
		self.assertTrue(checkJoin.workoutName_id == checkWorkout.id)

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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		DatesController.scheduleNewWorkout("bob123", "27-2-2017", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "3-2-2017", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "27-2-2018", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "2-3-2018", "2:00pm", "back")
		DatesController.scheduleNewWorkout("bob123", "7-3-2018", "2:00pm", "shoulders")
		DatesController.scheduleNewWorkout("bob123", "8-3-2018", "2:00pm", "legs")
		DatesController.scheduleNewWorkout("bob123", "9-3-2018", "2:00pm", "arms")
		
		dates = []
		workouts = []

		dates.append(datetime.strptime("27-2-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p'))
		dates.append(datetime.strptime("2-3-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p'))
		dates.append(datetime.strptime("7-3-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p'))
		dates.append(datetime.strptime("8-3-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p'))
		dates.append(datetime.strptime("9-3-2018" + " " +  "2:00pm", '%d-%m-%Y %I:%M%p'))

		workouts.append("chest")
		workouts.append("back")
		workouts.append("shoulders")
		workouts.append("legs")
		workouts.append("arms")

		schedule = DatesController.getUserSchedule("bob123", "26-2-2018", '7:00pm')

		self.assertTrue(dates[0] == schedule[0]["date"])
		self.assertTrue(dates[1] == schedule[1]["date"])
		self.assertTrue(dates[2] == schedule[2]["date"])
		self.assertTrue(dates[3] == schedule[3]["date"])
		self.assertTrue(dates[4] == schedule[4]["date"])

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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		DatesController.scheduleNewWorkout("bob123", "27-3-2017", "2:00pm", "chest")
		DatesController.enterExercise("bob123", "27-3-2017", "2:00pm", "chest", "chest Press")
		
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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		DatesController.scheduleNewWorkout("bob123", "27-3-2017", "2:00pm", "chest")
		DatesController.enterExercise("bob123", "27-3-2017", "2:00pm", "chest", "chest Press")
		DatesController.enterSetWeight("bob123", "27-3-2017", "2:00pm", "chest", "chest Press", 1, 10, 50, 'lb')
		DatesController.enterSetWeight("bob123", "27-3-2017", "2:00pm", "chest", "chest Press", 2, 10, 50, 'lb')
		
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
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder", "male", 5.6, "ft", 156.0 ,"lb", 20.0)
		DatesController.scheduleNewWorkout("bob123", "27-3-2018", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "28-3-2018", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "29-3-2018", "2:00pm", "chest")
		DatesController.scheduleNewWorkout("bob123", "1-4-2018", "2:00pm", "chest")

		DatesController.enterExercise("bob123", "27-3-2018", "2:00pm", "chest", "chest Press")
		DatesController.enterExercise("bob123", "28-3-2018", "2:00pm", "chest", "chest Press")
		DatesController.enterExercise("bob123", "29-3-2018", "2:00pm", "chest", "chest Press")
		DatesController.enterExercise("bob123", "1-4-2018", "2:00pm", "chest", "chest Press")
		
		DatesController.enterSetWeight("bob123", "27-3-2018", "2:00pm", "chest", "chest Press", 1, 10, 50, 'lb')
		DatesController.enterSetWeight("bob123", "27-3-2018", "2:00pm", "chest", "chest Press", 2, 10, 50, 'lb')

		DatesController.enterSetWeight("bob123", "28-3-2018", "2:00pm", "chest", "chest Press", 1, 10, 55, 'lb')
		DatesController.enterSetWeight("bob123", "28-3-2018", "2:00pm", "chest", "chest Press", 2, 10, 60, 'lb')

		DatesController.enterSetWeight("bob123", "29-3-2018", "2:00pm", "chest", "chest Press", 1, 10, 50, 'lb')
		DatesController.enterSetWeight("bob123", "29-3-2018", "2:00pm", "chest", "chest Press", 2, 10, 65, 'lb')

		DatesController.enterSetWeight("bob123", "1-4-2018", "2:00pm", "chest", "chest Press", 1, 10, 40, 'lb')
		DatesController.enterSetWeight("bob123", "1-4-2018", "2:00pm", "chest", "chest Press", 2, 10, 50, 'lb')

		progresses = DatesController.getExerciseProgress("bob123", "chest Press")

		
		self.assertTrue(progresses[0]["set Number"] == 1)
		self.assertTrue(progresses[1]["set Number"] == 2)
		self.assertTrue(progresses[2]["set Number"] == 2)
		self.assertTrue(progresses[3]["set Number"] == 2)
		# self.assertTrue(progresses[0]["set Number"] == 1)



if __name__ == '__main__':
	unittest.main()  

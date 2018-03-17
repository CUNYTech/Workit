import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from model.users import User, db
from datetime import datetime
from model.workouts import Datetime, WorkoutName, DateUserWorkoutJoin, Exercise, ExerciseDateJoin, SetWeight, SetExerciseDateJoin, CalisthenicSet, CardioSet,CalisthenicExerciseDateJoin, CardioExerciseDateJoin
from flask import jsonify
from flask_api import status
from sqlalchemy import desc
import json

#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the logic for manipulating the dates table													#
# --------------------------------------------------------------------------------------------------------------#




# create new date time
# date must be in day/month/year format with slashes
# {
# username
# date
# time
# workout
# }
def scheduleNewWorkout(schedule):
	if not isinstance(schedule, dict):
		schedule = json.loads(schedule)


	user = User.query.filter_by(username=schedule["username"]).first()

	if user is None:
		return status.HTTP_404_NOT_FOUND

	dateTime = datetime.strptime(schedule["date"] + " " +  schedule["time"], '%d-%m-%Y %I:%M%p')
	checkDates = Datetime.query.filter_by(datetime = dateTime).first()
	checkWorkout = WorkoutName.query.filter_by(name = schedule["workout"]).first()

	if checkDates is None:
		newDate = Datetime(datetime = dateTime)
		db.session.add(newDate)
		db.session.commit()

	if checkWorkout is None:
		newWorkout = WorkoutName(name =  schedule["workout"])
		db.session.add(newWorkout)
		db.session.commit()

	if checkWorkout is not None and checkDates is not None:
		newScheddule = DateUserWorkoutJoin(user_id = user.id, workoutName_id = checkWorkout.id, datetime_id = checkDates)
		db.session.add(newScheddule)
		db.session.commit()

		return status.HTTP_201_CREATED

	workouts = WorkoutName.query.filter_by(name = schedule["workout"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	newSchedule = DateUserWorkoutJoin(user_id = user.id, workoutName_id = workouts.id, datetime_id = dates.id)
	db.session.add(newSchedule)
	db.session.commit()

	return status.HTTP_201_CREATED

# gets user schedule
# date must be in day/month/year format with slashes
def getUserSchedule(username, curDate, curTime):
	dateTime = datetime.strptime(curDate + " " +  curTime, '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username=username).first()
	dates = Datetime.query.filter(Datetime.datetime > dateTime).all()

	schedules = []

	for date in dates:
		joinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = date.id).first()
		workout = WorkoutName.query.filter_by(id = joinTable.workoutName_id).first()
		
		schedule = {
			"date": date.datetime,
			"workout": workout.name
		}

		schedules.append(schedule)

	return schedules



# enter exercise
# {
# username
# date
# time
# workout
# exerciseName
# tag
# }
def enterExercise(exercise):
	if not isinstance(exercise, dict):
		exercise = json.loads(exercise)

	dateTime = datetime.strptime(exercise["date"] + " " +  exercise["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = exercise["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = exercise["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = exercise["exerciseName"]).first()

	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED


	if checkExercise is not None:
		newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
		db.session.add(newExerciseJoin)
		db.session.commit()

		return status.HTTP_201_CREATED

	newExercise = Exercise(name = exercise["exerciseName"], tag = exercise["tag"])
	db.session.add(newExercise)
	#print(Exercise.query.filter_by(name = exerciseName).first())
	db.session.commit()
	newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id)
	db.session.add(newExerciseJoin)
	db.session.commit()

	#print(ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id).first())
	return status.HTTP_201_CREATED

#only for weight lifting
def enterSetWeight(exerciseSet):
	if not isinstance(exerciseSet, dict):
		exerciseSet = json.loads(exerciseSet)

	dateTime = datetime.strptime(exerciseSet["date"] + " " +  exerciseSet["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = exerciseSet["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = exerciseSet["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = exerciseSet["exerciseName"]).first()
	checkSet = SetWeight.query.filter_by(setNumber = exerciseSet["setNum"], reps = exerciseSet["reps"], weight = exerciseSet["weight"], weightUnit = exerciseSet["weightUnit"]).first()

	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkExercise.tag.lower() != "weight lifting":
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkSet is not None:
		checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
		# print(checkExerciseJoin)
		newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = checkSet.id)
		db.session.add(newSetJoin)
		db.session.commit()

		return status.HTTP_201_CREATED

	newSet = SetWeight(setNumber = exerciseSet["setNum"], reps = exerciseSet["reps"], weight = exerciseSet["weight"], weightUnit = exerciseSet["weightUnit"])
	db.session.add(newSet)
	db.session.commit()
	checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
	newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = newSet.id)	
	db.session.add(newSetJoin)
	db.session.commit()

	return status.HTTP_201_CREATED

# for all cardio exercises
def enterCardio(cardioExercise):
	if not isinstance(cardioExercise, dict):
		cardioExercise = json.loads(cardioExercise)

	dateTime = datetime.strptime(cardioExercise["date"] + " " +  cardioExercise["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = cardioExercise["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = cardioExercise["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = cardioExercise["exerciseName"]).first()
	checkCardio = CardioSet.query.filter_by(length = cardioExercise["length"], lengthUnit = cardioExercise["lengthUnit"]).first()

	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkExercise.tag.lower() != "cardio":
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkCardio is not None:
		checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
		# print(checkExerciseJoin)
		newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, cardio_id = checkCardio.id)
		db.session.add(newSetJoin)
		db.session.commit()

		return status.HTTP_201_CREATED

	newSet = CardioSet(length = cardioExercise["length"], lengthUnit = cardioExercise["lengthUnit"])
	db.session.add(newSet)
	db.session.commit()
	checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
	newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, cardio_id = newSet.id)	
	db.session.add(newSetJoin)
	db.session.commit()

	return status.HTTP_201_CREATED

# for all cardio exercises
def enterCalisthenic(CalisthenicExercise):
	if not isinstance(CalisthenicExercise, dict):
		CalisthenicExercise = json.loads(CalisthenicExercise)

	dateTime = datetime.strptime(CalisthenicExercise["date"] + " " +  CalisthenicExercise["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = CalisthenicExercise["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = CalisthenicExercise["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = CalisthenicExercise["exerciseName"]).first()
	checkCalisthenic = CalisthenicSet.query.filter_by(setNumber = CalisthenicExercise["setNum"], reps = CalisthenicExercise["reps"]).first()

	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkExercise.tag.lower() != "calisthenic":
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkCalisthenic is not None:
		checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
		# print(checkExerciseJoin)
		newSetJoin = CalisthenicExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, calisthenic_id = checkCalisthenic.id)
		db.session.add(newSetJoin)
		db.session.commit()

		return status.HTTP_201_CREATED

	newSet = CalisthenicSet(setNumber = CalisthenicExercise["setNum"], reps = CalisthenicExercise["reps"])
	db.session.add(newSet)
	db.session.commit()
	checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
	newSetJoin = CalisthenicExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, calisthenic_id = newSet.id)	
	db.session.add(newSetJoin)
	db.session.commit()

	return status.HTTP_201_CREATED

#only for weightlifting
def getWeightLiftingProgress(username, exerciseName):
	user = User.query.filter_by(username = username).first()
	getDateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id).all()
	getExercise = Exercise.query.filter_by(name = exerciseName).first()

	exerciseProgress = []

	for date in getDateJoinTable:
		exerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = date.id, exercise_id = getExercise.id).first()

		if exerciseJoin is not None:
			getSetWeightJoin = SetExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
			
			maxSet = {
					"max" : 0,
					"set" : None
			}
			for setWeight in getSetWeightJoin:
				getSet = SetWeight.query.filter_by(id = setWeight.setWeight_id).first()
				if getSet.weight > maxSet["max"]:
					maxSet["max"] = getSet.weight
					maxSet["set"] = getSet
				
			progress = {
				"date": date.datetime.datetime,
				"set Number": maxSet["set"].setNumber,
				"reps" : maxSet["set"].reps,
				"weight" : maxSet["set"].weight,
				"unit" : maxSet["set"].weightUnit,
			}

			#print(progress)
			exerciseProgress.append(progress)

	return exerciseProgress

#only for calisthenic
def getCalisthenicProgress(username, exerciseName):
	user = User.query.filter_by(username = username).first()
	getDateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id).all()
	getExercise = Exercise.query.filter_by(name = exerciseName).first()

	exerciseProgress = []

	for date in getDateJoinTable:
		exerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = date.id, exercise_id = getExercise.id).first()

		if exerciseJoin is not None:
			getCalisthenicJoin = CalisthenicExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
			
			maxSet = {
					"max" : 0,
					"set" : None
			}
			for calisthenic in getCalisthenicJoin:
				getSet = CalisthenicSet.query.filter_by(id = calisthenic.calisthenic_id).first()
				if getSet.reps > maxSet["max"]:
					maxSet["max"] = getSet.reps
					maxSet["set"] = getSet
				
			progress = {
				"date": date.datetime.datetime,
				"reps" : maxSet["set"].reps,
				"setNumber" : maxSet["set"].setNumber 

			}

			#print(progress)
			exerciseProgress.append(progress)
	return exerciseProgress

#only for cardio
def getCardioProgress(username, exerciseName):
	user = User.query.filter_by(username = username).first()
	getDateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id).all()
	getExercise = Exercise.query.filter_by(name = exerciseName).first()

	exerciseProgress = []

	for date in getDateJoinTable:
		exerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = date.id, exercise_id = getExercise.id).first()

		if exerciseJoin is not None:
			getCardioJoin = CardioExerciseDateJoin.query.filter_by(exerciseDateJoin_id = exerciseJoin.id).all()
			
			maxSet = {
					"max" : 0,
					"set" : None
			}
			for cardio in getCardioJoin:
				getSet = CardioSet.query.filter_by(id = cardio.cardio_id).first()
				if getSet.length > maxSet["max"]:
					maxSet["max"] = getSet.length
					maxSet["set"] = getSet
				
			progress = {
				"date": date.datetime.datetime,
				"length" : maxSet["set"].length,
				"lengthUnit" : maxSet["set"].lengthUnit

			}

			#print(progress)
			exerciseProgress.append(progress)

	return exerciseProgress


	



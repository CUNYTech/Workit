import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from model.users import User, db
from datetime import datetime
from model.workouts import Datetime, WorkoutName, DateUserWorkoutJoin, Exercise, ExerciseDateJoin, SetWeight, SetExerciseDateJoin
from flask import jsonify
from sqlalchemy import desc

#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the logic for manipulating the dates table													#
# --------------------------------------------------------------------------------------------------------------#




# create new date time
# date must be in day/month/year format with slashes
def scheduleNewWorkout(username,date, time, workout):
	user = User.query.filter_by(username=username).first()

	if user is None:
		return False

	dateTime = datetime.strptime(date + " " +  time, '%d-%m-%Y %I:%M%p')
	checkDates = Datetime.query.filter_by(datetime = dateTime).first()
	checkWorkout = WorkoutName.query.filter_by(name = workout).first()

	if checkDates is None:
		newDate = Datetime(datetime = dateTime)
		db.session.add(newDate)
		db.session.commit()

	if checkWorkout is None:
		newWorkout = WorkoutName(name =  workout)
		db.session.add(newWorkout)
		db.session.commit()

	if checkWorkout is not None and checkDates is not None:
		newScheddule = DateUserWorkoutJoin(user_id = user.id, workoutName_id = checkWorkout.id, datetime_id = checkDates)
		db.session.add(newScheddule)
		db.session.commit()

		newSchedule = {
			"date": dateTime,
			"workout": workout
		}

		return jsonify(newSchedule)

	workouts = WorkoutName.query.filter_by(name = workout).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	newSchedule = DateUserWorkoutJoin(user_id = user.id, workoutName_id = workouts.id, datetime_id = dates.id)
	db.session.add(newSchedule)
	db.session.commit()

	newSchedule = {
			"date": dateTime,
			"workout": workout
		}

	return newSchedule

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
def enterExercise(username, date, time, workoutName, exerciseName):
	dateTime = datetime.strptime(date + " " +  time, '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = username).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = workoutName).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = exerciseName).first()

	if user is None:
		return {"failed": "Cannot find user"}

	if dateJoinTable is None:
		return {"failed": "Cannot find scheduled workout"}


	if checkExercise is not None:
		newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
		db.session.add(newExerciseJoin)
		db.session.commit()

		return {"date time" : date + " " + time,
				"workout name": workoutName,
				"exercise" : exerciseName
				}
		
	

	newExercise = Exercise(name = exerciseName)
	db.session.add(newExercise)
	#print(Exercise.query.filter_by(name = exerciseName).first())
	db.session.commit()
	newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id)
	db.session.add(newExerciseJoin)
	db.session.commit()

	#print(ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id).first())
	return {"date time" : date + " " + time,
				"workout name": workoutName,
				"exercise" : exerciseName
			}


def enterSetWeight(username, date, time, workoutName, exerciseName, setNum, reps, weight, weightUnit):
	dateTime = datetime.strptime(date + " " +  time, '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = username).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = workoutName).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = exerciseName).first()
	checkSet = SetWeight.query.filter_by(setNumber = setNum, reps = reps, weight = weight, weightUnit = weightUnit).first()

	if user is None:
		return {"failed": "Cannot find user"}

	if dateJoinTable is None:
		return {"failed": "Cannot find scheduled workout"}

	if checkSet is not None:
		checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
		# print(checkExerciseJoin)
		newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = checkSet.id)
		db.session.add(newSetJoin)
		db.session.commit()

		return {"exercise" : exerciseName,
				"setNumber": setNum,
				"reps" : reps,
				"weight" : weight,
				"weightUnit" : weightUnit 
			}

	newSet = SetWeight(setNumber = setNum, reps = reps, weight = weight, weightUnit = weightUnit)
	db.session.add(newSet)
	db.session.commit()
	checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
	newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = newSet.id)	
	db.session.add(newSetJoin)
	db.session.commit()

	return {"exercise" : exerciseName,
				"setNumber": setNum,
				"reps" : reps,
				"weight" : weight,
				"weightUnit" : weightUnit 
			}


def getExerciseProgress(username, exerciseName):
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




	



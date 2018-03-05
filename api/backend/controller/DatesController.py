import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/backend')

from model.users import User, db
from datetime import datetime
from model.workouts import Datetime, WorkoutName, DateUserWorkoutJoin, Exercise, ExerciseSetDateJoin, SetWeight
from flask import jsonify

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



#enter execrise
def enterExecrise(username, date, time, workoutName, execriseName, setNum = None, weight = None, reps = None, weightUnit = None):
	dateTime = datetime.strptime(curDate + " " +  curTime, '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = username).first()
	dates = Datetime.query.filter(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = workoutName).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = date.id, workoutName_id = workout.id).first()
	checkExecrise = Execrise.query.filter_by(name = execriseName).first()
	checkExecriseJoinTable = ExerciseSetDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, execrise_id = checkExecrise).first()

	if user is None:
		return {"failed": "Cannot find user"}

	if dateJoinTable is None:
		return {"failed": "Cannot find scheduled workout"}


	if checkExecrise is None:
		newExecrise = Execrise(name = execriseName)
		db.session.add(newExecrise)
		db.session.commit()
	
	if checkExecriseJoinTable is not None:
			newSet = SetWeight(setNumber = setNum, reps = reps, weight = weight, weightUnit = weightUnit)
			db.session.add(newSet)
			db.session.commit()

			checkExecriseJoinTable.setWeight_id = newSet.id
			db.session.commit()

			return {"update": "added set weight and reps"}

	else:
		if set is None and weight is None and reps is None and weightUnit is None:
			newJoin = ExerciseSetDateJoin(dateJoin_id = dateJoinTable.id, execrise_id = checkExecrise)
			db.session.add(newJoin)
			db.session.commit()

			return {"execrise": execrise}

		else:
			newSet = SetWeight(setNumber = setNum, reps = reps, weight = weight, weightUnit = weightUnit)
			db.session.add(newSet)
			db.session.commit()

			newJoin = ExerciseSetDateJoin(dateJoin_id = dateJoinTable.id, execrise_id = checkExecrise, setWeight_id = newSet.id)
			db.session.add(newJoin)
			db.session.commit()

			return {
				"execirse": execrise,
				"set" : setNum,
				"weight" : weight,
				"weightUnit": weightUnit,
				"reps": reps
				}




	



import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from model.users import User, db
from datetime import datetime
from model.workouts import Datetime, WorkoutName, DateUserWorkoutJoin, Exercise, ExerciseDateJoin, SetWeight, SetExerciseDateJoin, CalisthenicSet, CardioSet,CalisthenicExerciseDateJoin, CardioExerciseDateJoin, BodyPart, BodyPartExerciseJoin,UserDateExerciseJoin
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
# bodyPart
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
		newlistExercise = UserDateExerciseJoin(user_id = user.id, datetime_id = dates.id, exercise_id = checkExercise.id)
		db.session.add(newlistExercise)
		db.session.commit()
		if 'bodyPart' in exercise:
			for part in exercise["bodyPart"]:

				checkPart = BodyPart.query.filter_by(name = part).first()
				if checkPart is not None:
					checkJoin = BodyPartExerciseJoin.query.filter_by(bodyPart_id = checkPart.id, exercise_id = newExercise.id).first()

					if checkJoin is None:
						newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = checkPart.id, exercise_id = newExercise.id)
						db.session.add(newBodyPartExercieJoin)
						db.session.commit()

				else:
					newPart = BodyPart(name = part)
					db.session.add(newPart)
					db.session.commit()

					newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = newPart.id, exercise_id = newExercise.id)
					db.session.add(newBodyPartExercieJoin)
					db.session.commit()

		newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
		db.session.add(newExerciseJoin)
		db.session.commit()

		return status.HTTP_201_CREATED

	newExercise = Exercise(name = exercise["exerciseName"], tag = exercise["tag"])
	db.session.add(newExercise)
	db.session.commit()

	newlistExercise = UserDateExerciseJoin(user_id = user.id, datetime_id = dates.id, exercise_id = newExercise.id)
	db.session.add(newlistExercise)
	db.session.commit()
	if 'bodyPart' in exercise:
		for part in exercise["bodyPart"]:
			checkPart = BodyPart.query.filter_by(name = part).first()
			if checkPart is not None:
				newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = checkPart.id, exercise_id = newExercise.id)
				db.session.add(newBodyPartExercieJoin)
				db.session.commit()

			else:
				newPart = BodyPart(name = part)
				db.session.add(newPart)
				db.session.commit()

				newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = newPart.id, exercise_id = newExercise.id)
				db.session.add(newBodyPartExercieJoin)
				db.session.commit()


	#print(BodyPart.query.filter_by(name = "chest").first())
	newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id)
	db.session.add(newExerciseJoin)
	db.session.commit()

	#print(ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = newExercise.id).first())
	return status.HTTP_201_CREATED

def newExercise(exercise):
	if not isinstance(exercise, dict):
		exercise = json.loads(exercise)

	getExercise = Exercise.query.filter_by(name = exercise["exerciseName"]).first()

	if getExercise is not None:
		for part in exercise["bodyPart"]:
			checkPart = BodyPart.query.filter_by(name = part).first()

			if checkPart is not None:
				checkJoin = BodyPartExerciseJoin.query.filter_by(bodyPart_id = checkPart.id, exercise_id = getExercise.id).first()

				if checkJoin is None:
					newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = checkPart.id, exercise_id = getExercise.id)
					db.session.add(newBodyPartExercieJoin)
					db.session.commit()

			else:
				newPart = BodyPart(name = part)
				db.session.add(newPart)
				db.session.commit()

				newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = newPart.id, exercise_id = newExercise.id)
				db.session.add(newBodyPartExercieJoin)
				db.session.commit()

		return status.HTTP_201_CREATED

	newExercise = Exercise(name = exercise["exerciseName"], tag = exercise["tag"])
	db.session.add(newExercise)
	db.session.commit()

	for part in exercise["bodyPart"]:
		checkPart = BodyPart.query.filter_by(name = part).first()

		if checkPart is not None:
			checkJoin = BodyPartExerciseJoin.query.filter_by(bodyPart_id = checkPart.id, exercise_id = newExercise.id).first()

			if checkJoin is None:
				newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = checkPart.id, exercise_id = newExercise.id)
				db.session.add(newBodyPartExercieJoin)
				db.session.commit()

		else:
			newPart = BodyPart(name = part)
			db.session.add(newPart)
			db.session.commit()

			newBodyPartExercieJoin = BodyPartExerciseJoin(bodyPart_id = newPart.id, exercise_id = newExercise.id)
			db.session.add(newBodyPartExercieJoin)
			db.session.commit()
	# print(Exercise.query.filter_by(name = exercise["exerciseName"]).first())
	return status.HTTP_201_CREATED



#only for weight lifting
def enterSetWeight(exerciseSet):

	# if not isinstance(exerciseSet, dict) or isinstance(exerciseSet, list):
	# 	exerciseSet = json.loads(exerciseSet)
	#print(exerciseSet)

	dateTime = datetime.strptime(exerciseSet[0]["date"] + " " +  exerciseSet[0]["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = exerciseSet[0]["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = exerciseSet[0]["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = exerciseSet[0]["exerciseName"]).first()


	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkExercise.tag.lower() != "weight lifting":
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	newlistExercise = UserDateExerciseJoin(user_id = user.id, datetime_id = dates.id, exercise_id = checkExercise.id)
	db.session.add(newlistExercise)
	db.session.commit()

	for exercise in exerciseSet:
		checkSet = SetWeight.query.filter_by(setNumber = exercise["setNum"], reps = exercise["reps"], weight = exercise["weight"], weightUnit = exercise["weightUnit"]).first()
		if checkSet is not None:
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()

				newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, setWeight_id = checkSet.id)
				db.session.add(newSetJoin)
				db.session.commit()
			else:
				newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = checkSet.id)
				db.session.add(newSetJoin)
				db.session.commit()

		else:

			newSet = SetWeight(setNumber = exercise["setNum"], reps = exercise["reps"], weight = exercise["weight"], weightUnit = exercise["weightUnit"])
			db.session.add(newSet)
			db.session.commit()
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()

				newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, setWeight_id = checkSet.id)
				db.session.add(newSetJoin)
				db.session.commit()
			else:
				newSetJoin = SetExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, setWeight_id = newSet.id)
				db.session.add(newSetJoin)
				db.session.commit()

	return status.HTTP_201_CREATED

# for all cardio exercises
def enterCardio(cardioExercise):
	# if not isinstance(cardioExercise, dict):
	# 	cardioExercise = json.loads(cardioExercise)

	dateTime = datetime.strptime(cardioExercise[0]["date"] + " " +  cardioExercise[0]["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = cardioExercise[0]["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = cardioExercise[0]["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = cardioExercise[0]["exerciseName"]).first()


	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	if checkExercise.tag.lower() != "cardio":
		return status.HTTP_428_PRECONDITION_REQUIRED

	if dateJoinTable is None:
		return status.HTTP_428_PRECONDITION_REQUIRED

	newlistExercise = UserDateExerciseJoin(user_id = user.id, datetime_id = dates.id, exercise_id = checkExercise.id)
	db.session.add(newlistExercise)
	db.session.commit()

	for exercise in cardioExercise:
		checkCardio = CardioSet.query.filter_by(length = exercise["length"], lengthUnit = exercise["lengthUnit"]).first()
		if checkCardio is not None:
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()
				newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, cardio_id = checkCardio.id)
				db.session.add(newSetJoin)
				db.session.commit()

			# print(checkExerciseJoin)
			else:
				newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, cardio_id = checkCardio.id)
				db.session.add(newSetJoin)
				db.session.commit()


		else:
			newSet = CardioSet(length = exercise["length"], lengthUnit = exercise["lengthUnit"])
			db.session.add(newSet)
			db.session.commit()
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()
				newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, cardio_id = newSet.id)
				db.session.add(newSetJoin)
				db.session.commit()

			else:
				newSetJoin = CardioExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, cardio_id = newSet.id)
				db.session.add(newSetJoin)
				db.session.commit()

	return status.HTTP_201_CREATED

# for all cardio exercises
def enterCalisthenic(calisthenicExercise):
	# if not isinstance(calisthenicExercise, dict):
	# 	calisthenicExercise = json.loads(calisthenicExercise)
	#

	dateTime = datetime.strptime(calisthenicExercise[0]["date"] + " " +  calisthenicExercise[0]["time"], '%d-%m-%Y %I:%M%p')

	user = User.query.filter_by(username = calisthenicExercise[0]["username"]).first()
	dates = Datetime.query.filter_by(datetime = dateTime).first()
	workout = WorkoutName.query.filter_by(name = calisthenicExercise[0]["workout"]).first()
	dateJoinTable = DateUserWorkoutJoin.query.filter_by(user_id = user.id, datetime_id = dates.id, workoutName_id = workout.id).first()
	checkExercise = Exercise.query.filter_by(name = calisthenicExercise[0]["exerciseName"]).first()
	checkCalisthenic = CalisthenicSet.query.filter_by(setNumber = calisthenicExercise[0]["setNum"], reps = calisthenicExercise[0]["reps"]).first()

	if user is None:
		return status.HTTP_428_PRECONDITION_REQUIRED


	if dateJoinTable is None:

		return status.HTTP_428_PRECONDITION_REQUIRED

	newlistExercise = UserDateExerciseJoin(user_id = user.id, datetime_id = dates.id, exercise_id = checkExercise.id)
	db.session.add(newlistExercise)
	db.session.commit()

	for exercise in calisthenicExercise:
		checkCalisthenic = CalisthenicSet.query.filter_by(setNumber = exercise["setNum"], reps = exercise["reps"]).first()
		if checkCalisthenic is not None:
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()

				newSetJoin = CalisthenicExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, calisthenic_id = checkCalisthenic.id)
				db.session.add(newSetJoin)
				db.session.commit()
			else:
				newSetJoin = CalisthenicExerciseDateJoin(exerciseDateJoin_id = checkExerciseJoin.id, calisthenic_id = checkCalisthenic.id)
				db.session.add(newSetJoin)
				db.session.commit()

		else:
			newSet = CalisthenicSet(setNumber = exercise["setNum"], reps = exercise["reps"])
			db.session.add(newSet)
			db.session.commit()
			checkExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id).first()
			if checkExerciseJoin is None:
				newExerciseJoin = ExerciseDateJoin(dateJoin_id = dateJoinTable.id, exercise_id = checkExercise.id)
				db.session.add(newExerciseJoin)
				db.session.commit()
				newSetJoin = CalisthenicExerciseDateJoin(exerciseDateJoin_id = newExerciseJoin.id, calisthenic_id = newSet.id)
				db.session.add(newSetJoin)
				db.session.commit()
			else:
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


def getExerciseByBodyPart(bodyPart):
	part = BodyPart.query.filter_by(name = bodyPart).first()

	joinTable = BodyPartExerciseJoin.query.filter_by(bodyPart_id = part.id).all()
	print("Something",joinTable)
	exercises = []
	for exerciseId in joinTable:
		getExercise = Exercise.query.filter_by(id = exerciseId.exercise_id).first()
		exercise = {
			"name" : getExercise.name,
			"type" : getExercise.tag

		}
		exercises.append(exercise)

	print(exercises)

	return exercises


def getExerciseList(user, date, time):

	dateTime = datetime.strptime(date + " " +  time, '%d-%m-%Y %I:%M%p')

	getUser = User.query.filter_by(username= user).first()
	getDatetime = Datetime.query.filter_by(datetime = dateTime).first()

	getUserDateExerciseJoin = UserDateExerciseJoin.query.filter_by(user_id = getUser.id, datetime_id = getDatetime.id).all()


	exerciseList = []
	for exercises in getUserDateExerciseJoin:
		getExercise = Exercise.query.filter_by(id = exercises.exercise_id).first()

		exercise = {
			"name" : getExercise.name,
			"tag" : getExercise.tag

		}

		exerciseList.append(exercise)

	return exerciseList


def getSetExercises(user):
	class ExerciseHolder():
		def __init__(self, name, tag):
			self.name = name
			self.tag = tag

		def __repr__(self):
			return "Item(%s, %s)" % (self.name, self.tag)

		def __eq__(self, other):
			if isinstance(other, ExerciseHolder):
				return ((self.name == other.name) and (self.tag == other.tag))
			else:
				return False

		def __ne__(self, other):
			return (not self.__eq__(other))

		def __hash__(self):
			return hash(self.__repr__())


	getUser = User.query.filter_by(username= user).first()
	getUserDateExerciseJoin = UserDateExerciseJoin.query.filter_by(user_id = getUser.id).all()

	exerciseSet = set()

	for exerciseid in getUserDateExerciseJoin:
		getExercise = Exercise.query.filter_by(id = exerciseid.exercise_id).first()

		exerciseSet.add(ExerciseHolder(getExercise.name,getExercise.tag))


	exerciseList = []

	for holder in exerciseSet:

		exercise = {
			"name" : holder.name,
			"tag" : holder.tag

		}

		exerciseList.append(exercise)


	return exerciseList



def getSets(user, date, time, exercise):
	dateTime = datetime.strptime(date + " " +  time, '%d-%m-%Y %I:%M%p')

	getUser = User.query.filter_by(username= user).first()
	getDatetime = Datetime.query.filter_by(datetime = dateTime).first()
	getExercise = Exercise.query.filter_by(name= exercise).first()
	getUserDateJoin = DateUserWorkoutJoin.query.filter_by(user_id = getUser.id, datetime_id = getDatetime.id).first()
	getExerciseJoin = ExerciseDateJoin.query.filter_by(dateJoin_id = getUserDateJoin.id , exercise_id = getExercise.id).first()

	sets = []

	if getExercise.tag.lower() == "weight lifting":
		getSetJoin = SetExerciseDateJoin.query.filter_by(exerciseDateJoin_id = getExerciseJoin.id).all()


		for liftingset in  getSetJoin:
			getSet = SetWeight.query.filter_by(id = liftingset.setWeight_id).first()

			newSet = {
				"setNumber" : getSet.setNumber,
				"reps" : getSet.reps,
				"weight" : getSet.weight,
				"weightUnit" : getSet.weightUnit
			}

			sets.append(newSet)




	if getExercise.tag.lower() == "cardio":
		getSetJoin = CardioExerciseDateJoin.query.filter_by(exerciseDateJoin_id = getExerciseJoin.id).all()


		for liftingset in  getSetJoin:
			getSet = CardioSet.query.filter_by(id = liftingset.cardio_id).first()

			newSet = {
				"length" : getSet.length,
				"lengthUnit" : getSet.lengthUnit

			}

			sets.append(newSet)



	if getExercise.tag.lower() == "calisthenics":
		getSetJoin = CalisthenicExerciseDateJoin.query.filter_by(exerciseDateJoin_id = getExerciseJoin.id).all()



		for liftingset in  getSetJoin:
			getSet = CalisthenicSet.query.filter_by(id = liftingset.calisthenic_id).first()

			newSet = {
				"setNumber" : getSet.setNumber,
				"reps" : getSet.reps

			}

			sets.append(newSet)


	return sets

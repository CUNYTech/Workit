import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from controller import userController, DatesController
from model import users
from flask import Blueprint,redirect,jsonify,Response,request,abort


dates = Blueprint('date', __name__)


@dates.route("/new/workout", methods = ["POST"])
def scheduleNewWorkout():
	return '',DatesController.scheduleNewWorkout(request.get_json())

@dates.route("/schedule/workout/<username>/<curDate>/<curTime>", methods = ["GET"])
def getSchedule(username, curDate, curTime):
	return jsonify(DatesController.getUserSchedule(username, curDate, curTime))

@dates.route("/new/exercise", methods = ["POST"])
def enterExercise():
	checkKey = request.get_json()
	if 'username' in checkKey:		
		return '', DatesController.enterExercise(request.get_json())
		
	else:
		return '', DatesController.newExercise(request.get_json())

@dates.route("/new/exercise/set", methods = ["POST"])
def enterWeight():
	return '', DatesController.enterSetWeight(request.get_json())

@dates.route("/new/exercise/cardio", methods = ["POST"])
def enterCardio():
	return '', DatesController.enterCardio(request.get_json())

@dates.route("/new/exercise/calisthenic", methods = ["POST"])
def enterCalisthenic():
	return '', DatesController.enterCalisthenic(request.get_json())

@dates.route("/get/exercises/<bodyPart>", methods= ["GET"])
def getExercie(bodyPart):
	return jsonify(DatesController.getExerciseByBodyPart(bodyPart))

@dates.route("/progress/<username>/<tag>/<exercise>", methods = ["GET"])
def getProgess(username, exercise, tag):
	if tag.lower() == "weight_lifting":
		return jsonify(DatesController.getWeightLiftingProgress(username, exercise))
	elif tag.lower() == "cardio":
		return jsonify(DatesController.getCardioProgress(username, exercise))
	elif tag.lower() == "calisthenic":
		return jsonify(DatesController.getCalisthenicProgress(username, exercise))
	else:
		abort(404)

@dates.route("/get/exercise/list/<user>/<date>/<time>")
def getList(user,date,time):
	return jsonify(DatesController.getExerciseList(user,date,time))


@dates.route("/get/sets/<user>/<date>/<time>/<exercise>")
def getSet(user,date,time,exercise):
	return jsonify(DatesController.getSets(user, date, time, exercise))

@dates.route("/get/unique/exercise/<user>")
def getUniqueExercise(user):
	return jsonify(DatesController.getSetExercises(user))
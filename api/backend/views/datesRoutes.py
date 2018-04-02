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
	return '', DatesController.enterExercise(request.get_json())

@dates.route("/new/exercise/set", methods = ["POST"])
def enterWeight():
	return '', DatesController.enterSetWeight(request.get_json())

@dates.route("/new/exercise/cardio", methods = ["POST"])
def enterCardio():
	return '', DatesController.enterCardio(request.get_json())

@dates.route("/new/exercise/calisthenic", methods = ["POST"])
def enterCalisthenic():
	return '', DatesController.enterCalisthenic(request.get_json())


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
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from controller import userController, DatesController
from model import users
from flask import Blueprint,redirect,jsonify,session,g

dates = Blueprint('date', __name__)


@dates.route("/new/workout/<username>/<date>/<time>/<workout>")
def scheduleNewWorkout(username,date,time,workout):
	return jsonify(DatesController.scheduleNewWorkout(username, date, time, workout))

@dates.route("/schedule/workout/<username>/<curDate>/<curTime>")
def getSchedule(username, curDate, curTime):
	return jsonify(DatesController.getUserSchedule(username, curDate, curTime))

@dates.route("/exercise/new/<username>/<date>/<time>/<workout>/<exerciseName>")
def enterExercise(username, date, time, workout, exerciseName):
	return jsonify(DatesController.enterExercise(username, date, time, workout, exerciseName))

@dates.route("/exercise/new/weight/<username>/<date>/<time>/<workout>/<exerciseName>/<setNum>/<reps>/<weight>/<weightUnit>")
def enterWeight(username, date, time, workout, exerciseName, setNum, reps, weight, weightUnit):
	return jsonify(DatesController.enterSetWeight(username, date, time, workout, exerciseName, setNum, reps, weight, weightUnit))
import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/backend')

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
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from controller import userController
from model import users
from flask import Blueprint,request,Response
from flask_api import status

user = Blueprint('user', __name__)


#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the routes for user interaction															#
# --------------------------------------------------------------------------------------------------------------#



# NOTE must implement some sort of encryption for route url 
# logging in
@user.route("/login/<username>/<password>", methods = ['GET'])
def userLogin(username, password):
	#some logic to decrypt password
	return "",userController.verifyUser(username, password)


# NOTE must implement some sort of encryption for route url 
# creating new user
@user.route("/new", methods = ['POST'])
def createNewUser():
	return "",userController.createUser(request.get_json()) 

# change any of the user fields
# email, username, password(not implemented yet), first name = fname, last name = lname
@user.route("/update/<username>/<field>/<newChange>")
def updateUser(username, field, newChange):
	
	if field == "username":
		return jsonify(userController.changeUsername(username, newChange))

	elif field == "email":
		return jsonify(userController.changechangeEmail(username, newChange))

	elif field == "password":
		pass

	elif field == "fname":
		return jsonify(userController.changeFirstName(username, newChange))

	elif field == "lname":
		return jsonify(userController.changeLastName(username, newChange))

	
	return jsonify({"error": "invalid field or username"})
	
	
@user.route("/info/<username>", methods = ["GET"])
def getInfo(username):
	return jsonify(getUserInfo(username))

@user.route("/new/weight/", methods = ["POST"])
def addNewWeight():
	return "", addWeight(request.get_json)

@user.route("/progress/weight/<username>", methods= ["GET"])
def getUserWeightProgress(username):
	return jsonify(getWeightProgress(username))

@user.route("/get/username/weight/progress")
def getProgress(username):
	pass

@user.route("/get/username/weight/current")
def currentWeight(username):
	pass

# deletes user
# NOTE must implement some sort of encryption for route url 
@user.route("/delete/<username>/")
# @userController.auth.login_required
def deleteUser(username):
	
	userController.deleteUser(username)

	return "deleted"


	

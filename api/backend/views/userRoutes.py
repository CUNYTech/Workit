import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from controller import userController
from model import users
from flask import Blueprint,redirect,jsonify,session,g

user = Blueprint('user', __name__)


#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the routes for user interaction															#
# --------------------------------------------------------------------------------------------------------------#



# NOTE must implement some sort of encryption for route url 
# logging in
@user.route("/login/<username>/<password>")
def userLogin(username, password):
	#some logic to decrypt password
	return jsonify(userController.verifyUser(username,password))
		


# NOTE must implement some sort of encryption for route url 
# creating new user
@user.route("/new/<username>/<email>/<password>/<fname>/<lname>/<gender>/<height>/<heightUnit>/<weight>/<weightUnits>/<bmi>")
def createNewUser(username, email, password, fname, lname, gender, height, heightUnit, weight, weightUnits, bmi):
	
	if userController.createUser(username, email, password, fname, lname, gender, height, heightUnit, weight, weightUnits, bmi):
		return redirect("user/login/" + username + "/" + password)

	return jsonify({"create user": False})
# change any of the user fields
# email, username, password(not implemented yet), first name = fname, last name = lname
@user.route("/update/username/<field>/<newChange>")
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
	
	


@user.route("/new/weight/<username>/<weight>/<weightUnits>/<bmi>")
def addNewWeight(username, weight, weightUnits, bmi):
	return addWeight(username, weight, weightUnits, bmi)

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


	

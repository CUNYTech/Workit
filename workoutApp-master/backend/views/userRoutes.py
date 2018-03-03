import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/backend')

from controller import userController
from model import users
from flask_httpauth import HTTPBasicAuth
from flask import Blueprint,redirect,jsonify


auth = HTTPBasicAuth()
user = Blueprint('user', __name__)

#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the routes for user interaction															#
# --------------------------------------------------------------------------------------------------------------#

# NOTE must implement some sort of encryption for route url 
# logging in
@user.route("/login/<username>/<password>")
@auth.checkPassword
def userLogin(username, password):
	#some logic to decrypt password

	if userController.verifyUser(username, password) == False:
		return False

	return True


# NOTE must implement some sort of encryption for route url 
# creating new user
user.route("/new/<username>/<email>/<password>/<fname>/<lname>")
def createNewUser(username, email, password, fname, lname):
	createUser(username, email, password, fname, lname)

	return redirect("/login/" + username + "/" + password)

# change any of the user fields
# email, username, password(not implemented yet), first name = fname, last name = lname
@user.route("/update/<field>/<newChange>")
@auth.login_required
def updateUser(field, newChange):
	if field == "username":
		userController.changeUsername(auth.username(), newChange)

	elif field == "email":
		userController.changeUsername(auth.username(), newChange)

	elif field == "password":
		pass
	elif field == "fname":
		userController.changeUsername(auth.username(), newChange)

	elif field == "lname":
		userController.changeUsername(auth.username(), newChange)

	else:
		return jsonify({"error": "invalid feild"})

# deletes user
# NOTE must implement some sort of encryption for route url 
@user.route("/delete/<username>/<password>")
@auth.login_required
def deleteUser(username, password):
	user = userController.verifyUser(username, password)

	if user != False:
		userController.deleteUser(username)
		return "user is deleted"

	return jsonify({"error": "password or username is invalid"})

user.route("/logout")
@auth.login_required
def logout():
	pass
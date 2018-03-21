import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from datetime import datetime
from model.users import User, Weight, WeightUserJoin, db
from passlib.hash import sha256_crypt
from flask_api import status
from sqlalchemy import desc
import json



#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the ability to create new users, update user info, delete user, and retreive user info		#
# This file also contains the ability for the user to login and logout											#
# NOTE:  need to implement change password function																#
# --------------------------------------------------------------------------------------------------------------#



# add weight update entry
def addWeight(weight):
	if not isinstance(weight, dict):
		weight = json.loads(weight)

	user = User.query.filter_by(username = weight["username"]).first()
	checkWeight = Weight.query.filter_by(weight = weight["weight"], bmi = weight["bmi"], weightUnit = weight["weightUnit"]).first()

	if user == None:
		return status.HTTP_404_NOT_FOUND

	if checkWeight == None:
		newWeight = Weight(weight = weight["weight"], bmi = weight["bmi"], weightUnit = weight["weightUnit"])
		db.session.add(newWeight)
		db.session.commit()

	newWeightId = Weight.query.filter_by(weight = weight["weight"], bmi = weight["bmi"], weightUnit = weight["weightUnit"]).first()
	
	joinTables = WeightUserJoin(user_id = user.id, weight_id = newWeightId.id)


	db.session.add(joinTables)
	db.session.commit()

	return status.HTTP_201_CREATED

# adds new user to the database
def createUser(user):
	if not isinstance(user, dict):
		user = json.loads(user)

	checkEmail = User.query.filter_by(email_address = user["email"])
	checkUsername = User.query.filter_by(username = user["username"])

	if checkEmail.count() > 0:
		return status.HTTP_409_CONFLICT

	if checkUsername.count() > 0:
		return status.HTTP_409_CONFLICT

	newUser = User(username = user["username"], password = sha256_crypt.hash(user["password"]), email_address = user["email"], 
		fname = user["fname"], lname = user["lname"], gender = user["gender"], height = user["height"], heightUnit = user["heightUnit"])
	db.session.add(newUser)
	db.session.commit()

	if addWeight(user) == status.HTTP_201_CREATED:
		return status.HTTP_201_CREATED

	return status.HTTP_417_EXPECTATION_FAILED

# check if user exist and password mathes
def verifyUser(username, password):
	
	checkUser = User.query.filter_by(username = username).first()

	if checkUser is None:
		return HTTP_400_BAD_REQUEST
	
	if checkUser.checkPassword(password):
		return status.HTTP_202_ACCEPTED

	return HTTP_400_BAD_REQUEST

# changes user's email address
def changeEmail(username, email):
	updatedUser = User.query.filter_by(username = username).update(dict(email_address = email))
	if updatedUser == None:
		raise Exception('username does not exist')
	db.session.commit()

	return {"email": email,
			"Changed": "email"
	}

# changes username
def changeUsername(username, newUsername):
	updatedUser = User.query.filter_by(username = username).update(dict(username = newUsername))
	if updatedUser == None:
		raise Exception('username does not exist')
	db.session.commit()

	return {"username": username,
			"Changed": "username"
	}

# changes first name of user
def changeFirstName(username, fName):
	updatedUser = User.query.filter_by(username = username).update(dict(fname = fName))
	if updatedUser == None:
		raise Exception('username does not exist')
	db.session.commit()

	return {"First Name": fName,
			"Changed": "First Name"
	}

# changes first name of user
def changeLastName(username, lName):
	updatedUser = User.query.filter_by(username = username).update(dict(lname = lName))
	if updatedUser == None:
		raise Exception('username does not exist')
	db.session.commit()

	return {"Last Name": lName,
			"Changed": "Last Name"
	}

def getUserInfo(username):
	user = username.query.filter_by(username = username).first()
	weightJoin = WeightUserJoin.quey.filter_by(user_id = user.id).order_by(desc(WeightUserJoin.date)).first()
	weight = Weight.query.filter_by(id = weight_id).first()

	info = {"username": user.username,
			"email" : user.email_address,
			"First Name" : user.fname,
			"Last Name" : user.lname,
			"gender" : user.gender,
			"height" : user.height,
			"heightUnit" : user.heightUnit,
			"weight" : weight.weight,
			"weightUnit" : weight.weightUnit,
			"bmi" : weight.bmi
	}

	return info

def getWeightProgress(username):
	user = User.query.filter_by(username = username).first()
	weightJoin = WeightUserJoin.query.filter_by(user_id = user.id).all()

	progresses = []

	for join in weightJoin:
		getWeight = Weight.query.filter_by(id = join.weight_id).first()

		weight = {
				"date" : join.date,
				"weight" : getWeight.weight,
				"weightUnit" : getWeight.weightUnit,
				"bmi" : getWeight.bmi
		} 

		progresses.append(weight)
	print(progresses)
	return progresses

# under contruction
# delete user
def deleteUser(username):
	user = User.query.filter_by(username = username).first()
	db.session.delete(user)
	db.session.commit()

# # get most recent weight
# def getRecentWeight(username):
# 	query = db.session.query(User, Weight, WeightUserJoin).join(User).join(Weight)
# 	weight Weight.query.order_by('datetime').first()

# 	weightDict = {
# 		'weight': weight.weight
# 		'unit' : weight.weightUnit
# 		'bmi': weight.bmi
# 	}

# 	return jsonify(weightDict)


# # get all weights in chronological order
# def getAllWeights(username):
# 	query = db.session.
# 	WeightUserJoin.query.order_by('datetime')
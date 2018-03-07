import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from datetime import datetime
from model.users import User, Weight, WeightUserJoin, db
from passlib.hash import sha256_crypt
from flask import jsonify




#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the ability to create new users, update user info, delete user, and retreive user info		#
# This file also contains the ability for the user to login and logout											#
# NOTE:  need to implement change password function																#
# --------------------------------------------------------------------------------------------------------------#



# add weight update entry
def addWeight(username, weight, bmi, weightUnit, date=None):
	user = User.query.filter_by(username = username).first()
	checkWeight = Weight.query.filter_by(weight = weight, bmi = bmi, weightUnit = weightUnit).first()

	if user == None:
		return False

	if checkWeight == None:
		newWeight = Weight(weight = weight, bmi = bmi, weightUnit = weightUnit)
		db.session.add(newWeight)
		db.session.commit()

	newWeightId = Weight.query.filter_by(weight = weight, bmi = bmi, weightUnit = weightUnit).first()
	if date == None:
		joinTables = WeightUserJoin(user_id = user.id, weight_id = newWeightId.id)

	else:
		joinTables = WeightUserJoin(user_id = user.id, weight_id = newWeightId.id, date = datetime.datetime.strptime(date, '%d%m%Y').date())

	db.session.add(joinTables)
	db.session.commit()

	return True

# adds new user to the database
def createUser(username, email, password, fname, lname, gender, height, heightUnit, weight, weightUnit, bmi):
	checkEmail = User.query.filter_by(email_address = email)
	checkUsername = User.query.filter_by(username = username)

	if checkEmail.count() > 0:
		return {"email": "exists"}

	if checkUsername.count() > 0:
		return {"username": "exists"}

	newUser = User(username = username, password = sha256_crypt.hash(password), email_address = email, fname = fname, lname = lname, gender = gender, height = height, heightUnit = heightUnit)
	db.session.add(newUser)
	db.session.commit()

	if addWeight(username, weight, bmi, weightUnit):
		True

	return False

# check if user exist and password mathes
def verifyUser(username, password):
	user = User.query.filter_by(username = username).first()

	if user is None:
		return {"verified": False}
	
	return {"verified" : user.checkPassword(password)}

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

# returns email address of user
def getEmail(username):
	user  = User.query.filter_by(username = username)
	return {"email": user.email_address}

# returns email address of user
def getLastName(username):
	user  = User.query.filter_by(username = username)
	return {"Last Name": user.lname}

# returns email address of user
def getFirstName(username):
	user  = User.query.filter_by(username = username)
	return {"First Name": user.fname}

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
import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/backend')

from model.users import User, db
from passlib.hash import sha256_crypt

#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the ability to create new users, update user info, delete user, and retreive user info		#
# This file also contains the ability for the user to login and logout											#
# NOTE:  need to implement change password function																#
# --------------------------------------------------------------------------------------------------------------#


# adds new user to the database
def createUser(username, email, password, fname, lname):
	checkEmail = User.query.filter_by(email_address = email)
	checkUsername = User.query.filter_by(username = username)

	if checkEmail.count() > 0:
		raise Exception("email exists")

	if checkUsername.count() > 0:
		raise Exception("user name exists")

	newUser = User(username = username, password = sha256_crypt.hash(password), email_address = email, fname = fname, lname = lname)
	db.session.add(newUser)
	db.session.commit()

# check if user exist and password mathes
def verifyUser(username, password):
	user = User.query.filter_by(username = username).first()

	if user is None:
		return False

	if not user.checkPassword(password):
		return False

	return user

# changes user's email address
def changeEmail(username, email):
	updatedUser = User.query.filter_by(username = username).update(dict(email_address = email))
	db.session.commit()

# changes username
def changeUsername(username, newUsername):
	updatedUser = User.query.filter_by(username = username).update(dict(username = newUsername))
	db.session.commit()

# changes first name of user
def changeFirstName(username, fName):
	updatedUser = User.query.filter_by(username = username).update(dict(fname = fName))
	db.session.commit()

# changes first name of user
def changeLastName(username, lName):
	updatedUser = User.query.filter_by(username = username).update(dict(lname = lName))
	db.session.commit()

# delete user
def deleteUser(username):
	user = User.query.filter_by(username = username).first()
	db.session.delete(user)
	db.session.commit()
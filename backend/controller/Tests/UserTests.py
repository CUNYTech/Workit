import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/')

import unittest
from backend.controller import userController
from model import users
from backend import create_app
import unittest

#--------------------------------------- File Description ------------------------------------------------------#
# This file tests various functions from the userController.py file												#
# --------------------------------------------------------------------------------------------------------------#


class CreateNewUser(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		userController.createUser("bob123","bob123@email.com","1234567","Bob","TheBuilder")

	def tearDown(self):
		users.User.query.filter_by(username='bob123').delete()
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_checkUser(self):
		self.assertTrue(users.User.query.count() == 1)
		user = users.User.query.filter_by(username='bob123').first()
		self.assertTrue(user.checkPassword("1234567") == True)
		self.assertTrue(user.username == "bob123")
	
	# tests verifyUser function
	def test_verfiyUserfunction(self):
		self.assertTrue(userController.verifyUser("bob123", "1234567") != False)

	# tests changeEmail function
	def test_changeEmail(self):
		userController.changeEmail("bob123", "lazerhawk@email.com")
		user = users.User.query.filter_by(username='bob123').first()
		self.assertTrue(user.email_address == "lazerhawk@email.com")
	# tests change username function
	def test_changeUsername(self):
		userController.changeUsername("bob123", "Synthwave6969")
		user = users.User.query.filter_by(username= "Synthwave6969").first()
		self.assertTrue(users.User.query.count() == 1)
		self.assertTrue(user.username == "Synthwave6969")

	# tests two function one change first name of use and the other the last name
	def test_changeFirstAndLastName(self):
		userController.changeFirstName("bob123", "Poopyhead")
		userController.changeLastName("bob123", "Von Toilet")
		user = users.User.query.filter_by(username= "bob123").first()
		self.assertTrue(users.User.query.count() == 1)
		self.assertTrue(user.fname == "Poopyhead")
		self.assertTrue(user.lname == "Von Toilet")


	
	
		

if __name__ == '__main__':
	unittest.main()  
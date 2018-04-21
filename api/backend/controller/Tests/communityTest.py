import sys
import os
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/')

from flask_api import status
from backend.controller import userController
from backend.controller import communityController
from views import userRoutes
from model import users, community
from backend import create_app
import json
import unittest


class AddFriend(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_addFriend(self):
		newUser1 = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser2 = {
			"username": "megan123",
			"email": "megan123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		friendRequest = {
			'username' : newUser1['username'],
			'friend' : newUser2['username']
		}

		userController.createUser(newUser1)
		userController.createUser(newUser2)



		communityController.addFriend(friendRequest)

		
		bob = users.User.query.filter_by(username = friendRequest['username']).first()
		megan = users.User.query.filter_by(username = friendRequest['friend']).first()
		checkIfFriends = community.Friend.query.filter_by(friend_id1 = bob.id, friend_id2 = megan.id).first()

		self.assertTrue(checkIfFriends is not None)


class checkIfFriends(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_checkIfFriends(self):
		newUser1 = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser2 = {
			"username": "megan123",
			"email": "megan123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		friendRequest1 = {
			'username' : newUser1['username'],
			'friend' : newUser2['username']
		}

		friendRequest2 = {
			'username' :newUser2['username'],
			'friend' : newUser1['username']
		}

		userController.createUser(newUser1)
		userController.createUser(newUser2)



		communityController.addFriend(friendRequest1)
		communityController.addFriend(friendRequest2)
		
		friendshipChecker = communityController.checkIfFriends(friendRequest2)

		self.assertTrue(friendshipChecker['friends'] == True)


class checkFriendRequests(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_checkIfFriendsRequests(self):
		newUser1 = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser2 = {
			"username": "megan123",
			"email": "megan123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser3 = {
			"username": "paul123",
			"email": "paul23@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser4 = {
			"username": "jack123",
			"email": "jack123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser5 = {
			"username": "fukcer123",
			"email": "fucker123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		friendRequest1 = {
			'username' : newUser1['username'],
			'friend' : newUser2['username']
		}

		friendRequest2 = {
			'username' :newUser2['username'],
			'friend' : newUser1['username']
		}

		friendRequest6 = {
			'username' :newUser1['username'],
			'friend' : newUser5['username']
		}

		friendRequest3 = {
			'username' : newUser3['username'],
			'friend' : newUser1['username']
		}

		friendRequest4 = {
			'username' :newUser4['username'],
			'friend' : newUser1['username']
		}

		friendRequest5 = {
			'username' :newUser5['username'],
			'friend' : newUser1['username']
		}



		userController.createUser(newUser1)
		userController.createUser(newUser2)
		userController.createUser(newUser3)
		userController.createUser(newUser4)
		userController.createUser(newUser5)



		communityController.addFriend(friendRequest1)
		communityController.addFriend(friendRequest2)
		communityController.addFriend(friendRequest3)
		communityController.addFriend(friendRequest4)
		communityController.addFriend(friendRequest5)
		communityController.addFriend(friendRequest6)

		checkFriendRequests = communityController.checkFriendRequests({'username' : newUser1['username']})
		

		self.assertTrue(checkFriendRequests[0]['username'] == friendRequest3['username'])
		self.assertTrue(checkFriendRequests[1]['username'] == friendRequest4['username'])
		# self.assertTrue(checkFriendRequests[2]['username'] == friendRequest5['username'])

class checkFriend(unittest.TestCase):
	def setUp(self):
		app = create_app()
		app.config['TESTING'] = True
		self.app = app.test_client()
		app.app_context().push()
		users.db.create_all()
		

	def tearDown(self):
		users.db.session.remove()
		users.db.drop_all()
	
	# checks if user was created
	def test_checkIfFriends(self):
		newUser1 = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser2 = {
			"username": "megan123",
			"email": "megan123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser3 = {
			"username": "paul123",
			"email": "paul23@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser4 = {
			"username": "jack123",
			"email": "jack123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		newUser5 = {
			"username": "fukcer123",
			"email": "fucker123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

		friendRequest1 = {
			'username' : newUser1['username'],
			'friend' : newUser2['username']
		}

		friendRequest2 = {
			'username' :newUser2['username'],
			'friend' : newUser1['username']
		}

		friendRequest6 = {
			'username' :newUser1['username'],
			'friend' : newUser5['username']
		}

		friendRequest3 = {
			'username' : newUser3['username'],
			'friend' : newUser1['username']
		}

		friendRequest4 = {
			'username' :newUser4['username'],
			'friend' : newUser1['username']
		}

		friendRequest5 = {
			'username' :newUser5['username'],
			'friend' : newUser1['username']
		}



		userController.createUser(newUser1)
		userController.createUser(newUser2)
		userController.createUser(newUser3)
		userController.createUser(newUser4)
		userController.createUser(newUser5)



		communityController.addFriend(friendRequest1)
		communityController.addFriend(friendRequest2)
		communityController.addFriend(friendRequest3)
		communityController.addFriend(friendRequest4)
		communityController.addFriend(friendRequest5)
		communityController.addFriend(friendRequest6)

		checkFriendRequests = communityController.getFriendsList(newUser1['username'])
		

		self.assertTrue(checkFriendRequests[0]['username'] == friendRequest3['username'])
		self.assertTrue(checkFriendRequests[1]['username'] == friendRequest4['username'])
			


if __name__ == '__main__':
	unittest.main()  

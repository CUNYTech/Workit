# add friends/acceptfriends
# check if are friends
# check if blocked
# add blocked



import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from model.users import User, db
from model.community import Friend, Block
import json


# {
	
# 	username
# 	friend
# }

def addFriend(friend):
	if not isinstance(friend, dict):
		friend = json.loads(friend)

	getUserId = User.query.filter_by(username=friend['username']).first()
	getFriendId = User.query.filter_by(username=friend['friend']).first()
	checkUserFriend = Friend.query.filter_by(friend_id1 = getUserId.id, friend_id2 = getFriendId.id).first()

	if checkUserFriend is None:
		newUserFriend = Friend(friend_id1 = getUserId.id, friend_id2 = getFriendId.id)
		db.session.add(newUserFriend)
		db.session.commit()
		# print(newUserFriend)

		return {'new_friend': 'succesful add'}

	return {'new_friend': 'failed'}


# {
# 	username
# 	friend
# }
def checkIfFriends(friend):
	if not isinstance(friend, dict):
		friend = json.loads(friend)

	getUserId = User.query.filter_by(username=friend['username']).first()
	getFriendId = User.query.filter_by(username=friend['friend']).first()
	checkIfUser = Friend.query.filter_by(friend_id1 = getUserId.id, friend_id2 = getFriendId.id).first()
	checkIfFriend = Friend.query.filter_by(friend_id1 =getFriendId.id, friend_id2 = getUserId.id).first()

	if checkIfUser is not None and checkIfFriend is not None:
		return {"friends": True}

	return {"friends": False}


def checkFriendRequests(user):
	if not isinstance(user, dict):
		user = json.loads(user)

	getUserId = User.query.filter_by(username=user['username']).first()
	checkIfFriend = Friend.query.filter(Friend.friend_id2 == getUserId.id).all()

	requests = []
	for request in checkIfFriend:
		check = Friend.query.filter_by(friend_id1 = getUserId.id, friend_id2 = request.id).first()
		if check is None:
			user = User.query.filter_by(id = request.friend_id1).first()

			username = {
				"username" : user.username
			}

			requests .append(username)
	
	return requests


def getFriendsList(username):
	getUserId = User.query.filter_by(username = username).first()

	checkIfFriend = Friend.query.filter(Friend.friend_id2 == getUserId.id).all()

	friends = []
	for friend in checkIfFriend:
		check = Friend.query.filter_by(friend_id1 = getUserId.id, friend_id2 = friend.id).first()
		if check is None:
			user = User.query.filter_by(id = friend.friend_id1).first()

			username = {
				"username" : user.username
			}

			friends.append(username)
	
	return friends

def blockUser(block):
	if not isinstance(block, dict):
		block = json.loads(block)

	getUserId = User.query.filter_by(username = block['username']).first()
	getblockeeId = User.query.filter_by(username = block['block']).first()

	blockUser = Block(block_id1 = block['username'], block_id2 = block['block'])
	db.session.add(blockUser)
	db.session.commit()

	return {'block': 'succesful add'}



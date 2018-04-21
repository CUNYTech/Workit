# create friends list
# create block list
# create gym table and join table


import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from .users import db, User



class Friend(db.Model):
	__tablename__ = 'friends'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	friend_id1 = db.Column(db.Integer, db.ForeignKey('users.id'))
	friend_id2 = db.Column(db.Integer, db.ForeignKey('users.id'))
	friends1 = db.relationship('User', foreign_keys=[friend_id1])
	friends2 = db.relationship('User', foreign_keys=[friend_id2])
	

	def __repr__(self):
		return "<Friend(self.friend_id1 = '%s', self.friend_id2 = '%s')>" %(self.friend_id1, self.friend_id2)


class Block(db.Model):
	__tablename__ = 'blocks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	block_id1 = db.Column(db.Integer, db.ForeignKey('users.id'))
	block_id2 = db.Column(db.Integer, db.ForeignKey('users.id'))
	blocks1 = db.relationship('User', foreign_keys=[block_id1])
	blocks2 = db.relationship('User',  foreign_keys=[block_id2])

	def __repr__(self):
		return "<Friend(self.block_id1 = '%s', self.block_id2 = '%s')>" %(self.block_id1, self.block_id2)
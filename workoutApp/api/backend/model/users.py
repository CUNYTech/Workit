from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from sqlalchemy.orm import validates
from datetime import datetime


#--------------------------------------- File Description ------------------------------------------------------#
# This file contains the tables for users, date time, and workoutnames They are all stored in workoutApp		#
# --------------------------------------------------------------------------------------------------------------#



db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	fname = db.Column(db.String(80), nullable=False)
	lname = db.Column(db.String(80), nullable=False)
	email_address = db.Column(db.String(80), unique=True, nullable=False)
	gender = db.Column(db.String(10), nullable=False)
	height = db.Column(db.Float, nullable=False)
	heightUnit = db.Column(db.String(10), nullable=False)
	dateUserWorkoutJoins = db.relationship('DateUserWorkoutJoin', backref='user', lazy=True)
	userweightJoins = db.relationship('WeightUserJoin', backref='user', lazy=True)
	userDateExerciseJoin = db.relationship('UserDateExerciseJoin', backref='user', lazy=True)

	
	def __repr__(self):
	    return "<Users(username ='%s', password='%s', email_address='%s' , fname='%s' , lname='%s')>" % (self.username, self.password, self.email_address, self.fname, self.lname)

	@validates('password')
	def validatePassword(self, key, password):
		assert len(password) >= 6
		return password

	@validates('email_address')
	def check_email(self, key, email):
		assert '@' in email
		return email

	def checkPassword(self, password):
		return sha256_crypt.verify(password, self.password)


class Weight(db.Model):
	__tablename__ = "weights"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	weight = db.Column(db.Float, nullable=False)
	weightUnit = db.Column(db.String(80), nullable=False)
	bmi = db.Column(db.Float, nullable=False)
	userweightJoins = db.relationship('WeightUserJoin', backref='weight', lazy=True)

	def __repr__(self):
		return "<weights(weight = '%s', weightUnit = '%s', bmi = '%s')>" %(self.weight, self.weightUnit, self.bmi)

class WeightUserJoin(db.Model):
	__tablename__ = "weightUserJoins"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	date = db.Column(db.Date, default=datetime.now().date())
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	weight_id = db.Column(db.Integer, db.ForeignKey('weights.id'))

	def __repr__(self):
		return "<weightUserjoins(user_id = '%s', weight_id = '%s' date = '%s')>" %(self.user_id, self.weight_id, self.date)


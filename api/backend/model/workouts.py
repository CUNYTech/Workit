import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from .users import db, User


class Datetime(db.Model):
	__tablename__ = 'datetimes'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	datetime = db.Column(db.DateTime, nullable=False, unique=True)
	dateUserWorkoutJoins = db.relationship('DateUserWorkoutJoin', backref='datetime', lazy=True)
	userDateExerciseJoin = db.relationship('UserDateExerciseJoin', backref='datetime', lazy=True)
	

	def __repr__(self):
		return "<datetimes(datetime= '%s')>" %(self.datetime)

class WorkoutName(db.Model):
	__tablename__ = 'workoutNames'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	dateUserWorkoutJoins = db.relationship('DateUserWorkoutJoin', backref='workoutName', lazy=True)


	def __repr__(self):
		return "<workoutNames(name='%s')>" %(self.name) 

class Exercise(db.Model):
	__tablename__ = 'exercises'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(200), unique=True, nullable=False)
	tag = db.Column(db.String(200), nullable=False)
	exerciesSetDateJoin = db.relationship('ExerciseDateJoin', backref='exercise', lazy=True)
	bodyPartExerciseJoin = db.relationship('BodyPartExerciseJoin', backref='exercise', lazy=True)
	userDateExerciseJoin = db.relationship('UserDateExerciseJoin', backref='exercise', lazy=True)
	

	def __repr__(self):
		return "<exercise(name = '%s')>" %(self.name)

class BodyPart(db.Model):
	__tablename__ = 'bodyParts'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(200), unique=True, nullable=False)
	bodyPartExerciseJoin = db.relationship('BodyPartExerciseJoin', backref='bodyPart', lazy=True)

	def __repr__(self):
		return "<bodyParts(name = '%s')>" %(self.name)

class CalisthenicSet(db.Model):
	__tablename__ = 'calisthenicSets'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	setNumber = db.Column(db.Integer)
	reps = db.Column(db.Integer)
	calisthenicExerciseDateJoin = db.relationship('CalisthenicExerciseDateJoin', backref='calisthenicSet', lazy=True)

	def __repr__(self):
		return "<calisthenicSets(setNumber = '%s', reps = '%s')>" %(self.setNumber, self.reps)

class CardioSet(db.Model):
	__tablename__ = 'cardioSets'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	length = db.Column(db.Float)
	lengthUnit = db.Column(db.String(200))
	cardioExerciseDateJoin = db.relationship('CardioExerciseDateJoin', backref='cardioSet', lazy=True)

	def __repr__(self):
		return "<cardioSets(setNumber = '%s', reps = '%s')>" %(self.length, self.lengthUnit)

class BodyPartExerciseJoin(db.Model):
	__tablename__ = 'bodyPartExerciseJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
	bodyPart_id = db.Column(db.Integer, db.ForeignKey('bodyParts.id'))


	def __repr__(self):
		return "<bodyPartExerciseJoins(exercise_id = '%s', bodyPart_id = '%s')>" %(self.exercise_id, self.bodyPart_id)

class SetWeight(db.Model):
	__tablename__ = 'setWeights'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	setNumber = db.Column(db.Integer)
	reps = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	weightUnit = db.Column(db.String(80))
	setExerciesDateJoin = db.relationship('SetExerciseDateJoin', backref='setWeight', lazy=True)

	def __repr__(self):
		return "<setWeight(setNumber = '%s', reps = '%s', weight = '%s', weightUnit = '%s')>" %(self.setNumber, self.reps, self.weight, self.weightUnit)


class DateUserWorkoutJoin(db.Model):
	__tablename__	= 'dateUserWorkoutJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	workoutName_id = db.Column(db.Integer, db.ForeignKey('workoutNames.id'))
	datetime_id = db.Column(db.Integer, db.ForeignKey('datetimes.id'))
	exerciesDateJoin = db.relationship('ExerciseDateJoin', backref='dateUserWorkoutJoin', lazy=True)

	def __repr__(self):
		return "<dateUserWorkoutJoins(user_id='%s', workoutName_id='%s', datetime_id='%s')>" %(self.user_id, self.workoutName_id, self.datetime_id)

class ExerciseDateJoin(db.Model):
	__tablename__ = 'exerciseDateJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dateJoin_id = db.Column(db.Integer, db.ForeignKey('dateUserWorkoutJoins.id'))
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
	setExerciesDateJoin = db.relationship('SetExerciseDateJoin', backref='exerciseDateJoin', lazy=True)
	calisthenicExerciseDateJoin = db.relationship('CalisthenicExerciseDateJoin', backref='exerciseDateJoin', lazy=True)
	cardioExerciseDateJoin = db.relationship('CardioExerciseDateJoin', backref='exerciseDateJoin', lazy=True)
	
	def __repr__(self):
		return "<exerciseDateJoins(dateJoin_id = '%s', exercise_id = '%s')>" %(self.dateJoin_id, self.exercise_id)

class SetExerciseDateJoin(db.Model):
	__tablename__ = 'setExerciseDateJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	exerciseDateJoin_id = db.Column(db.Integer, db.ForeignKey('exerciseDateJoins.id')) 
	setWeight_id =  db.Column(db.Integer, db.ForeignKey('setWeights.id'))

	def __repr__(self):
		return "<setExerciseDateJoins(exerciseDateJoin_id = '%s', setWeight_id = '%s')>" %(self.exerciseDateJoin_id, self.setWeight_id)

class CalisthenicExerciseDateJoin(db.Model):
	__tablename__ = 'calisthenicExerciseDateJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	exerciseDateJoin_id = db.Column(db.Integer, db.ForeignKey('exerciseDateJoins.id')) 
	calisthenic_id =  db.Column(db.Integer, db.ForeignKey('calisthenicSets.id'))

	def __repr__(self):
		return "<calisthenicExerciseDateJoins(exerciseDateJoin_id = '%s', calisthenic_id = '%s')>" %(self.exerciseDateJoin_id, self.calisthenic_id)

class CardioExerciseDateJoin(db.Model):
	__tablename__ = 'cardioExerciseDateJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	exerciseDateJoin_id = db.Column(db.Integer, db.ForeignKey('exerciseDateJoins.id')) 
	cardio_id =  db.Column(db.Integer, db.ForeignKey('cardioSets.id'))

	def __repr__(self):
		return "<cardioExerciseDateJoins(exerciseDateJoin_id = '%s', cardio_id = '%s')>" %(self.exerciseDateJoin_id, self.cardio_id)

class UserDateExerciseJoin(db.Model):
	__tablename__ = 'userDateExerciseJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	datetime_id = db.Column(db.Integer, db.ForeignKey('datetimes.id'))
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

	def __repr__(self):
		return "<userDateExerciseJoins(user_id = '%s' , datetime_id = '%s' , exercise_id = '%s')>" %(self.user_id, self.datetime_id, self.exercise_id)

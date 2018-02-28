import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/backend/api/backend/model')

from .users import db, User


class Datetime(db.Model):
	__tablename__ = 'datetimes'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	datetime = db.Column(db.DateTime, nullable=False, unique=True)
	dateUserWorkoutJoins = db.relationship('DateUserWorkoutJoin', backref='datetime', lazy=True)
	

	def __repr__(self):
		return "<datetimes(datetime= '%s')>" %(self.datetime)

class WorkoutName(db.Model):
	__tablename__ = 'workoutNames'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	dateUserWorkoutJoins = db.relationship('DateUserWorkoutJoin', backref='workoutName', lazy=True)


	def __repr__(self):
		return "<workoutNames(name='%s')>" %(self.name) 

class exercise(db.Model):
	__tablename__ = 'exercises'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(200), unique=True, nullable=False)
	exerciesSetDateJoin = db.relationship('ExercisSetDateJoin', backref='exercise', lazy=True)

	def __repr__(self):
		return "<exercise(name = '%s')>" %(self.name)


class SetWeight(db.Model):
	__tablename__ = 'setWeights'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	setNumber = db.Column(db.Integer)
	reps = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	weightUnit = db.Column(db.String(80))
	exerciesSetDateJoin = db.relationship('ExercisSetDateJoin', backref='exercise', lazy=True)

	def __repr__(self):
		return "<exercise(setNumber = '%s', reps = '%s', weight = '%s', weightUnit = '%s')>" %(self.setNumber, self.reps, self.weight, self.weightUnit)


class DateUserWorkoutJoin(db.Model):
	__tablename__	= 'dateUserWorkoutJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	workoutName_id = db.Column(db.Integer, db.ForeignKey('workoutNames.id'))
	datetime_id = db.Column(db.Integer, db.ForeignKey('datetimes.id'))
	exerciesSetDateJoin = db.relationship('ExercisSetDateJoin', backref='exercise', lazy=True)

	def __repr__(self):
		return "<dateUserWorkoutJoins(user_id='%s', workoutName_id='%s', datetime_id='%s')>" %(self.user_id, self.workoutName_id, self.datetime_id)

class ExerciseSetDateJoin(db.Model):
	__tablename__ = 'exerciseSetDateJoins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dateJoin_id = db.Column(db.Integer, db.ForeignKey('dateUserWorkoutJoins.id'))
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
	setWeight_id =  db.Column(db.Integer, db.ForeignKey('setWeights.id'))

	def __repr__(self):
		return "<exerciseSetDateJoins(dateJoin_id = '%s', exercise_id = '%s', setWeight_id = '%s')>" %(self.dateJoin_id, self.exercise_id, self.setWeight_id)
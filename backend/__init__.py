import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/backend')

from flask import Flask 
from model.users import db
# from views.views import main

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pen226@localhost/workoutApp'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = 'dude'
	db.init_app(app)
	return app

app = create_app()
db.create_all(app=app)	

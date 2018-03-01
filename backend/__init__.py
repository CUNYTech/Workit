import sys
sys.path.insert(0, '/home/brandon/workoutApp/backend')

from flask import Flask 
from model.users import db
# from views.views import main

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testdb:testtest@teststuff.c6nwp1reyyfx.us-east-2.rds.amazonaws.com/dbstuff'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = 'testtest'
	db.init_app(app)
	return app

app = create_app()
db.create_all(app=app)	

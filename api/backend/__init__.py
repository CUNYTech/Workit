import sys
sys.path.insert(0, '/home/russ/Desktop/workoutApp/api/backend')

import os
from flask import Flask 
from model.users import db
from views.userRoutes import user
from views.datesRoutes import dates
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pen226@localhost/workoutApp'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = 'dude'
	app.secret_key = os.urandom(24)
	app.register_blueprint(user, url_prefix='/user')
	app.register_blueprint(dates, url_prefix='/date')
	db.init_app(app)
	return app

app = create_app()
db.create_all(app=app)	
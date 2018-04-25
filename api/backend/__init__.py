import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import os
from flask import Flask
from model.users import db
from views.userRoutes import user
from views.datesRoutes import dates


def create_app():
	app = Flask(__name__)
	#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + sys.argv[1]+ ':' + sys.argv[2] + '@localhost/workoutApp'
	#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://russ:russ1992@cunycodes.cfoznmrgp7ri.us-east-2.rds.amazonaws.com:3306/workoutApp'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Dajcochran:root@localhost/workoutApp'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = 'dude'
	app.secret_key = os.urandom(24)
	app.register_blueprint(user, url_prefix='/user')
	app.register_blueprint(dates, url_prefix='/date')
	db.init_app(app)
	return app

app = create_app()
db.create_all(app=app)

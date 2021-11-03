from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy

my_obj = Flask(__name__)

my_obj.config.from_mapping(
	SECRET_KEY = 'you-will-know',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

db = SQLAlchemy(my_obj)

from app import routes, models

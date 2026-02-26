import os

from flask import Flask
# install: 
# python -m pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# install: 
# python -m pip install flask-migrate
from flask_migrate import Migrate

app = Flask(__name__)

# database
# Get absolute path of this directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'site.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from learnFlaskApp import routes, models
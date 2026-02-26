from flask import Flask
# install: 
# python -m pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database
db = SQLAlchemy(app)

from learnFlaskApp import routes, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
if 'DATABASE_URL' in os.environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config('SQLALCHEMY_TRACK_MODIFICATIONS') = False
db = SQLAlchemy(app)

from app import views
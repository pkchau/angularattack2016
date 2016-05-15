
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask('Trippin')
app.config.from_object('config')
login_manager=LoginManager()
login_manager.init_app(app)

db=SQLAlchemy(app)

from .api import api

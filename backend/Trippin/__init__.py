
from flask import Flask

app=Flask('Trippin')
app.config.from_object('config')

from .api import api

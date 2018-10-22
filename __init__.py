from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, sys


import settings as settings

app = Flask(__name__)
app.config.from_object(settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import view
import model
import forms

if __name__ == '__main__':
    app.run()
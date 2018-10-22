from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import settings as settings

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    db = SQLAlchemy(app)
    return app

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rami import app
from flask_script import Manager, Server
from application import create_app
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)


manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '127.0.0.1'),
    port=int(os.getenv('PORT', 5000)))
)

if __name__ == "__main__":
    manager.run()
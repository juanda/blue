from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .home import home
from .dash import dash
from .admin import admin

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')
app.register_blueprint(home)
app.register_blueprint(dash)
app.register_blueprint(admin)

db = SQLAlchemy(app)

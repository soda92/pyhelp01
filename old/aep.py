import flask_login
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

login_manager = flask_login.LoginManager()
users = Flask(__name__)
users.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(users)

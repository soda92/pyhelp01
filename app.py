from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
database = SQLAlchemy(app)


class Employee(database.Model):
    employee_id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(50), nullable=False)
    last_name = database.Column(database.String(80), nullable=False)
    email_address = database.Column(database.String(100), nullable=False, unique=True)
    phone_number = database.Column(database.Integer, unique=True)
    first_aid_trained = database.Column(database.Boolean, nullable=False, default=False)
    password = database.Column(database.String(128), nullable=False)


@app.route('/')
def hello():
    return 'Hello, World!'

from sqlalchemy import select
@app.route("/testdata", methods=["GET"])
def test_data():
    employees = database.session.execute(select(Employee)).first()
    for i in employees:
        print(i)
        print(i.first_name)
    return "test"

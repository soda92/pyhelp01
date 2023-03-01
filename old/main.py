from sqlalchemy import (
    create_engine,
    ForeignKey,
    Column,
    String,
    Integer,
    VARCHAR,
    CHAR,
)  # THIS IS NOT READING
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from aep import db, login_manager, users
from flask_login import UserMixin
from itsdangerous import TimedSerializer as Serializer
from flask import current_app

Session = sessionmaker(bind=create_engine)
base = declarative_base()


@login_manager.user_loader
def load_user(user_id):
    return WORKER.query.get(int(user_id))


from dataclasses import dataclass

@dataclass
class WORKER(db.Model, UserMixin):
    tablename = "WORKER"
    Worker_ID = db.Column(db.Integer, primary_key=True)
    Worker_FirstName = db.Column(db.VARCHAR(100), unique=False, nullable=False)
    Worker_LastName = db.Column(db.VARCHAR(100), unique=False, nullable=False)
    Worker_Email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    Worker_Password = db.Column(db.VARCHAR(25), nullable=False)
    Department_ID = db.Column(db.Integer, nullable=False)
    Role_ID = db.Column(db.Integer, nullable=False)
    # Department_ID = relationship("Department", order_by=Worker_ID, back_populates="Department")
    # Role_ID = relationship("Role", order_by=Worker_ID, back_populates="Role")

    def repr(self):
        return f"({self.Worker_FirstName} {self.Worker_FirstName} {self.Worker_LastName} "\
            f"{self.Worker_Email} {self.Worker_Password})"


from flask import render_template, redirect, url_for, flash


# @users.route("/login", methods=["GET", "POST"])
# def login():
#     if current_worker:
#         return redirect(url_for("main.mainpage"))

#     form = LoginForm()

#     if form.validate_on_submit():
#         user = WORKER.query.filter_by(Worker_Email=form.Worker_Email.data).first()
#         if user and (user.Worker_Password == form.Worker_Password.data):
#             return redirect(url_for("main.mainpage"))
#         else:
#             flash("Login Unsuccessful. Please check email and password", "danger")
#     return render_template("login.html", title="Login", form=form)

"""using UserMixin to add flask login attributes to the model """
from flask_login import UserMixin
from . import db


# python code to create a user model with columns for an id, email, password, name
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
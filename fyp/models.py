from enum import unique
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    result = db.Column(db.Float(32))
    status = db.Column(db.String(1000))
    reason = db.Column(db.String(1000))

class Car(UserMixin, db.Model):
    __tablename__ = "car"
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    aid = db.Column(db.String(1000), unique=True)
    status = db.Column(db.String(1000))
    email = db.Column(db.String(100))
    A = db.Column(db.Integer)
    B = db.Column(db.Integer)
    C = db.Column(db.Integer)
    D = db.Column(db.Integer)
    E = db.Column(db.Integer)
    F = db.Column(db.Integer)
    G = db.Column(db.Integer)
    H = db.Column(db.Integer)
    I = db.Column(db.Integer)
    J = db.Column(db.Integer)

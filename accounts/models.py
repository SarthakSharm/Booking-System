from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

with app.app_context():
    db.create_all()
from flask_login import UserMixin
from website import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    ticket = db.relationship("Ticket", backref="ticket_user")

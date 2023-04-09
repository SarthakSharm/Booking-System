from website import db, app


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    place = db.Column(db.String, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    screens = db.Column(db.Integer, nullable=False)
    show = db.relationship("Show", cascade="all, delete", backref="show_venue")

from website import db, app


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    show = db.Column(db.Integer, db.ForeignKey("show.id"), nullable=False)

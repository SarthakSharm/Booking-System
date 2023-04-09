from website import db, app


class Show(db.Model):
    __tablename__ = "show"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    tag = db.Column(db.String, nullable=True)
    ticket_price = db.Column(db.Integer, nullable=False)
    updated_price = db.Column(db.Integer, nullable=True)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venue.id", ondelete="CASCADE"), nullable=False
    )
    date = db.Column(db.Date, nullable=False)
    ticket = db.relationship(
        "Ticket",
        cascade="all, delete",
        backref="ticket_show",
    )

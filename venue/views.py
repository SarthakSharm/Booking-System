from flask import Blueprint, request, render_template
from .models import Venue
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from website import db

venue = Blueprint("venue", __name__, url_prefix="/venue")


@venue.route("/", methods=["GET"])
def venues():
    if request.method == "GET":
        venues = Venue.query.all()
        return render_template("venue.html", venues=venues, user=current_user)


@venue.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        venue = Venue(
            name=request.form.get("name"),
            place=request.form.get("place"),
            capacity=request.form.get("capacity"),
            screens=request.form.get("screens"),
        )
        db.session.add(venue)
        db.session.commit()
        return render_template("venue.html", user=current_user)
    if request.method == "GET":
        return render_template("createVenue.html", user=current_user)

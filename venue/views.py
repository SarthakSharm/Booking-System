from flask import Blueprint, request, render_template, redirect, url_for
from .models import Venue
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from website import db


venue = Blueprint("venue", __name__, url_prefix="/venue")


@venue.route("/", methods=["GET"])
@login_required
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
        return redirect(url_for("venue.venues"))
    if request.method == "GET":
        return render_template("createVenue.html", user=current_user)

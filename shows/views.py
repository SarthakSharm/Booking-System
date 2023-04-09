from flask import Blueprint, flash, request, render_template, redirect, url_for
from .models import Show
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
from website import db
from venue.models import Venue

show = Blueprint("show", __name__, url_prefix="/show")


@show.route("/", methods=["GET"])
def shows():
    if request.method == "GET":
        shows = Show.query.all()
        return render_template("show.html", shows=shows, user=current_user)


@show.route("/delete/<int:show_id>", methods=["GET"])
def delete(show_id):
    if current_user.is_admin == False:
        flash("You are not admin", category="error")
        return redirect(url_for("show.shows"))

    if request.method == "GET":
        show = Show.query.filter_by(id=show_id).first()
        if show == None:
            flash("Empty", category="error")
            return redirect(url_for("show.shows"))
        db.session.delete(show)
        db.session.commit()
        return redirect(url_for("show.shows"))


@show.route("/create", methods=["GET", "POST"])
def create():
    if current_user.is_admin == False:
        flash("You are not admin", category="error")
        return redirect(url_for("show.shows"))

    if request.method == "POST":
        show = Show(
            name=request.form.get("name"),
            tag=request.form.get("tag"),
            rating=request.form.get("rating"),
            ticket_price=request.form.get("price"),
            venue_id=request.form.get("venue"),
            date=datetime.strptime(request.form.get("date"), "%Y-%m-%d"),
        )
        db.session.add(show)
        db.session.commit()
        return redirect(url_for("show.shows"))

    if request.method == "GET":
        venues = Venue.query.all()
        return render_template("createShow.html", user=current_user, venues=venues)

from flask import Blueprint, request, render_template, redirect, url_for, flash
from .models import Ticket
from shows.models import Show
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
from website import db
from venue.models import Venue

ticket = Blueprint("ticket", __name__, url_prefix="/ticket")


@ticket.route("myTickets", methods=["GET"])
@login_required
def myTickets():
    if request.method == "GET":
        tickets = Ticket.query.filter_by(user=current_user.id)
        return render_template("myTickets.html", tickets=tickets, user=current_user)


@ticket.route("show/<int:show_id>", methods=["GET"])
@login_required
def confirmTicket(show_id):
    if request.method == "GET":
        show = Show.query.filter_by(id=show_id).first()
        print(show)
        return render_template("bookTicket.html", show=show, user=current_user)


@ticket.route("/book", methods=["POST"])
@login_required
def bookTicket():
    venue = Venue.query.filter(Venue.show.any(id=request.form.get("show_id"))).first()
    tickets = Ticket.query.filter_by(show=request.form.get("show_id")).count()
    if tickets > venue.capacity:
        flash("Venue Full. Sorry!", category="error")
        return redirect(url_for("website.home"))

    ticket = Ticket(
        show=request.form.get("show_id"),
        date=datetime.strptime(request.form.get("date"), "%Y-%m-%d"),
        user=current_user.id,
    )
    db.session.add(ticket)
    db.session.commit()
    return redirect(url_for("ticket.myTickets"))

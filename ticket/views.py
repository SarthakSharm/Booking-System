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
        # tickets = Ticket.query.filter(Venue.show.any())
        return render_template("myTickets.html", tickets=tickets, user=current_user)


@ticket.route("show/<int:show_id>", methods=["GET"])
@login_required
def confirmTicket(show_id):
    if request.method == "GET":
        show = Show.query.filter_by(id=show_id).first()

        return render_template("bookTicket.html", show=show, user=current_user)


@ticket.route("/book", methods=["POST"])
@login_required
def bookTicket():
    show = Show.query.filter_by(id=request.form.get("show_id")).first()
    venue = Venue.query.filter(Venue.show.any(id=request.form.get("show_id"))).first()
    tickets = Ticket.query.filter_by(show=request.form.get("show_id"))
    count = 0
    for ticket in tickets:
        count = count + ticket.quantity
    print("Tickets count: ", tickets)
    print("Venue capacity: ", venue.capacity)
    print(count > venue.capacity)
    if count > venue.capacity:
        flash("Venue Full. Sorry!", category="error")
        return redirect(url_for("views.home"))

    ticket = Ticket(
        show=request.form.get("show_id"),
        date=datetime.strptime(request.form.get("date"), "%Y-%m-%d"),
        user=current_user.id,
        quantity=request.form.get("quantity"),
    )
    db.session.add(ticket)
    db.session.commit()

    percentage = count / venue.capacity
    print(percentage)
    print(count)
    price = show.ticket_price + show.ticket_price * percentage
    print("Updated price: ", price)
    show.ticket_price = price
    db.session.commit()

    return redirect(url_for("ticket.myTickets"))

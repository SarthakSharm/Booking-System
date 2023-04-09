from flask import Blueprint, request, render_template, redirect, url_for
from shows.models import Show
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint("views", __name__, url_prefix="/")


@views.route("/")
def home():
    shows = Show.query.all()
    return render_template("home.html", shows=shows, user=current_user)

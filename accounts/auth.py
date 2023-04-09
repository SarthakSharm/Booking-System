from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from datetime import datetime
from website import db

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        # Handle GET request
        return render_template("signup.html", user=current_user)
    if request.method == "POST":
        new_user = User(
            name=request.form.get("Name"),
            email=request.form.get("Email"),
            dob=datetime.strptime(request.form.get("Dob"), "%Y-%m-%d"),
            phone=request.form.get("Phone"),
            password=generate_password_hash(request.form.get("Password")),
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("signup.html", user=current_user)
    return "Invalid method"

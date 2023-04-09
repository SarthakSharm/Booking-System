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
            if user.is_admin == True:
                flash("Login using admin login!", category="warning")
                return redirect(url_for("auth.adminLogin"))
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/admin/login", methods=["GET", "POST"])
def adminLogin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user.is_admin == True:
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("views.home"))
                else:
                    flash("Incorrect password, try again.", category="error")
            else:
                flash("Email does not exist.", category="error")
        else:
            flash("This is only for admin", category="error")

    return render_template("login.html", user=current_user, admin=True)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        # Handle GET request
        return render_template("signup.html", user=current_user)
    if request.method == "POST":
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            dob=datetime.strptime(request.form.get("dob"), "%Y-%m-%d"),
            phone=request.form.get("phone"),
            password=generate_password_hash(request.form.get("password")),
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("signup.html", user=current_user)
    return "Invalid method"

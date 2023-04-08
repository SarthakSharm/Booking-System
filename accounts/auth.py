from flask import Blueprint, request, render_template
from accounts.models import User
from datetime import datetime
from website import db

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login")
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        # Handle GET request
        return render_template("signup.html")
    if request.method == "POST":
        new_user = User(
            name=request.form["Name"],
            email=request.form["Email"],
            dob=datetime.strptime(request.form["Dob"], "%Y-%m-%d"),
            phone=request.form["Phone"],
            password=request.form["Password"],
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("signup.html")
    return "Invalid method"

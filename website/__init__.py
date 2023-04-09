from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "project.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecretkasdfliasgafudbi2134rlisdjkbf"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from accounts.auth import auth
    from shows.views import show
    from venue.views import venue
    from ticket.views import ticket

    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(venue)
    app.register_blueprint(show)
    app.register_blueprint(ticket)

    from accounts.models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("DB Created")

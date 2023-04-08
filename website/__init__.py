from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
app.config['SECRET_KEY'] = ''

from .views import views
from accounts.auth import auth

app.register_blueprint(views)
app.register_blueprint(auth)


def create_app():
    return app
    
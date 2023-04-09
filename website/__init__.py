from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "project.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from accounts.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from accounts.models import User
    with app.app_context():
        db.create_all()

    return app
    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print("DB Created")
from flask import Blueprint, jsonify, request, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from flask import session
from db import db, User
from pages.songs.songs import songs
from pages.auth.auth import auth, bcrypt
from pages.index.index import index
from pages.search.search import search
import os

SECRET_KEY = os.urandom(32)
application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
application.config["SECRET_KEY"] = SECRET_KEY

login_manager = LoginManager(application)
login_manager.login_view = "auth.login"
bcrypt.init_app(application)

db.init_app(application)
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


application.register_blueprint(songs)
application.register_blueprint(auth)
application.register_blueprint(index)
application.register_blueprint(search)


if __name__ == "__main__":
    application.run(debug=True, port=5001)

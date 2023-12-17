from flask import Blueprint, jsonify, request, render_template, flash, redirect, url_for
from db import User, db
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import timedelta
from pages.auth.forms.loginForm import LoginForm
from pages.auth.forms.registerForm import RegisterForm

auth = Blueprint("auth", __name__, template_folder="templates")
bcrypt = Bcrypt()


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("songs.getSongs"))
        return render_template(
            "auth.html", title="Login", form=LoginForm(), buttonAction="Login"
        )

    elif request.method == "POST":
        user = (
            User.query.filter_by(email=request.form["email"]).first()
            or User.query.filter_by(username=request.form["email"]).first()
        )

        if not user:
            flash("User does not exist", "danger")
            return redirect(url_for("auth.login"))
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("Incorrect password", "danger")
            return redirect(url_for("auth.login"))
        login_user(user, remember=True, duration=timedelta(days=365), force=True)
        return redirect(url_for("index.home"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template(
            "auth.html", title="Register", form=RegisterForm(), buttonAction="Register"
        )

    elif request.method == "POST":
        user = (
            User.query.filter_by(email=request.form["email"]).first()
            or User.query.filter_by(name=request.form["username"]).first()
        )

        if user:
            flash("User already exists", "danger")
            return redirect(url_for("auth.login"))
        user = User(
            username=request.form["username"],
            name=request.form["name"],
            email=request.form["email"],
            password=bcrypt.generate_password_hash(password=request.form["password"]),
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

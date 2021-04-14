from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False
    # if the user doesn't exist or password is wrong, reload the page
    if email == "" or password == "":
        flash("Please input your details.")
        return redirect(url_for("auth.login"))

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    if user.email == "admin@email.com":
        return redirect(url_for("main.admin_profile"))

    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")
    if email == "" or name == "" or password == "":
        flash("Please input your details. If you have an account, you may")
        return redirect(url_for("auth.signup"))

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address already exists. You may")
        return redirect(url_for("auth.signup"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    else:
        new_user = User(
            email=email,
            name=name,
            password=generate_password_hash(password, method="sha256"),
        )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

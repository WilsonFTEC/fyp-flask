from flask import Blueprint, app, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from jinja2.utils import urlize
from . import db
from fyp.decision import Prediction
from .models import User, Car
from datetime import datetime, timedelta
import json
import numpy as np
import requests


main = Blueprint("main", __name__)


@main.route("/")
@login_required
def profile():
    amount = round(current_user.result, 2)
    return render_template(
        "profile.html",
        name=current_user.name,
        email=current_user.email,
        result=amount,
    )


@main.route("/newapplication")
@login_required
def newapplication():
    email = current_user.email
    user = Car.query.filter_by(email=email).all()
    for u in user:
        if "running" in u.status:
            return render_template("loading.html", applicationNumber=u.aid)
    return render_template("NewApplication.html")


@main.route("/newapplication", methods=["POST"])
@login_required
def newapplication_post():
    all_user = Car.query.all()
    aid = "C0000" + str(len(all_user) + 1)
    email = current_user.email

    if request.method == "POST":
        time = datetime.today().date()
        new_application = Car(
            aid=aid,
            A=0,
            B=0,
            C=0,
            D=0,
            E=0,
            F=0,
            G=0,
            H=0,
            I=0,
            J=0,
            email=email,
            status="running",
            date=time,
            result=0,
        )
        db.session.add(new_application)
        db.session.commit()

    return redirect(url_for("main.newapplication"))


@main.route("/report")
@login_required
def report():
    email = current_user.email
    all_user = Car.query.filter_by(email=email).all()
    user = all_user[len(all_user) - 1]
    r = ["Invalid File Format"]
    reason = r[0]
    amount = 0
    status = user.status
    amount = round(user.result, 2)
    applicationNumber = user.aid
    return render_template(
        "Report.html",
        name=current_user.name,
        reason=reason,
        status=status,
        applicationNumber=applicationNumber,
        amount=amount,
    )


@main.route("/trackprogress")
@login_required
def trackprogress():
    email = current_user.email
    all_user = Car.query.filter_by(email=email).all()
    user = all_user[len(all_user) - 1]
    status = user.status
    time = user.date
    if status != "":
        value = round(user.result, 2)
    return render_template(
        "TrackProgress.html",
        name=current_user.name,
        status=status,
        time=time,
        value=value,
    )


@main.route("/virtualassit")
@login_required
def virtualassit():

    return render_template("VirtualAssistant.html")


@main.route("/predict")
@login_required
def predict():
    user = Car.query.filter_by(email=current_user.email, status="running").first()
    return render_template("predict.html", value=user.result)


@main.route("/predict", methods=["POST"])
@login_required
def predict_post():
    result = 0
    if request.method == "POST":
        user = Car.query.filter_by(email=current_user.email, status="running").first()
        if user.result > 0:
            flash("You have made the prediction!")
            return redirect(url_for("main.trackprogress"))
        # hardcoding
        # A = int(request.form.get("ca"))
        url_api = "https://api.ocr.space/parse/image"
        with open("/home/wilson/fyp/fyp-flask/fyp/data/files/image.png", "rb") as f:
            result = requests.post(
                url_api,
                files={"abc.png": f},
                data={"apikey": "bf7420f44f88957", "language": "eng"},
            )

        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")
        output = []
        for t in text_detected:
            output.append(ord(t) - 64)

        data = [output[:10]]
        prediction = Prediction(data)
        result = prediction.test()
        
        user.result = result
        user.A=output[0]
        user.B=output[1]
        user.C=output[2]
        user.D=output[3]
        user.E=output[4]
        user.F=output[5]
        user.G=output[6]
        user.H=output[7]
        user.I=output[8]
        user.J=output[9]

        # update data to the database
        db.session.commit()
    return redirect(url_for("main.trackprogress"))


@main.route("/admin")
@login_required
def admin():
    all_user = Car.query.filter_by(status="running").all()

    posts = []

    for user in all_user:
        post = {"number": user.aid, "email": user.email, "date": (user.date)[5:]}
        posts.append(post)

    user_amount = 0
    if len(posts) > 0:
        user_amount = 1

    # return str(user_amount)
    return render_template("admin.html", posts=posts, user_amount=user_amount)


@main.route("/admin", methods=["POST"])
@login_required
def admin_post():
    all_user = Car.query.filter_by(status="running").all()
    status = [""]
    if request.method == "POST":

        status = request.form.getlist("ca")
        i = 0
        for user in all_user:
            if status is not None:
                user.status = status[i]
                profile = User.query.filter_by(email=user.email).first()
                if status[i] == "passed":
                    profile.result = user.result
                else:
                    profile.result = 0
                    user.result = 0
                db.session.commit()

                i = i + 1

    return redirect(url_for("main.admin"))


@main.route("/adminprofile")
@login_required
def admin_profile():
    return render_template(
        "admin_profile.html",
        name=current_user.name,
        email=current_user.email,
    )


@main.route("/test")
@login_required
def test():
    return render_template("test.html")

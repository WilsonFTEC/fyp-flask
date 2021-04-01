from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from fyp.decision import Prediction

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    result = 0
    if request.method == "POST":
        data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        prediction = Prediction(data)
        result = prediction.test()
        return render_template("index.html", title="AI Page | Dashboard", value=result)
    else:
        return render_template("index.html", title="AI Page | Dashboard")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name, email=current_user.email)
    # return render_template('NewApplication.html')


@main.route("/newapplication")
def newapplication():
    return render_template("NewApplication.html")


@main.route("/report")
def report():
    return render_template("Report.html")


@main.route("/trackprogress")
def trackprogress():
    return render_template("TrackProgress.html")


@main.route("/user")
def user():
    return render_template("UserPortfolio.html")


@main.route("/virtualassit")
def virtualassit():
    return render_template("VirtualAssistant.html")
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from fyp.decision import Prediction
from .models import User
from datetime import datetime

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
    user_id = "C0000" + str(current_user.id)
    return render_template("NewApplication.html", applicationNumber=user_id)


@main.route("/report")
@login_required
def report():
    reason = "Invalid file"
    status = ""
    return render_template(
        "Report.html", name=current_user.name, reason=reason, status=status
    )


@main.route("/trackprogress")
@login_required
def trackprogress():
    status = "running"
    return render_template("TrackProgress.html", name=current_user.name, status=status)


@main.route("/virtualassit")
@login_required
def virtualassit():
    return render_template("VirtualAssistant.html")


@main.route("/predict", methods=["GET", "POST"])
@login_required
def index():
    result = 0
    if request.method == "POST":
        # hardcoding
        data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        prediction = Prediction(data)
        result = prediction.test()
        user = User.query.filter_by(email=current_user.email).first()
        user.result = result

        # update data to the database
        db.session.commit()
        return render_template("index.html", title="AI Page | Dashboard", value=result)
    else:
        return render_template("index.html", title="AI Page | Dashboard")


@main.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    number = ["C00001", "C00002"]
    time = datetime.today().date()
    post = [
        {"number": number[0], "name": "abc", "date": time},
        {"number": number[1], "name": "cde", "date": time},
    ]
    return render_template("admin.html", posts=post)


@main.route("/test")
@login_required
def test():
    return render_template("test.html", test=111, a="0")
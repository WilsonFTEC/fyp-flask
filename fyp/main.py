from flask import Blueprint, app, render_template, request
from flask_login import login_required, current_user
from . import db
from fyp.decision import Prediction
from .models import User, Car
from datetime import datetime, timedelta

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
    aid = "C0000" + str(current_user.id)
    email = current_user.email
    # new_application = Car(aid=aid, email=email)
    # db.session.add(new_application)
    # db.session.commit()

    return render_template("NewApplication.html", applicationNumber=aid)


@main.route("/report")
@login_required
def report():
    r = ["Invalid File Format"]
    reason = r[0]
    if not current_user.status:
        status = ""
    else:
        status = current_user.status
    status = "failed"
    applicationNumber = "C0000" + str(current_user.id)
    amount = round(current_user.result, 2)
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
    if not current_user.status:
        status = ""
    else:
        status = current_user.status
    status = "failed"
    time = datetime.today().date()
    return render_template(
        "TrackProgress.html", name=current_user.name, status=status, time=time
    )


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
    #number = Car.query.filer_by(email="running").all()
    time = (datetime.today() - timedelta(1)).date()
    post = [
        {"number": "C00001", "name": "test1", "date": time},
        {"number": "C00002", "name": "test2", "date": time},
        {"number": "C00003", "name": "test3", "date": time},

    ]
    return render_template("admin.html", posts=post)


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
    return render_template("test.html", test=111, a="0")
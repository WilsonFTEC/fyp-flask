from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from fyp.decision import Prediction
from .models import User

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
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


@main.route("/user")
@login_required
def profile():
    return render_template(
        "profile.html",
        name=current_user.name,
        email=current_user.email,
        result=current_user.result,
    )


@main.route("/newapplication")
@login_required
def newapplication():
    user_id = "C0000" + str(current_user.id)
    return render_template("NewApplication.html", applicationNumber=user_id)


@main.route("/report")
@login_required
def report():
    user_id = "C0000" + str(current_user.id)
    return render_template(
        "Report.html", name=current_user.name, applicationNumber=user_id
    )


@main.route("/trackprogress")
@login_required
def trackprogress():
    return render_template("TrackProgress.html")


@main.route("/modiuser")
@login_required
def user():
    return render_template("UserPortfolio.html")


@main.route("/virtualassit")
@login_required
def virtualassit():
    return render_template("VirtualAssistant.html")

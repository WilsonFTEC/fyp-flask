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


@main.route("/newapplication", methods=["GET", "POST"])
@login_required
def newapplication():
    if request.method == "POST":
        all_user = Car.query.all()
        aid = "C0000" + str(len(all_user) + 1)
        email = current_user.email
        user = Car.query.filter_by(email=email).all()
        for u in user:
            if "running" in u.status:
                print(u.status)
                return render_template("test.html", test=user)
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
        return render_template("NewApplication.html", applicationNumber=aid)

    return render_template("NewApplication.html")


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
    if not current_user.status:
        status = ""
    else:
        status = current_user.status
    status = "running"
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
        A = int(request.form.get("ca"))
        data = [[A, 0, 0, 0, 5, 7, 1, 6, 3, 3]]
        prediction = Prediction(data)
        result = prediction.test()
        # result = data
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
    all_user = Car.query.filter_by(status="running").all()

    posts = []

    for user in all_user:
        post = {"number": user.aid, "email": user.email, "date": (user.date)[5:]}
        posts.append(post)

    user_amount = 0
    if len(posts) > 0:
        user_amount = 1

    status = [""]
    if request.method == "POST":
        
        status = request.form.getlist("ca")
        i = 0
        for user in all_user:
            user.status = status[i]
            db.session.commit()

            i = i + 1

    return render_template(
        "admin.html", posts=posts, status=status, user_amount=user_amount
    )


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
    email = current_user.email
    all_user = Car.query.filter_by(status="running").all()

    posts = []

    for user in all_user:
        post = {"number": user.aid, "name": user.email, "date": user.date}
        posts.append(post)

    return render_template("test.html", test=posts)

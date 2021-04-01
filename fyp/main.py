from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    #return render_template('NewApplication.html')

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
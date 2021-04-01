# from flask import Flask, render_template, request
# from flask import flash, redirect, session, abort
# import os
# from decision import Prediction

# app = Flask(__name__)

# @app.route("/")
# def home():
#     if not session.get('logged_in'):
#         return render_template('Login.html')
#     else:
#         return index()

# @app.route("/index", methods=['GET', 'POST'])
# def index():
#     result = 0
#     if request.method == 'POST':
#         data = [[1,1,1,1,1,1,1,1,1,1]]
#         prediction = Prediction(data)
#         result = prediction.test()
#         return render_template("index.html", title="AI Page | Dashboard", value=result)
#     else:
#         return render_template("index.html", title="AI Page | Dashboard")

# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return home()

# @app.route("/logout")
# def logout():
#     session['logged_in'] = False
#     return home()

# @app.route("/newapplication")
# def newapplication():
#     return render_template("NewApplication.html")

# @app.route("/report")
# def report():
#     return render_template("Report.html")

# @app.route("/trackprogress")
# def trackprogress():
#     return render_template("TrackProgress.html")

# @app.route("/user")
# def user():
#     return render_template("UserPortfolio.html")

# @app.route("/virtualassit")
# def virtualassit():
#     return render_template("VirtualAssistant.html")

# app.secret_key = os.urandom(12)

# if __name__ == '__main__':
#     app.run(debug=True) # disable debug=True in production
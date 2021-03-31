from flask import Flask, render_template, request
from decision import Fruit

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    weight = texture = result = 0
    if request.method == 'POST':
        weight = request.form['weight']
        texture = request.form['texture']
        fruit = Fruit(weight, result)
        fruit.train()
        result = fruit.test()
        return render_template("index.html", title="Hello AI", value=result)
    else:
        return render_template("index.html", title="Hello AI")

@app.route("/newapplication")
def newapplication():
    return render_template("NewApplication.html")

@app.route("/report")
def report():
    return render_template("Report.html")

@app.route("/trackprogress")
def trackprogress():
    return render_template("TrackProgress.html")

@app.route("/user")
def user():
    return render_template("UserPortfolio.html")

@app.route("/virtualassit")
def virtualassit():
    return render_template("VirtualAssistant.html")

if __name__ == '__main__':
    app.run() # disable debug=True in production
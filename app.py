from flask import Flask, render_template, request
from decision import Prediction

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    result = 0
    if request.method == 'POST':
        data = [[1,1,1,1,1,1,1,1,1,1]]
        prediction = Prediction(data)
        result = prediction.test()
        return render_template("index.html", title="AI Page | Dashboard", value=result)
    else:
        return render_template("index.html", title="AI Page | Dashboard")


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
    app.run(debug=True) # disable debug=True in production
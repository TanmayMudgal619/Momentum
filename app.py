from flask import Flask, url_for, render_template, request
from requests import api
import apis
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form["lat"], request.form["lon"])
        quote = apis.getQuote()
        temp = apis.getTemp(request.form["lat"], request.form["lon"])
        bg = apis.getBG()
        return render_template("index.html", title="Momentum", quote=quote, temp=temp, bg=bg)
    return render_template("load.html", title="Momentum")


if __name__ == '__main__':
    app.run(debug=True)

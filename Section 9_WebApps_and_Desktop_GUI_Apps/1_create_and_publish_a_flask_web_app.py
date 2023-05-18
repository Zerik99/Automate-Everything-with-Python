"""Module that creates and publishes a flask web app"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    """Home page of the web app"""
    return render_template("index.html")


@app.route("/", methods=["POST"])
def home_post():
    """Home page method that handles post requests"""
    dim_1 = request.form["first_dim"]
    dim_2 = request.form["second_dim"]
    dim_3 = request.form["third_dim"]
    volume = float(dim_1) * float(dim_2) * float(dim_3)

    return render_template(
        "index.html", output=volume, dim_1=dim_1, dim_2=dim_2, dim_3=dim_3
    )


app.run()

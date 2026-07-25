from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import datetime
import os

app = Flask(__name__)
BASE_DIR=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, "sandbox.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Sandbox(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    sandbox_id = db.Column(db.String(50))

    username = db.Column(db.String(100))

    email = db.Column(db.String(100))

    environment = db.Column(db.String(50))

    region = db.Column(db.String(50))

    status = db.Column(db.String(50))


@app.route("/")
def home():

    count = Sandbox.query.count()

    return render_template(
        "index.html",
        count=count
    )


@app.route("/request", methods=["GET","POST"])
def sandbox_request():

    if request.method == "POST":

        sandbox_id = "SBX-" + str(random.randint(10000,99999))

        new_request = Sandbox(

            sandbox_id=sandbox_id,

            username=request.form["username"],

            email=request.form["email"],

            environment=request.form["environment"],

            region=request.form["region"],

            status="Requested"

        )


        db.session.add(new_request)

        db.session.commit()


        return redirect("/dashboard")


    return render_template("request.html")



@app.route("/dashboard")
def dashboard():

    sandboxes = Sandbox.query.all()

    return render_template(

        "dashboard.html",

        sandboxes=sandboxes

    )


@app.route("/update/<int:id>")
def update_status(id):

    sandbox = Sandbox.query.get(id)

    if sandbox:

        if sandbox.status == "Requested":

            sandbox.status="Provisioning"

        elif sandbox.status == "Provisioning":

            sandbox.status="Completed"


        db.session.commit()


    return redirect("/dashboard")



@app.route("/about")
def about():

    return render_template("about.html")



with app.app_context():

    db.create_all()



if __name__=="__main__":

    app.run(host="0.0.0.0",port=8000, debug=True)

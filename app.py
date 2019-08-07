from flask import Flask, render_template, request
import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind = engine))

app = Flask(__name__)
@app.route("/")
def home():
     return render_template("home.html")

@app.route("/register")
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    user_exist = db.execute("SELECT username from loginDB WHERE username = ':username'",{"username":username})
    if user_exist == None:
        db.execute("INSERT INTO loginDB (username, password) VALUES (:username,:password)" ,{"username":username,"password":password})
        return render_template("login.html")
    else:
        print ("<h6> username already exists</h6>")
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)

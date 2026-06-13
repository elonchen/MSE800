from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import db
from utils import hash_password
from utils import verify_password

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    full_name = request.form["full_name"]
    dob = request.form["date_of_birth"]
    email = request.form["email"]
    password = request.form["password"]

    if db.get_user_by_email(email):
        return "Email already exists"

    password_hash = hash_password(password)

    db.insert_user(
        email,
        password_hash,
        full_name,
        dob
    )

    return redirect("/login")



@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    password = request.form["password"]

    user = db.get_user_by_email(email)

    if user is None:
        return "Invalid email"

    if not verify_password(user["password_hash"], password):
        return "Wrong password"

    session["email"] = email

    return redirect("/profile")



@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
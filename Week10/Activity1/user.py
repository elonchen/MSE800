from datetime import datetime

from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect

import db
from utils import gen_reset_token
from utils import hash_password
from utils import send_email

user_bp = Blueprint("user", __name__)


# Profile
@user_bp.route("/profile", methods=["GET", "POST"])
def profile():

    email = session.get("email")

    if email is None:
        return redirect("/login")

    user = db.get_user_by_email(email)

    if request.method == "GET":
        return render_template(
            "profile.html",
            user=user
        )

    full_name = request.form["full_name"]
    dob = request.form["date_of_birth"]

    db.update_profile(
        email,
        full_name,
        dob
    )

    return redirect("/profile")


# Forgot Password
@user_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "GET":
        return render_template(
            "forgot_password.html"
        )

    email = request.form["email"]

    user = db.get_user_by_email(email)

    if user is None:
        return "Email not found"

    token, expires = gen_reset_token()

    db.save_reset_token(
        email,
        token,
        expires.isoformat()
    )

    send_email(email, token)

    return "Reset email sent (check terminal output)"


# Reset Password
@user_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):

    user = db.get_user_by_token(token)

    if user is None:
        return "Invalid token"

    expires = datetime.fromisoformat(
        user["reset_expires"]
    )

    if datetime.now() > expires:
        return "Token expired"

    if request.method == "GET":
        return render_template(
            "reset_password.html"
        )

    new_password = request.form["password"]

    password_hash = hash_password(
        new_password
    )

    db.update_password(
        user["email"],
        password_hash
    )

    return redirect("/login")
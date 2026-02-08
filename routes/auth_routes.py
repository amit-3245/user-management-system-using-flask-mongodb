from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import create_user, authenticate_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = authenticate_user(email, password)

        if user:
            session["user_id"] = str(user["_id"])
            session["user_name"] = user["name"]
            session["role"] = user.get("role", "user")
            return redirect(url_for("users.dashboard"))
        else:
            flash("Invalid email or password", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        result = create_user(name, email, password)

        if result["status"]:
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(result["message"], "danger")

    return render_template("auth/register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

users_bp = Blueprint("users", __name__)


def login_required():
    """
    Simple login check
    """
    return "user_id" in session


@users_bp.route("/dashboard")
def dashboard():
    if not login_required():
        return redirect(url_for("auth.login"))

    return render_template(
        "users/dashboard.html",
        user_name=session.get("user_name"),
        role=session.get("role")
    )


@users_bp.route("/users")
def user_list():
    if not login_required():
        return redirect(url_for("auth.login"))

    users = get_all_users()
    return render_template("users/user_list.html", users=users)


@users_bp.route("/users/add", methods=["GET", "POST"])
def add_user():
    if not login_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role", "user")

        result = create_user(name, email, password, role)

        if result["status"]:
            flash("User added successfully", "success")
            return redirect(url_for("users.user_list"))
        else:
            flash(result["message"], "danger")

    return render_template("users/add_user.html")


@users_bp.route("/users/edit/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not login_required():
        return redirect(url_for("auth.login"))

    user = get_user_by_id(user_id)

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        role = request.form.get("role")

        update_user(user_id, name, email, role)
        flash("User updated successfully", "success")
        return redirect(url_for("users.user_list"))

    return render_template("users/edit_user.html", user=user)


@users_bp.route("/users/delete/<user_id>")
def remove_user(user_id):
    if not login_required():
        return redirect(url_for("auth.login"))

    delete_user(user_id)
    flash("User deleted successfully", "success")
    return redirect(url_for("users.user_list"))

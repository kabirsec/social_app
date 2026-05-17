from flask import render_template, request, redirect, session
from services.auth_service import register_user, login_user

def register():
    if request.method == "POST":
        register_user(
            request.form["username"],
            request.form["password"]
        )
        return redirect("/login")
    return render_template("register.html")

def login():
    if request.method == "POST":
        user = login_user(
            request.form["username"],
            request.form["password"]
        )
        if user:
            session["user_id"] = user[0]
            return redirect("/")
    return render_template("login.html")

def logout():
    session.clear()
    return redirect("/login")

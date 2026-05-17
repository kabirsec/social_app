from flask import render_template, session, redirect
from services.post_service import get_posts

def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    posts = get_posts()
    return render_template("dashboard.html", posts=posts)

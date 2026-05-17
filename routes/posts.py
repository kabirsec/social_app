from flask import request, redirect, render_template, session
from services.post_service import create_post_db, get_posts

def create_post():
    create_post_db(
        session["user_id"],
        request.form["content"]
    )
    return redirect("/")

def view_post(id):
    return f"Post ID: {id}"

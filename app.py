from flask import Flask
from routes.auth import login, register, logout
from routes.dashboard import dashboard
from routes.posts import create_post, view_post

app = Flask(__name__)
app.secret_key = "secret123"

# AUTH
app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
app.add_url_rule("/register", view_func=register, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=logout)

# PAGES
app.add_url_rule("/", view_func=dashboard)
app.add_url_rule("/post", view_func=create_post, methods=["POST"])
app.add_url_rule("/post/<int:id>", view_func=view_post)

if __name__ == "__main__":
    app.run(debug=True)

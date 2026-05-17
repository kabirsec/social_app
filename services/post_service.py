from models import get_db

def create_post_db(user_id, content):
    db = get_db()
    db.execute(
        "INSERT INTO posts (user_id, content) VALUES (?, ?)",
        (user_id, content)
    )
    db.commit()

def get_posts():
    db = get_db()
    return db.execute("SELECT * FROM posts").fetchall()


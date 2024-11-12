from flask import Flask, request, render_template
from database.db import get_db_connection

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # the raw squealy goodness zaddy
    query = """
    select p.content c, p.posted_at pa, u.username un
    from posts p
    join users u on p.user_id = u.user_id
    """
    
    cursor.execute(query)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

# TODO:
# implement session management
# implement create operation (HTTP POST)
# implement update operation (HTTP PUT)
# implement delete operation (HTTP DELETE)

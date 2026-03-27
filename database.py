import sqlite3


def init_db():
    """
    Initilizes database if it does not already exist
    """

    connect = sqlite3.connect("history.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, subject TEXT, content TEXT, date TEXT);""")
    connect.commit()
    connect.close()

def insert_post(title, subject, content, date):
    """
    Inserts post into the SQL database.
    """
    connect = sqlite3.connect("history.db")
    cursor = connect.cursor()
    cmd = "INSERT INTO posts (title, subject, content, date) VALUES (?, ?, ?, ?);"
    cursor.execute(cmd, (title, subject, content, date))
    connect.commit()
    connect.close()


def get_posts():
    """
    Return's posts from the SQL Database using query statements 
    """
    connect = sqlite3.connect("history.db")
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM posts ORDER BY id DESC;")
    results = cursor.fetchall()
    connect.close()
    return results

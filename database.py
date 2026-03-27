import psycopg2

def conn():
    connect = psycopg2.connect(
        dbname="history_ntbx",
        user="history_ntbx_user",
        password="REMOVED",
        host="REMOVED",
        port="5432"
    )
    return connect


def init_db():
    """
    Initilizes database if it does not already exist
    """
    connect = conn()
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS posts(id SERIAL PRIMARY KEY, title TEXT, subject TEXT, content TEXT, date TEXT);""")
    connect.commit()
    connect.close()

def insert_post(title, subject, content, date):
    """
    Inserts post into the Postgres database.
    """
    connect = conn()
    cursor = connect.cursor()
    cmd = "INSERT INTO posts (title, subject, content, date) VALUES (%s, %s, %s, %s);"
    cursor.execute(cmd, (title, subject, content, date))
    connect.commit()
    connect.close()


def get_posts():
    """
    Return's posts from the Postgres Database using query statements 
    """
    connect = conn()
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM posts ORDER BY id DESC;")
    results = cursor.fetchall()
    connect.close()
    return results

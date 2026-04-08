import os
import psycopg2
from dotenv import load_dotenv
import logging

load_dotenv()

DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

def conn():
    connect = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_URL,
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
    try:
        cursor = connect.cursor()
        cmd = "INSERT INTO posts (title, subject, content, date) VALUES (%s, %s, %s, %s);"
        cursor.execute(cmd, (title, subject, content, date))
        connect.commit()
        return True
    except Exception as e:
        connect.rollback()
        logging.error(f"Python raised an except and failed to insert post, printed error: {e}")
        return False
    finally:    
        connect.close()

def get_posts():
    """
    Return's posts from the Postgres Database using query statements 
    """
    connect = conn()
    cursor = connect.cursor()
    cursor.execute(f"SELECT id, title, subject, content, date, ROW_NUMBER() OVER (ORDER BY id) AS day_number FROM posts ORDER BY id DESC;")
    results = cursor.fetchall()
    connect.close()
    return results

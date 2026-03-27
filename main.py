from flask import Flask, render_template, request
import datetime
from database import init_db, insert_post, get_posts
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.environ.get("PASSWORD")

app = Flask(__name__)

init_db()
print(PASSWORD)
@app.route("/")
def hello_world():
    results = get_posts()
    return render_template('index.html', posts=results)

@app.route("/newpost", methods=['POST', 'GET'])
def newpost():
    return render_template('new.html')

@app.route("/submit", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            post_title = request.form['title']
            post_subject = request.form['subject']
            post_content = request.form['content']
            date = datetime.datetime.now().strftime("%H:%M %A %B %d %Y")
            insert_post(post_title, post_subject, post_content, date)
            return render_template('success.html')
        else:
            return "Unauthorised", 403


app.run(host='0.0.0.0', port=5000, debug=True)
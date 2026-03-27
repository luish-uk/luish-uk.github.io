from flask import Flask, render_template, request
import datetime
from database import init_db, insert_post, get_posts

app = Flask(__name__)

init_db()


@app.route("/")
def hello_world():
    results = get_posts()
    return render_template('index.html', posts=results)

@app.route("/newpost", methods=['POST', 'GET'])
def newpost():
    return render_template('new.html')

@app.route("/success", methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        post_title = request.form['title']
        post_subject = request.form['subject']
        post_content = request.form['content']
        date = datetime.datetime.now().strftime("%x %I:%M")
        post = "<article><h2>%s</h2><h3>%s</h3><p>%s</p><footer>%s</footer></article>" % (post_title, post_subject, post_content, date)
        insert_post(post_title, post_subject, post_content, date)
    return render_template('success.html')


app.run(host="0.0.0.0", port=5000)


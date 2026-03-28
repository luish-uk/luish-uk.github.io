from flask import Flask, render_template, request #Used as the frontend/backend
import datetime #For date and time of posts 
from database import init_db, insert_post, get_posts #Database of posts
from dotenv import load_dotenv 
import os
import hmac #For avoiding timing attacks
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR) #Adding log file

load_dotenv() 

#Initilize .env

PASSWORD = os.environ.get("PASSWORD")
DEBUG = os.environ.get("DEBUG")

app = Flask(__name__)

init_db() #Runs db setup 



@app.route("/")
def hello_world():
    results = get_posts()
    return render_template('index.html', posts=results)

@app.route("/newpost", methods=['GET'])
def newpost():
    return render_template('new.html')

@app.route("/submit", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        if hmac.compare_digest(request.form['password'], PASSWORD): 
            post_title = request.form['title']
            post_subject = request.form['subject']
            post_content = request.form['content']
            date = datetime.datetime.now().strftime("%H:%M %A %B %d %Y")
            insert_post(post_title, post_subject, post_content, date)
            return render_template('success.html')
        else:
            return "Unauthorised", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)

from app import app
# FROM APP FOLDER import app OBJECT

from flask import render_template

# function to route funciton to localhost server. Also gives the URL route name. 
# Use this as href when making links. Make sure render is imported to do so
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

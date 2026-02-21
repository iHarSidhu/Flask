from learnFlaskApp import app
from flask import render_template

@app.route('/')
@app.route('/index/<int:count>')
def index(count=0):
    info = { 'heading': 'This is Flask index page' }
    return render_template('index.html', other='This is a kind of paragraph', info=info, count=count)

@app.route('/profile')
def profileRoute():
    info = { 'heading': 'This is Profile page' }
    return render_template('newPage.html', other='Welcome to the new page!', info=info)
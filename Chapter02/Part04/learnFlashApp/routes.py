from learnFlaskApp import app
from flask import render_template

@app.route('/')
@app.route('/index/<int:count>')
def index(count):
    info = { 'heading': 'This is Flask index page' }
    return render_template('index.html', other='This is a kind of paragraph', info=info, count=count)
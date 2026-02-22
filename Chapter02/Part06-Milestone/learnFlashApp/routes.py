from learnFlaskApp import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    info = { 'heading': 'Flask index page' }
    return render_template('index.html', other='This is a kind of paragraph', info=info)

@app.route('/profile')
@app.route('/profile/<int:count>')
def profileRoute(count=0):
    info = { 'heading': 'Profile page' }
    return render_template('profile.html', other='Welcome to the new page!', info=info, count=count)

@app.route('/query')
def queryStringRoute():
    qry = request.args.get('qryInt', default=0, type=int)

    info = { 'heading': 'Query page' }

    return render_template(
        'query.html',
        other='We are passing int in query string where default value is zero',
        info=info,
        qry=qry
    )

@app.route('/countQuery')
@app.route('/countQuery/<int:count>')
def countQuery(count=0):
    qry = request.args.get('qryStr', default=0, type=int)

    info = { 'heading': 'Count and query string page' }

    return render_template(
        'countquery.html',
        other='Both Count and query string have a value of zero',
        info=info,
        count=count,
        qry=qry
    )
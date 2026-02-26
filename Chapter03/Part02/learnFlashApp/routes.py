from learnFlaskApp import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    info = { 'heading': 'Flask index page' }
    return render_template('index.html', other='This is a kind of paragraph', info=info, pageTitle='Welcome: Index Page')

@app.route('/profile')
@app.route('/profile/<int:count>')
def profileRoute(count=0):
    info = { 'heading': 'Profile page' }
    return render_template('profile.html', other='Welcome to the new page!', info=info, count=count, pageTitle='Profile Page')

@app.route('/query')
def queryStringRoute():
    qry = request.args.get('qryInt', default=0, type=int)

    info = { 'heading': 'Query page' }

    return render_template(
        'query.html',
        other='We are passing int in query string where default value is zero',
        info=info,
        qry=qry,
        pageTitle='Passing Query'
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
        qry=qry, 
        pageTitle='Passing Query and Count'
    )

@app.route('/posts')
def showPosts():
    info = { 'heading': 'For Loop on Static post' }
    border = False #True

    myPosts = [
        {
            'title' : 'Finibus Bonorum et Malorum',
            'body'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        },
        {
            'title' : 'Accusantium Doloremque Laudantium',
            'body'  : 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.'
        },
        {
            'title' : 'Sed Quia Non Numquam Dolorem',
            'body'  : 'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'
        }
    ]
    return render_template('posts.html', info=info, pageTitle='Static Posts', posts=myPosts, border=border)

@app.errorhandler(404)
def error404(error):
    return render_template('errorPage.html', pageTitle='OOPs where am i??'), 404

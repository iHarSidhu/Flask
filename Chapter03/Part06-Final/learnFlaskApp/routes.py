from learnFlaskApp import app
from flask import render_template, request, redirect, url_for
from learnFlaskApp.models import Post
from learnFlaskApp.forms import Posts
from learnFlaskApp import db

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
    border = True #False #True

    myPosts = Post.query.all()
    return render_template('posts.html', info=info, pageTitle='Static Posts', posts=myPosts, border=border)

@app.route('/addpost', methods=['GET', 'POST'])
def addPosts():
    info = { 'heading': 'Create a new dynamic post' }
    form = Posts()

    if form.validate_on_submit():
        newPost = Post(title=form.title.data, body=form.body.data)
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('showPosts'))


    return render_template('newPost.html', info=info, pageTitle='Add New Dynamic Posts', form=form)

@app.route('/post/<int:post_id>/edit', methods=['GET','POST'])
def editPost(post_id):
    post = Post.query.get_or_404(post_id)
    # Preload data
    form = Posts(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.body  = form.body.data
        db.session.commit()
        return redirect(url_for('showPosts'))

    return render_template(
        'editPost.html', form=form, post=post, pageTitle='Edit Post', info={'heading': 'Edit Post'}
    )

@app.route('/post/<int:post_id>/delete', methods=['POST'])
def deletePost(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('showPosts'))

@app.errorhandler(404)
def error404(error):
    return render_template('errorPage.html', pageTitle='OOPs where am i??'), 404
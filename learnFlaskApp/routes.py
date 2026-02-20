from learnFlaskApp import app

@app.route('/')
def index():
    return 'My First Flask Page'
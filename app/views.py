from flask import render_template
from app import app

@app.route("/")
def index():
    '''
    views function to return page and its data
    '''

    return render_template('index.html')


@app.route("/about")
def about():
    '''
    views function to return about page
    '''
    title = 'About'
    return render_template('about.html', title = title)



from flask import render_template,request,url_for
from app import app

pitches = [
    {
        'author': 'Missy Olivia',
        'title': 'Blog Post 1',
        'content': 'First post ',
        'date_posted': 'Nov 2, 2020'
    },
    {
        'author': 'Magic Mikey',
        'title': 'Blog Post 2',
        'content': 'Second post ',
        'date_posted': 'Dec 6, 2020'
    }
]
@app.route("/")
def index():
    '''
    views function to return page and its data
    '''

    return render_template('index.html', pitches = pitches)


@app.route("/about")
def about():
    '''
    views function to return about page
    '''
    title = 'About'
    return render_template('about.html', title = title)



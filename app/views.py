from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from app import app
from flask_sqlalchemy import SQLAlchemy
from .forms import RegForm, loginForm
    



# dummy data
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

@app.route("/register", methods=['GET','POST'])
def register():
    '''
    views function to return registration form 
    '''
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Created account for {form.username.data}', 'success')
        return redirect(url_for('index'))
    title = 'Register'
    return render_template('register.html', title = title, form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    '''
    views function to return login Form 
    '''
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pitch.com' and form.password.data == 'password':
            flash('You have logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid login!', 'danger')
    title = 'Login'
    return render_template('login.html',title = title, form = form)

@app.route("/home")
def home():
    '''
    views function to return about page
    '''
    title = 'Homepage'
    return render_template('home.html', title = title)

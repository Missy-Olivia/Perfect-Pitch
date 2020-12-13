from flask import render_template,url_for,flash,redirect,abort
from flask_login import login_required, current_user
from . import main, db, bcrypt
from .forms import RegForm, loginForm
from ..models import User, Post
db.create_all() 

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
@main.route("/")
def index():
    '''
    views function to return page and its data
    '''

    return render_template('index.html', pitches = pitches)


@main.route("/about")
def about():
    '''
    views function to return about page
    '''
    title = 'About'
    return render_template('about.html', title = title)

@main.route("/register", methods=['GET','POST'])
def register():
    '''
    views function to return registration form 
    '''
    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Created account for {form.username.data}, Login Now!', 'success')
        return redirect(url_for('login'))
    title = 'Register'
    return render_template('register.html', title = title, form = form)


@main.route("/login", methods=['GET','POST'])
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

@main.route("/home")
def home():
    '''
    views function to return about page
    '''
    title = 'Homepage'
    return render_template('home.html', title = title)
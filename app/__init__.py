from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# initializing the application
app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '8ded178d6e7cbcda'
app.config['SQLALCHEMY__DATABASE__URI'] = 'sqlite:///site.db'
bcrypt = Bcrypt(app)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views

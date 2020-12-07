from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# initializing the application
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ded178d6e7cbcda'
app.config['SQLALCHEMY__DATABASE__URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views

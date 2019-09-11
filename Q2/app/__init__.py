from flask import Flask
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()
app = Flask(__name__)

from app import routes

app.config['SECRET_KEY'] = 'any secret string'

csrf.init_app(app)

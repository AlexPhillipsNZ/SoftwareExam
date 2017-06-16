from .flaskr import app

from flask import Flask
app = Flask(__name__)

import yourapplication.views


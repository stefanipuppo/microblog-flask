from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "plavra-secreta"

from app import routes
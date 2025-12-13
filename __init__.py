from flask import Flask

from controllers.base_view import b_view
from models.config import initialise

def create_app():
    app = Flask(__name__)
    app.secret_key = "dharshan"

    initialise()
    app.register_blueprint(b_view)

    return app

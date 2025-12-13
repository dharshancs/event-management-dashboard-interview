from flask import Flask

from controllers.base_view import u_view
from models.config import initialise

def create_app():
    app = Flask(__name__)
    app.secret_key = "dharshan"

    initialise()
    app.register_blueprint(u_view)

    return app

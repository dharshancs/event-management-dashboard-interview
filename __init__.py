from flask import Flask

from controllers.base_view import b_view
from controllers.user_view import u_view
from controllers.organiser_view import o_view
from models.config import initialise

def create_app():
    app = Flask(__name__)
    app.secret_key = "dharshan"

    initialise()
    app.register_blueprint(b_view)
    app.register_blueprint(u_view,url_prefix='/user')
    app.register_blueprint(o_view,url_prefix='/organiser')

    return app

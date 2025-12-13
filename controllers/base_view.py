from flask import Blueprint
from .__init__ import connect_database

u_view = Blueprint('base',__name__)


@u_view.route('/')
def home():
    return "Welcome"

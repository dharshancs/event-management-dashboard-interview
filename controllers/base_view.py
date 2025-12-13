from flask import Blueprint,render_template
from .__init__ import connect_database

u_view = Blueprint('base',__name__)


@u_view.route('/')
def home():
    return render_template("index.html")

@u_view.route('/register')
def register():
    return render_template("register.html")

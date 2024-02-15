from flask import Blueprint
from views.home_view import render_home_view

home_controller = Blueprint("home", __name__)

@home_controller.route("/home")
def home():
    return render_home_view()


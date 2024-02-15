from flask import Blueprint
from views.home_view import home_view

home_controller = Blueprint("home", __name__)

@home_controller.route("/home")
def home():
    return home_view()


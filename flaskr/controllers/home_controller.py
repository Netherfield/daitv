from models.movie import Movie, sqlite_config
from flask import Blueprint, jsonify
from views.home_view import render_home_view


home_controller = Blueprint("home", __name__)

@home_controller.route("/api/data/all_shows", methods=["GET"])
def get_shows():
    data = Movie.get_all_sqlite("films", sqlite_config.DB_ABSOLUTE_PATH)
    return jsonify([s.to_dict() for s in data])

@home_controller.route("/")
def home():
    return render_home_view(get_shows().json)


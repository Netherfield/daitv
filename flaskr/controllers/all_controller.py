from flask import Blueprint, jsonify
from views.all_view import render_all_view
from models.movie import Movie


view_controller = Blueprint("view", __name__)

@view_controller.route("/api/data/all_shows")
def shows():
    data = Movie.get_all_mongodb("films")
    return jsonify([s.to_dict() for s in data])

@view_controller.route("/all_shows")
def shows_viewer():
    data = shows()
    list_data = data.json
    return render_all_view(list_data)






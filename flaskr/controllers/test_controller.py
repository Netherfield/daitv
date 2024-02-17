from flask import Blueprint, jsonify
from views.test_view import render_test_view
from models.movie import Movie, sqlite_config

test_controller = Blueprint("test", __name__)


@test_controller.route("/<movieid>")
def sql_one_show(movieid):
    film = Movie.get_one_sqlite("films", movieid, sqlite_config.DB_ABSOLUTE_PATH)
    return render_test_view(film.to_dict())
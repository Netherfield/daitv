from flask import jsonify, Flask
from models.movie import Movie
app = Flask(__name__)
with app.app_context():
    data = Movie.get_all_mongodb("films")
    a = jsonify([s.to_dict() for s in data])
    print(a.json)
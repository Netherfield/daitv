from flask import render_template

def render_all_view(movies):
    return render_template("__ALL__.html", movies=movies)
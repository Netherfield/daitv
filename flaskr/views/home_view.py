from flask import render_template
def render_home_view(films):
    return render_template("__HOME__.html", films=films)
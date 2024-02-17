from flask import render_template

def render_test_view(movie):
    return render_template("__TEST__.html", movie=movie)
from flask import render_template, redirect, url_for, Blueprint, request

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("index.html")

@my_view.route("/leviathan")
def leviathan():
    return render_template("leviathan.html")

@my_view.route("/play_now")
def play_now():
    return render_template("play_now.html")

@my_view.route("/info")
def info():
    return render_template("info.html")

@my_view.route("/classes")
def classes():
    return render_template("classes.html")

@my_view.route("/races")
def races():
    return render_template("races.html")

@my_view.route("/planets")
def planets():
    return render_template("planets.html")

@my_view.route("/facebook")
def facebook():
    return render_template("facebook.html")

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/homepage")
def homeb_redirect():
    return redirect(url_for("my_view.home"))

# -------------------------

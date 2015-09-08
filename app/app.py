# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, session, redirect, url_for
import shelve
import atexit
import recommendations
import tmdbsimple as tmdb

app = Flask(__name__)

db = shelve.open("./db/movielens_100k.db")


def get_data(user):
    if user in db:
        return {"user": user, "movies": db[user]}
    return {"user": user}


def set_data(user, movie, score):
    db.setdefault(user, {})
    db_user = db[user]
    db_user[movie] = score
    db[user] = db_user


@app.route("/")
def index():
    if session.get("username", None):
        return get_movies()
    else:
        return render_template("index.html")


@app.route("/get-movies", methods=["GET", "POST"])
def get_movies():
    data = {}
    if session.get("username", None):
        data = get_data(session["username"])
    elif request.method == "POST":
        username = str(request.form["username"])
        session["username"] = username
        data = get_data(username)
    return render_template("movies.html", data=data)


@app.route("/rec", methods=["POST"])
def rec():
    if request.method == 'POST':
        username = str(request.form["username"])
        recs = recommendations.get_recommendations(db, username)[:30]
        return render_template("movies.html", data=recs, rec=True)


@app.route("/add-score", methods=["POST"])
def add_score():
    username = request.form["username"].encode('utf-8')
    moviename = request.form["moviename"].encode('utf-8')
    if moviename:
        moviescore = float(request.form["moviescore"])
        search = tmdb.Search()
        response = search.movie(query=moviename.split("(")[0])
        if response['results']:
            set_data(username, moviename, moviescore)
    return render_template("redirect-user.html", data=username)


def exit_handler():
    db.close()

atexit.register(exit_handler)

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.debug = True

    tmdb.API_KEY = "f5fb780312d3eef86ddf28bf083c9887"
    app.run()

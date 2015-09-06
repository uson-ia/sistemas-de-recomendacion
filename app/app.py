from flask import Flask, render_template, request, redirect, url_for
import shelve
import atexit

app = Flask(__name__)

db = shelve.open("./db/movielens_100k.db")

def get_data(user):
    print db.cache
    db.sync()
    if user in db:
        return {"user" : user, "movies" : db[user]}
    return {"user" : user}

def set_data(user, movie, score):
    db.setdefault(user, {})
    db_user = db[user]
    db_user[movie] = score
    db[user] = db_user
    print db[user]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-movies", methods=["GET", "POST"])
def get_movies():
    data = {}
    if request.method == "POST":
        data = get_data(request.form["username"])
    return render_template("movies.html", data=data)

@app.route("/add-score", methods=["POST"])
def add_score():
    username = str(request.form["username"])
    moviename = str(request.form["moviename"])
    moviescore = float(request.form["moviescore"])
    set_data(username, moviename, moviescore)
    return redirect(url_for("get_movies"))

def exit_handler():
    db.close()

atexit.register(exit_handler)

if __name__ == '__main__':
    app.run(debug=True)

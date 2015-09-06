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


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-movies", methods=["GET", "POST"])
def get_movies():
    data = {}
    if request.method == "POST":
        data = get_data(request.form["username"])
    return render_template("movies.html", data=data)


def exit_handler():
    db.close()

atexit.register(exit_handler)

if __name__ == '__main__':
    app.run(debug=True)

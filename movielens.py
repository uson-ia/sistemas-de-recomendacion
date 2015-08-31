# encoding: utf-8

import csv
import zipfile

def load_100k(directory='datasets', filename='ml-100k', dataset_url="http://files.grouplens.org/datasets/movielens/ml-100k.zip"):
    directory_path = directory+'/'
    zip_filename = filename+".zip"
    movies_filename = filename+'/u.item'
    ratings_filename = filename+'/u.data'

    with zipfile.ZipFile(directory_path+zip_filename, "r") as z:
        # Cargar diccionario de peliculas {movieID : title}
        movies = {}
        with z.open(movies_filename) as movies_file:
            for line in movies_file:
                (id, title) = line.split('|')[0:2]
                movies[id] = title

        # Cargar diccionario de preferencias por usuario {user: {movie_id: rating}}
        prefs = {}
        with z.open(ratings_filename) as ratings_file:
            for line in ratings_file:
                (user, movie_id, rating, ts) = line.split('\t')
                prefs.setdefault(user, {})
                prefs[user][movies[movie_id]] = float(rating)
    return prefs

def load_20m(directory='datasets', filename='ml-20m', dataset_url="http://files.grouplens.org/datasets/movielens/20m.zip"):
    directory_path = directory+'/'
    zip_filename = filename+".zip"
    movies_filename = filename+'/movies.csv'
    ratings_filename = filename+'/ratings.csv'

    with zipfile.ZipFile(directory_path+zip_filename, "r") as z:
        # Cargar diccionario de peliculas {movieID : title}
        movies = {}
        with z.open(movies_filename) as movies_file:
            reader = csv.DictReader(movies_file)
            for row in reader:
                movies[row['movieId']] = row['title']

        # Cargar diccionario de preferencias por usuario {userID: {movieId: rating}}
        prefs = {}
        with z.open(ratings_filename) as ratings_file:
            reader = csv.DictReader(ratings_file)
            for row in reader:
                prefs.setdefault(row['userId'], {})
                prefs[row['userId']][row['movieId']] = float(row['rating'])
        return prefs
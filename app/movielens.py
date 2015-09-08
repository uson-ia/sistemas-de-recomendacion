# encoding: utf-8

from downloader import get_file
import csv
import os
import zipfile

def _file_exists(directory, filename):
    """ Returns a bool representing if a file is present in the given directory """
    return os.path.exists(directory) and os.path.isfile(directory+"/"+filename)

def _assert_dataset_existence(directory, dataset_filename, dataset_url):
    """ Check if a dataset exists inside the given directory. If it doesn't, offer the user to download it. Returns a bool """
    if _file_exists(directory, dataset_filename):
        return True

    print "Parece que no tienes el dataset adecuado ("+dataset_filename+") en la carpeta '"+directory+"'"
    should_download = (raw_input('¿Deseas descargar el dataset? [si|no]: ')).lower() == "si"
    if not should_download:
        print "No se descargara el archivo."
        return False

    print "Comenzará la descarga. Para cancelar, presiona control+c."

    downloaded_filename = get_file(directory, dataset_url, dataset_filename)
    return downloaded_filename != ""

def _load_from_u_files(directory, filename, dataset_url):
    """ Load preference dictionary from u.item and u.data files inside a zip file (I think only 100k file uses this format) """
    directory_path = directory+'/'
    zip_filename = filename+".zip"
    movies_filename = filename+'/u.item'
    ratings_filename = filename+'/u.data'

    # Checar si se tienen los datos
    dataset_exists = _assert_dataset_existence(directory, zip_filename, dataset_url)
    if not dataset_exists:
        return None

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

def _load_from_csv(directory, filename, dataset_url):
    """ Load preference dictionary from movies.csv and ratings.csv files inside a zip file """
    directory_path = directory+'/'
    zip_filename = filename+".zip"
    movies_filename = filename+'/movies.csv'
    ratings_filename = filename+'/ratings.csv'

    # Checar si se tienen los datos
    dataset_exists = _assert_dataset_existence(directory, zip_filename, dataset_url)
    if not dataset_exists:
        return None

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


def load_100k():
    return _load_from_u_files('datasets', 'ml-100k', "http://files.grouplens.org/datasets/movielens/ml-100k.zip")

def load_20m():
    return _load_from_csv('datasets', 'ml-20m', 'http://files.grouplens.org/datasets/movielens/ml-20m.zip')

def load_latest():
    return _load_from_csv('datasets', 'ml-latest', 'http://files.grouplens.org/datasets/movielens/ml-latest.zip')
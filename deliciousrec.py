# -*- coding: utf-8 -*-

__author__ = 'JuanManuel'

from pydelicious import get_popular, get_userposts, get_urlposts
import random
import recommendations
import time

"""
Funcion: initializeUserDict(tag, count = 5)
Descripcion: Esta funcion recibe una consulta la cual se revisa en los ultimos posts que contienen dicha consulta de delicious 
			 despues revisa cada post y obtiene los usuarios que postearon dicho post se obtiene el nombre de los usuarios
			 y se ponen en un diccionario.
Parametros:
tag   - Es una consulta.
count - Es el numero de usuarios que se tienen en el diccionario.
Valor de retorno: Un diccionario con usuarios de los ultimos posts.
"""
def initializeUserDict(tag, count = 5):
    user_dict = {}

    # Obtener el top de los post populares
    for p1 in get_popular(tag = tag)[0:count]:
        # Encontrar a todos los usuarios que postearon esto
        for p2 in get_urlposts(p1['url']):
            user = p2['user']
            user_dict[user] = {}
    print user_dict
    return user_dict

"""
Funcion: fillItems(user_dict)
Descripcion: Esta funcion recibe un diccionario que contiene usuarios y un espacio en blanco al ejecutar la funcion
			 se buscan los posts del usuario que haya realizado una consulta dada y guarda los enlaces a dichos posts
			 en el espacio en blanco con el valor de uno si no se encuentran posts relacionados con la consulta dada 
			 el valor en el espacio es cero.
Parametros:
user_dict - Es un diccionario que contiene usuarios y un espacio en blanco por cada usuario en donde se ponen los enlaces a los posts.
Valor de retorno: None
"""
def fillItems(user_dict):
    all_items = {}

    # Encuentra links posteados por otros usuarios
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user)
                break
            except:
                print "Error de usuario " + user + " reintentando"
                time.sleep(4)

        for post in posts:
            url = post['url']
            user_dict[user][url] = 1.0
            all_items[url] = 1

    # Se rellenan los items restantes con 0
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0.0
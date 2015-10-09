# -*- coding: utf-8 -*-

__author__ = 'JuanManuel'

from math import sqrt

# Un diccionario de los críticos de cine y sus calificaciones de un pequeño
# conjunto de películas

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# Devuelve una puntuación de similitud basada en la distancia por persona y persona

def sim_distance(prefs, person1, person2):
	# Obtener la lista de shared_items
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	# Si no tienen calificaciones en común, devolver 0
	if len(si) == 0:
		return 0

	# Suma los cuadrados de todas las diferencias
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
					 for item in prefs[person1] if item in prefs[person2]])

	return 1.0 / (1.0 + sum_of_squares)


	
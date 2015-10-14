# -*- coding: utf-8 -*-

__author__ = 'JuanManuel'

from pydelicious import get_popular, get_userposts, get_urlposts

def initializeUserDict(tag, count = 5):
	user_dict = {}

	# Obtener el top de los post populares
	for p1 in get_popular(tag = tag)[0:count]:
		# Encontrar a todos los usuarios que postearon esto
		for p2 in get_urlposts(p1['href']):
			user = p2['user']
			user_dict[user] = {}

	return user_dict
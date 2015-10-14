# -*- coding: utf-8 -*-

__author__ = 'JuanManuel'

from pydelicious import get_popular, get_userposts, get_urlposts
import random
import recommendations
import time

def initializeUserDict(tag, count = 5):
	user_dict = {}

	# Obtener el top de los post populares
	for p1 in get_popular(tag = tag)[0:count]:
		# Encontrar a todos los usuarios que postearon esto
		for p2 in get_urlposts(p1['href']):
			user = p2['user']
			user_dict[user] = {}

	return user_dict

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
			url = post['href']
			user_dict[user][url] = 1.0
			all_items[url] = 1

	# Se rellenan los items restantes con 0
	for ratings in user_dict.values():
		for item in all_items:
			if item not in ratings:
				ratings[item] = 0.0
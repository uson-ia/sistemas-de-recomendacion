from pydelicious import  get_popular, get_userposts, get_urlposts


def initializeUserDict(tag, count = 5):
 	user_dict = {}

 	# obtienes el top de los posts mas populares
 	for p1 in get_popular(tag = tag)[0:count]:
 		# encuentra a todos los usuarios que postearon esto
 		for p2 in get_urlposts(p1['url']):
 			user = p2['user']
 			user_dict[user] = {}
 	return user_dict

def fillItems(user_dict):
	all_items = {}
 	# encontramos links posteados por todos los usuarios
 	for user in user_dict:
 		for i in range(3):
 			try:
 				posts = get_userposts(user)
 				break
 			except:
 				print "Failed user " + user + ", retrying"
 				time.sleep(4)
 		for post in posts:
 			url = post['url']
 			user_dict[user][url] = 1.0
 			all_items[url] = 1
 
 	# rellenamos los valores desconocidos con 0
 	for ratings in user_dict.values( ):
 		for item in all_items:
 			if item not in ratings:
 				ratings[item] = 0.0


# def main():


# 	delusers=initializeUserDict('programming')
# 	delusers ['tsegaran']={}
# 	fillItems(delusers)
# 	user=delusers.keys( )[random.randint(0,len(delusers)-1)]
# 	print user
# 	print recommendations.getRecommendations(delusers,user)[0:10]

# if __name__ == "__main__":
#     main()
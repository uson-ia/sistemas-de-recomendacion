from pydelicious import get_popular, get_userposts, get_urlposts
import time


def initialize_user_dict(tag, count=100):
    user_dict = {}
    # obtenemos el top de posts populares
    for p1 in get_popular(tag=tag)[0:count]:
        # Encontramos usuarios que postearon esto
        for p2 in get_urlposts(p1['url']):
            user = p2['user']
            user_dict[user] = {}
    return user_dict


def fill_itmes(user_dict):
    all_itmes = {}
    # Encontramos links posteados por todos los usuarios
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user())
                break
            except:
                print "Failed user ", user, " retrying"
                time.sleep(4)
        for post in posts:
            url = post['url']
            user_dict[user][url] = 1.0
            all_itmes[ur] = 1

    for ratings in user_dict.values():
        for item in all_itmes:
            if item not in ratings:
                ratings[item] = 0.0

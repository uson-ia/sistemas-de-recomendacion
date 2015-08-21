from math import sqrt

# Diccionario de diccionarios (nested dictionary), con puntuacion que gente
# le ha dado a ciertas peliculas
critics = {'Tony Stark': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                          'Just My Luck': 3.0, 'Superman Returns': 3.5,
                          'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
           'Emma Watson': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                           'Just My Luck': 1.5, 'Superman Returns': 5.0,
                           'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
           'Dijkstra': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                        'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Pavlovich': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                                 'The Night Listener': 4.5, 'Superman Returns':
                                 4.0, 'You, Me and Dupree': 2.5},
           'Christian Ruink': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                               'Just My Luck': 2.0, 'Superman Returns': 3.0,
                               'The Night Listener': 3.0, 'You, Me and Dupree':
                               2.0},
           'Eduardo Yeomans': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                               'The Night Listener': 3.0, 'Superman Returns':
                               5.0, 'You, Me and Dupree': 3.5},
           'El Robbie': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
                         'Superman Returns': 4.0}}


def get_shared_items(prefs, person_1, person_2):
    # Obtenemos la lista de items compartidos
    shared_items = {}
    for item in prefs[person_1]:
        if item in prefs[person_2]:
            shared_items[item] = 1

    return shared_items


def sim_distance(prefs, person_1, person_2):
    """
    Esta funcion devuelve similaridad basada en distancia, para
    la persona 1 y la persona 2.
    """

    shared_items = get_shared_items(prefs, person_1, person_2)
    # Si no tienen nada compartido, devolvemos 0
    if len(shared_items) == 0:
        return 0

    # Sumamos el cuadrado de todas las diferencias (cada distancia)
    sum_of_squares = sum([pow(prefs[person_1][item] - prefs[person_2][item],
                         2) for item in prefs[person_1]
                         if item in prefs[person_2]])
    return 1/(1 + sum_of_squares)


def sim_pearson(prefs, p1, p2):
    """
    Esta funcion devuelve la similaridad entre las
    dos personas con "score de similaridad de Pearson"
    """
    # Obtenemos la lista de items que tienen en comun
    shared_items = get_shared_items(prefs, p1, p2)

    # Obtenemos el numero de elementos compartidos
    n = len(shared_items)

    # Si no tienen nada en comun devolvemos 0
    if n == 0:
        return 0

    # Suma de las preferencias de cada uno (las comunes)
    sum_1 = sum([prefs[p1][item] for item in shared_items])
    sum_2 = sum([prefs[p2][item] for item in shared_items])

    # Ahora la suma de los cuadrados
    sum1_sqrt = sum([pow(prefs[p1][item], 2) for item in shared_items])
    sum2_sqrt = sum([pow(prefs[p2][item], 2) for item in shared_items])

    # Suma de los productos de cada preferencia en comun
    product_sum = sum([prefs[p1][item]*prefs[p2][item]
                      for item in shared_items])

    # Calculamos el score de Pearson
    num = product_sum - (sum_1*sum_2 / n)
    den = sqrt((sum1_sqrt - pow(sum_1, 2)/n)*(sum2_sqrt - pow(sum_2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r

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


def sim_distance(prefs, person_1, person_2):
    """
    Esta funcion devuelve similaridad basada en distancia, para
    la persona 1 y la persona 2.
    """

    # Obtenemos la lista de items compartidos
    shared_items = {}
    for item in prefs[person_1]:
        if item in prefs[person_2]:
            shared_items[item] = 1

    # Si no tienen nada compartido, devolvemos 0
    if len(shared_items) == 0:
        return 0

    # Sumamos el cuadrado de todas las diferencias (cada distancia)
    sum_of_squares = sum([pow(prefs[person_1][item] - prefs[person_2][item],
                         2) for item in prefs[person_1] if item in prefs[person_2]])
    return 1/(1 + sum_of_squares)

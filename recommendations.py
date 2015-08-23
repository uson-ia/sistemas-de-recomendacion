from math import sqrt


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


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    """
    Esta funcion calcula la similaridad que tiene una persona
    con todas las demas (en prefs) y devuelve una lista con
    los puntajes de manera descendete.
    """
    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]

    scores.sort()
    scores.reverse()
    return scores[:n]


def get_recommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    sim_sums = {}
    for other in prefs:
        # No me comparo conmigo mismo
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # Ignoramos el score de 0 o menor
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Solo puntuamos peliculas que no haya visto aun
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similaridad * score
                # setdefault eso como 'get' pero si no lo encuentra lo anade
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim
                # suma de similaridades
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    # Creamos la lista normalizada
    rankings = [(total / sim_sums[item], item)
                for item, total in totals.items()]
    # Regresamos la lista con cada par de pelicula y su score
    rankings.sort()
    rankings.reverse()
    return rankings


def transform_prefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Volteamos item y persona
            result[item][person] = prefs[person][item]
    return result


def calculate_similar_items(prefs, n=10):
    """
    Esta funcion calcula la similaridad  que tiene cada item
    con los demas (invierte el diccionario de criticas) usando
    top_matches.
    """
    result = {}
    item_prefs = transform_prefs(prefs)
    c = 0
    for item in item_prefs:
        # Mostramos el status (para cantidad grande de items)
        c += 1
        if c % 100 == 0:
            print c, " / ", len(item_prefs)
        scores = top_matches(item_prefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result


def get_recommended_items(prefs, item_match, user):
    user_ratings = prefs[user]
    scores = {}
    total_sim = {}

    # Recorremos los items puntuados por el usuario
    for (item, rating) in user_ratings.items():

        # Recorremos los itemos similares a este
        for (similarity, item2) in item_match[item]:

            # Ignoramos si el usuario ya ha puntuado este itemo
            if item2 in user_ratings:
                continue

            scores.setdefault(item2, 0)
            scores[item2] += similarity*rating

            # Suma de todas las similaridades
            total_sim.setdefault(item2, 0)
            total_sim[item2] += similarity

    # Dividimos cada puntaje total entre la ponderacion total para
    # obtener el promedio
    rankings = [(score / total_sim[item], item)
                for item, score in scores.items()]

    rankings.sort()
    rankings.reverse()
    return rankings

# -*- coding: utf-8 -*-

__author__ = 'JuanManuel'

from math import sqrt
import pydelicious

# Un diccionario de críticos del cine y sus calificaciones de un pequeño
# conjunto de películas.

critics = {
    "Lisa Rose" : 
    {
        "Lady in the Water"  : 2.5,
        "Snakes on a Plane"  : 3.5,
        "Just My Luck"       : 3.0,
        "Superman Returns"   : 3.5,
        "You, Me and Dupree" : 2.5,
        "The Night Listener" : 3.0
    },
    "Gene Seymour" : 
    {
        "Lady in the Water"  : 3.0,
        "Snakes on a Plane"  : 3.5,
        "Just My Luck"       : 1.5,
        "Superman Returns"   : 5.0,
        "The Night Listener" : 3.0,
        "You, Me and Dupree" : 3.5
    },
    "Michael Phillips" : 
    {
        "Lady in the Water"  : 2.5,
        "Snakes on a Plane"  : 3.0,
        "Superman Returns"   : 3.5,
        "The Night Listener" : 4.0
    },
    "Claudia Puig" : 
    {
        "You, Me and Dupree" : 2.5,
        "Snakes on a Plane"  : 3.5,
        "Just My Luck"       : 3.0,
        "Superman Returns"   : 4.0,
        "The Night Listener" : 4.5
    },
    "Mick LaSalle" : 
    {
        "Lady in the Water"  : 3.0,
        "Snakes on a Plane"  : 4.0,
        "Just My Luck"       : 2.0,
        "Superman Returns"   : 3.0,
        "The Night Listener" : 3.0,
        "You, Me and Dupree" : 2.0
    },
    "Jack Matthews" : 
    {
        "Lady in the Water"  : 3.0,
        "Snakes on a Plane"  : 4.0,
        "You, Me and Dupree" : 3.5,
        "Superman Returns"   : 5.0,
        "The Night Listener" : 3.0
    },
    "Toby" : 
    {
        "Snakes on a Plane"  : 4.5,
        "You, Me and Dupree" : 1.0,
        "Superman Returns"   : 4.0
    },
    "Juan Manuel" : 
    {
        "Snakes on a Plane"  : 4.5,
        "You, Me and Dupree" : 1.0,
        "Superman Returns"   : 4.0
    }
}

"""
Funcion: get_shared_items(prefs, person1, person2)
Descripcion: Se obtiene la lista de peliculas en comun entre ambas personas.
Parametros:
prefs   - Diccionario que contiene el nombre de criticos de peliculas, peliculas y su calificacion.
person1 - Elemento del diccionario el cual es un critico de peliculas y contiene peliculas ademas de su calificacion.
person2 - Elemento del diccionario el cual es un critico de peliculas y contiene peliculas ademas de su calificacion.
Valor de retorno: Devuelve la lista de peliculas en comun entre ambas personas.
"""
def get_shared_items(prefs, person1, person2):
    shared_items = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            shared_items[item] = 1

    return shared_items

"""
Funcion: sim_distance(prefs, person1, person2)
Descripcion: Se obtiene una puntuación de similitud basada en la distancia de person1 y person2.
Parametros:
prefs   - Diccionario que contiene el nombre de criticos de peliculas, peliculas y su calificacion.
person1 - Elemento del diccionario el cual es un critico de peliculas y contiene peliculas ademas de su calificacion.
person2 - Elemento del diccionario el cual es un critico de peliculas y contiene peliculas ademas de su calificacion.
Valor de retorno: Devuelve una puntuación de similitud basada en la distancia de person1 y person2.
"""
def sim_distance(prefs, person1, person2):
    # Se obtiene la lista de shared_items
    shared_items = get_shared_items(prefs, person1, person2)

    # Si no tienen items en común, se devuelve 0
    if len(shared_items) == 0:
        return 0

    # Sumamos el cuadrado de todas las diferencias (cada distancia)
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1.0 / (1.0 + sum_of_squares)

# Devuelve el coeficiente de correlación de Pearson para person1 y person2.

def sim_pearson(prefs, person1, person2):
    # Obtener la lista de shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # Encuentra el número de elementos
    n = len(si)

    # Si no tienen calificaciones en común, devolver 0
    if n == 0:
        return 0

    # Suma todas las preferencias
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    # Suma los cuadrados
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])

    # Suma los productos
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

    # Calcular la puntuación de Pearson
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num/den

    return r

# Devuelve los mejores partidos de la persona del diccionario prefs.
# El número de resultados y la función de similitud son parametros opcionales.

def topMatches(prefs, person, n=5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    # Ordena la lista para que los puntajes más altos aparezcan en la parte superior
    scores.sort()
    scores.reverse()

    return scores[0:n]

# Obtiene recomendaciones para una persona mediante el uso de una media ponderada
# Del ranking de todos los demás usuarios.

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # No me comparo a mí mismo
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # Ignorar las puntuaciones de cero o menor
        if sim <= 0:
            continue

        for item in prefs[other]:
            # Sólo anotar películas que no he visto todavía
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similitud * Puntuación
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Suma de similitudes
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Crear la lista normalizada
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Devuelve la lista ordenada
    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Intercambiar item y persona
            result[item][person] = prefs[person][item]

    return result

def calculateSimilarItems(prefs, n = 10):
    # Crear un diccionario de items que muestre otros items
    # similares
    result = {}

    # Invertir la matriz de preferencia para que sea item-centric
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Actualizaciones de estado para grandes conjuntos de datos
        c += 1
        if c % 100 == 0:
            print "%d / %d" % (c, len(itemPrefs))
        # Encuentra los items más similares a este
        scores = topMatches(itemPrefs, item, n = n, similarity = sim_distance)
        result[item] = scores

    return result

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}

    # Se cicla por los items calificados por este usuario
    for (item, rating) in userRatings.items():

        # Se cicla por los items parecidos a este
        for (similarity, item2) in itemMatch[item]:
            
            # Ignora si este usuario ya califico este item
            if item2 in userRatings:
                continue

            # Suma ponderada de las similitudes //REVISA BIEN ESTO
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            # Suma de todas las similitudes
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity

    # Dividir cada calificacion total por el total de la suma ponderada para obtener
    # un promedio
    rankings = [(score / totalSim[item], item) for item, score in scores.items()]

    # Regresa las clasificaciones de la mas alta a la mas baja
    rankings.sort()
    rankings.reverse()

    return rankings 

def loadMovieLens(path='/C:\Users\JuanManuel\PycharmProjects\SR'):

    # Obtener títulos de películas
    movies = {}
    for line in open(path + '\u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    # Cargar datos
    prefs = {}
    for line in open(path + '\u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)

    return prefs

def main():

    print "Ejemplos que aparecen en el proyecto principal"

    """
    print "Ejemplo 1"
    from recommendations import critics
    critics['Lisa Rose']['Lady in the Water']
    critics['Toby']['Snakes on a Plane']=4.5
    critics['Toby']
    """

    """
    print "Ejemplo 2"
    from math import sqrt
    sqrt(pow(5-4,2)+pow(4-1,2))
    1/(1+sqrt(pow(5-4,2)+pow(4-1,2)))
    """

    """
    print "Ejemplo 3"
    import recommendations
    recommendations.sim_distance(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
    """

if __name__ == "__main__":
    main()
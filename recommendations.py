
from math import sqrt
#       Sistema de recomendacion de Collective Intelligence (capitulo 2)

# Un diccionario de los criticos de cine y sus clasificaciones

#	de un pequeno conjunto de peliculas, algo parecido a una peuqena 
#	base de datos

# Todos los balores en este ejemplo se guardan en un diccionario donde a las
#   personas guardan un conjunto de peliculas que les gusto y ranking que va de 
#   1 a 5 segun como les ha gustado la pelicual, es este caso se usaron pelicuas
#   y este tipo de valor numerico asignado, pero pueden ser otros ejemplos siempre
#   y cuando tengan un peso o valor numerico

critics={
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 
        'Superman Returns': 3.5, 
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },

    'Gene Seymour': {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 
        'Superman Returns': 5.0, 
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },

    'Michael Phillips': {
        'Lady in the Water': 2.5, 
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 
        'The Night Listener': 4.0
    },

    'Claudia Puig': {
        'Snakes on a Plane': 3.5, 
        'Just My Luck': 3.0,
        'The Night Listener': 4.5, 
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5
    },

    'Mick LaSalle': {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 
        'Superman Returns': 3.0, 
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },

    'Jack Matthews': {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0, 
        'Superman Returns': 5.0, 
        'You, Me and Dupree': 3.5},
    'Toby': {
        'Snakes on a Plane':4.5,
        'You, Me and Dupree':1.0,
        'Superman Returns':4.0
    }
}


# probando la pquenia base de datos
#lista = critics.keys()
#print lista #['Toby']
#print critics

#esta formula calcula la distancia, que sera mas peuqenia para personas que son 
#mas similares, sin embargo nesesictamos balores mas grandes, asi que agregaremos
# un uno a la funcion
print "simples ejemplos"
print sqrt(pow(5-4,2)+pow(4-1,2))
# 3.16227766017

#esta nueva funcion siempre regresa un valor entre cero y uno
#donde uno sicnifica que dos personas stiene preferencias identicas
print 1/(1+sqrt(pow(5-4,2)+pow(4-1,2)))
# 0.240253073352

#entonces bamos a crear una funcion para calcular las semejanzas
#tomado del libro collective Intelligence

#regresa  una puntuacion de similitud basada en la distancia de 
#person1 y peson2
def sim_distance(prefs,person1,person2):
    #obtiene la lista de elementos compartidos
    si ={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    #si ellos no tienen un raiting en comun regresa cero
    if len(si)==0:
        return 0

    #sumando la suma de todas las diferencias de lso cuadrados
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sum_of_squares)


#es un ejemplo cuando usamos la funcion para saber la distancia de dos personas

print "el resultado con la funcion sim_distance"
print sim_distance(critics,'Lisa Rose','Gene Seymour')
# 0.1481481481488
print sim_distance(critics,'Lisa Rose','Toby')
# 0.2222222222222


#regresa el coeficiente de correlacion pearson para p1 y p2
def sim_pearson(prefs,p1,p2):
    #obtiene la lista de objetos mutuos
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    #encuentra el numero de elementos
    n=len(si)

    #si no tiene un reiting en comun regresa correlacion
    if n==0:
        return 0

    #sume todas las preferencias
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    #suma los cuadrados
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    #suma el producto
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #calucla la puntuacion de pearson
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: 
        return 0

    r=num/den
    return r

#haciendo pruebas con la funcion sim_pearson
print "la impresion con al funcion sim_pearson"
print sim_pearson(critics,'Lisa Rose','Gene Seymour')
print sim_pearson(critics,'Lisa Rose','Toby')
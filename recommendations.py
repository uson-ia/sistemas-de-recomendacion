# Moises Salas
# Collective intelligence chapter 2

from math import sqrt
import pydelicious

# un diccionario de criticos de peliculas con sus ratings de unas cuantas peliculas

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
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

# regresa una distancia de similitud entre una puntuacion de una persona a otra
def sim_distance(prefs,person1,person2):
	# se obtiene una lista de los items que tienen ambos
	si={}
	for item in prefs[person1]:
 		if item in prefs[person2]:
 			si[item]=1
 	
 	# si no hay se regresa 0
 	if len(si)==0: return 0
 	
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
 	
 	return 1/(1+sum_of_squares)

# regresa el pearson score
def sim_pearson(prefs,p1,p2):
 	# se obtiene una lista de objetos que ambos calificaron
	si={}
 	for item in prefs[p1]:
 		if item in prefs[p2]: si[item]=1
 
 	# se ve el numero de elementos
 	n=len(si)
 
 	# si no hay se devuelve 0
 	if n==0: return 0
 
 	sum1=sum([prefs[p1][it] for it in si])
 	sum2=sum([prefs[p2][it] for it in si])
 
 	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
 	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
 
 	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
 
 	# se calcula el Pearson score
 	num=pSum-(sum1*sum2/n)
 	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
 	if den==0: return 0
 
 	r=num/den
 
 	return r

# regresa la mejor opcion de persona del diccionario de pref
def topMatches(prefs,person,n=5,similarity=sim_pearson):
 	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
 	
 	# se acomoda la lista para que aparezcan primero las puntuaciones mas altas
 	scores.sort( )
 	scores.reverse( )
 	return scores[0:n]

# se obtienen recomendaciones para una persona utilizando un promedio del ranking de los otros usuarios
def getRecommendations(prefs,person,similarity=sim_pearson):
 	totals={}
 	simSums={}
 	for other in prefs:
 		# no compararse con uno mismo
 		if other==person: continue
 		sim=similarity(prefs,person,other)
 
 		# se ignoran los scores de 0 o menor
 		if sim<=0: continue
 		for item in prefs[other]:
 			
 			# solo peliculas que no he visto
 			if item not in prefs[person] or prefs[person][item]==0:
 				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				simSums.setdefault(item,0)
				simSums[item]+=sim
 
 	# se crea una lista normalizada
 	rankings=[(total/simSums[item],item) for item,total in totals.items( )]
 	
 	# se regresa la lista orrdenada
 	rankings.sort( )
 	rankings.reverse( )
 	
 	return rankings

def transformPrefs(prefs):
 	result={}
 	for person in prefs:
 		for item in prefs[person]:
 			result.setdefault(item,{})
  			result[item][person]=prefs[person][item]
 	return result

def calculateSimilarItems(prefs,n=10):
 	# se crea un diccionario de items para mostrar que otros items son similares
 	result={}
 
 	itemPrefs=transformPrefs(prefs)
 	c=0
 	for item in itemPrefs:
 		c+=1
 		if c%100==0: print "%d / %d" % (c,len(itemPrefs))
 		# buscamos los items mas similares al actual
 		scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
 		result[item]=scores
 	return result

def getRecommendedItems(prefs,itemMatch,user):
 	userRatings=prefs[user]
 	scores={}
 	totalSim={}
 
 	# vemos a items ya calificados por el usuario
 	for (item,rating) in userRatings.items( ):
 		
 		# vemos items similares a el actual
 		for (similarity,item2) in itemMatch[item]:
 
 			# ignorar si el usuario ya le dio calificacion a esto
 			if item2 in userRatings: continue
 
 			# suma de ratings multiplicado por similitud
 			scores.setdefault(item2,0)
 			scores[item2]+=similarity*rating
 
 			# suma de todas las similitudes
 			totalSim.setdefault(item2,0)
 			totalSim[item2]+=similarity

 	# divide cada puntuacion total por el total para obtener un promedio
 	rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
 
 	# regresa ranking de mayor a menor
 	rankings.sort( )
 	rankings.reverse( )
 	return rankings

def loadMovieLens(path='C:\codes\GitHub\sistemas-de-recomendacion'):
 	# obtiene los titulos de las peliculas
 	movies={}
 	for line in open(path+'/u.item'):
 		(id,title)=line.split('|')[0:2]
 		movies[id]=title
 
 	# carga la informacion
 	prefs={}
 	for line in open(path+'/u.data'):
 		(user,movieid,rating,ts)=line.split('\t')
 		prefs.setdefault(user,{})
 		prefs[user][movies[movieid]]=float(rating)
 	return prefs


def main():

	print 'recommendations'

	# pruebas que hice del documento

	# print sim_pearson(critics,'Lisa Rose','Gene Seymour')
	# print topMatches(critics,'Toby',n=3)
	# print getRecommendations(critics,'Toby')
	# movies = transformPrefs(critics)
 # 	print topMatches(movies,'Superman Returns')
 # 	print getRecommendations(movies,'Just My Luck')
 	# print pydelicious.get_popular(tag = 'programmin')
 # 	itemsim = calculateSimilarItems(critics)
 # 	# print itemsim
	# # print getRecommendedItems(critics,itemsim,'Toby')
	# prefs = loadMovieLens()
	# # print prefs['87']
	# # print getRecommendations(prefs,'87')[0:30]
	# itemsim = calculateSimilarItems(prefs,n=50)
	# print itemsim
	# print getRecommendedItems(prefs,itemsim)[0:30]


if __name__ == "__main__":
    main()
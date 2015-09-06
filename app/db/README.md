# Base de datos

Aquí deberían estar las bases de datos del movielens.

Ahorita estoy haciendo las cosas utilizando Shelve (que es como una base de datos de diccionarios de Python).

Para el desarrollo de esta app, propongo utilizar la base de datos mas peque (la que es de 100k).

para tener estos datos como un shelve debemos escribir los siguientes comandos en la consola de python (ubicados en la raíz del repositorio).

```
In [1]: import movielens

In [2]: import shelve

In [3]: preferences = movielens.load_100k()

In [4]: db = shelve.open("./app/db/movielens_100k.db")

In [5]: for critic in preferences:
   ...:     for movie in preferences[critic]:
   ...:         score = preferences[critic][movie]
   ...:         db.setdefault(critic, {})
   ...:         db_critic = db[critic]
   ...:         db_critic[movie] = score
   ...:         db[critic] = db_critic

In [6]: db.close()
```

No se como se vean los archivos que genera el shelve, pero en mi linux me genera tres archivos: `movielens_100k.db.bak`, `movielens_100k.db.dat` y `movielens_100k.db.dir`.

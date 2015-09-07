Sistemas de recomendación
==========

En este repositorio se exploraran algunas técnicas usadas en el desarrollo de los sistemas de recomendación.
Los sistemas de recomendación son programas que filtran datos para encontrar aquellos más relevantes para el usuario.

## Cómo usar
#### 1. Elige el dataset con el que quieres trabajar.

A continuación están los datasets soportados hasta el momento y el código necesario para cargarlos a un diccionario de preferencias:

- **Sencillo - 100k**. Ideal para pruebas y algoritmos.
    [5 MB] - 100,000 ratings, 6000 usuarios, 4000 películas - http://files.grouplens.org/datasets/movielens/ml-100k.zip
    `preferences = movielens.load_100k()`

- **Jumbo - 20M**. Seguramente correrá bastante lento. Se puede usar para entrarle a rollos de optimización.
    [138 MB] - 20,000,000 ratings, 138,000 usuarios, 27,000 películas - http://files.grouplens.org/datasets/movielens/ml-20m.zip
    `preferences = movielens.load_20m()`

- **Jumbo con papas - 21M**. Dataset similar al anterior, pero es constantemente actualizado (i.e. seguira creciendo).
    [+144 MB] - 21,000,000 ratings, 230,000 usuarios, 30,000 películas - http://files.grouplens.org/datasets/movielens/ml-latest.zip
    `preferences = movielens.load_latest()`

Puedes hacer las llamadas a las funciones de arriba sin importar si descargaste o no el dataset (el sistema los descargará por ti).
Los datasets deben guardarse dentro de una carpeta con el nombre `datasets` dentro del proyecto
Si sólo quieres descargar los datos de prueba (sin cargarlos a un diccionario) puedes usar el siguiente comando:   `python -m get_dataset [dataset_url]`
Para checar estos y otros datasets puedes visitar http://grouplens.org/datasets/movielens/

#### 2. Siguiente paso.

Instrucciones. [pendiente]

## Siguientes Pasos
Los siguientes son puntos deseables en los que el proyecto podría mejorar. Si tienes tiempo de hackear alguno recibirás honor eterno:

- **Agregar items a esta lista**
- Agregar interfáz gráfica [DONE] (creo... atte Eduardo)
- Guardar resultados del entrenamiento (para no tener que calcular todo en cada corrida)
- Añadir autocompletado de las películas en MovieLens al input text de /get-movies
- Refinar el añadido de películas
  - a) Restringir a que solo se puedan calificar películas que ya están en MovieLens, o
  - b) Hacer una trácala para elegir strings semejantes como una misma película, como "El Rey León", "El Rey León (1994)" y "Rey León 1994" son strings diferentes pero hacen referencia a la misma película.
- .

### Acerca de la implementacion del sistemilla web
Para correr la aplicacion:
- Crear el entorno virtual dentro del repositorio:

    `virtualenv mientorno (con deactivate sales del entorno)`
- Activar el entorno:

    `source mientorno/bin/activate`
- Instalar las dependencias:

    `pip install -r requirements.txt`
- Correr el archivo `app.py`
- Recuerden.. si instalan otros plugins agreguenlos a la lista de
requeimientos:

    `pip freeze > requirements.txt`

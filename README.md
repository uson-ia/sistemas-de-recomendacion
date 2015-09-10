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
Si sólo quieres descargar los datos de prueba (sin cargarlos a un diccionario) puedes usar el siguiente comando:   `python -m downloader [dataset_url]` 
Para checar estos y otros datasets puedes visitar http://grouplens.org/datasets/movielens/

#### 2. Instalar dependencias la aplicación web

Ejecuta los siguientes comandos (en la raíz del proyecto)
- **Instalar `pip`**
  `pip` es un manejador de paquetes, lo cual nos va a permitir descargar e instalar dependencias de forma fácil
  Para información sobre como instalar pip visita el siguiente link https://pip.pypa.io/en/latest/installing.html 
   
- **Instalar `virtualenv`** 
 `virtualenv` es una herramienta para crear entornos isolados de Python (y así evitar colisiones entre dependencias de diferentes proyectos)
  Ya instalado pip podemos instalar virtualenv con el siguiente comando: 
  `pip install virtualenv` 
  
- **Crear un entorno virtual para el proyecto**
    `virtualenv ia-sisrec-env`

- **Activar el entorno**
    `source ia-sisrec-env/bin/activate`
    En caso de que te quieras salir del entorno, puedes correr el comando: `deactivate` 

- **Instalar las dependencias** 
    `pip install -r requirements.txt`
     Es probable que para que scipy se compile/instale bien requiera tener un compilador de fortran instalado y alcanzable desde el PATH.
     Una opción es el compilador de GNU `gfortran`. Puede que ya lo tengas si haz instalado `gcc`

#### 3. Correr la aplicación web
Cada vez que se
 - **Activar el entorno**
    Probablemente lo hiciste cuando instalaste las dependencias, pero esto se tiene que hacer cada vez que enciendas el servidor
    `source ia-sisrec-env/bin/activate`
 
- **Levantar el servidor**
    ```
    cd app
    python -m app
    ```

Listo! Si todo salió bien deberías de estar leyendo un mensaje diciéndote que te dirijas a http://127.0.0.1:5000/ - ahi está la aplicación
Si sucede algún error en estos pasos intenta actualizar las dependencias desde el archivo `requirements.txt` (ver sección anterior) o agregar un issue en el repositorio de GitHub

## Agregar dependencias
Si instalan otros plugins hay que agregarlos al archivo de dependencias para que los demas las puedan instalar también.
Una manera sencilla de hacerlo es ejecutando el siguiente comando:  
    ```
    pip freeze > requirements.txt
    ```


## Roadmap
Los siguientes son puntos deseables en los que el proyecto podría mejorar. Si tienes tiempo de hackear alguno recibirás honor eterno:

- **Agregar items a esta lista**
- ~~Agregar interfáz gráfica~~ DONE (creo... - atte @eduardoacye)
- Guardar resultados del entrenamiento (para no tener que calcular todo en cada corrida)
- Añadir autocompletado de las películas en MovieLens al input text de /get-movies
- Refinar el añadido de películas
  - a) Restringir a que solo se puedan calificar películas que ya están en MovieLens, o
  - b) Hacer una trácala para elegir strings semejantes como una misma película, como "El Rey León", "El Rey León (1994)" y "Rey León 1994" son strings diferentes pero hacen referencia a la misma película.
- .
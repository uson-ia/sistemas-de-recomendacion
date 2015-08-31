Sistemas de recomendación
==========

En este repositorio se exploraran algunas técnicas usadas en el desarrollo de los sistemas de recomendación.
Los sistemas de recomendación son programas que filtran datos para encontrar aquellos más relevantes para el usuario.

## Cómo usar
1. Elige el dataset con el que quieres trabajar. Abre una terminal en la carpeta del proyecto y ejecuta el comando adecuado.
    - **Sencillo - 100k**. Ideal para pruebas y algoritmos. 
        [5 MB] - 100,000 ratings, 6000 usuarios, 4000 películas
        `python -m get_dataset "http://files.grouplens.org/datasets/movielens/ml-100k.zip"`
        
    - **Doble wini - 1M**. Por si el anterior no te satisface.  
        [6 MB] - 1,000,000 ratings, 72,000 usuarios, 10,000 películas
        `python -m get_dataset "http://files.grouplens.org/datasets/movielens/ml-1m.zip"`
        
    - **Momia - 21M**. Seguramente correrá hyper lento (si es que corre). Se puede usar para entrarle a rollos de optimización. 
        [+144 MB] - 21,000,000 ratings, 230,000 usuarios, 30,000 películas
        `python -m get_dataset "http://files.grouplens.org/datasets/movielens/ml-latest.zip"`
    
    Para estos y más datasets puedes visitar http://grouplens.org/datasets/movielens/
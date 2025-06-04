# Proyecto: Representación TF-IDF de Noticias (RepB)

Este proyecto procesa las 10 noticias ubicadas en `../../tp3/2/output.json`, generando representaciones TF-IDF (RepB) bajo tres variantes:

1. **Texto original**
2. **Eliminando stop-words**
3. **Con bigramas**

Luego, deja una de las noticias como consulta y calcula el top 3 de noticias más similares usando la métrica de coseno. Para cada resultado, muestra el score y el texto de la noticia.

## Aclaración sobre la representación RepB (TF-IDF)

La representación utilizada para comparar las noticias es **TF-IDF**, denominada en la consigna como **RepB**. Esto se implementa mediante la clase `TfidfVectorizer` de la librería `scikit-learn`, que transforma cada noticia en un vector numérico ponderando cada término según su frecuencia en el documento y su rareza en el corpus. Esta es la representación vectorial utilizada para calcular la similitud entre noticias.

## Requisitos
- Python 3.11
- pipenv

## Instalación de dependencias

```
pipenv install
```

## Ejecución

```
pipenv run python main.py
```

## Estructura
- `main.py`: Script principal que realiza el procesamiento y muestra los resultados.

## Notas
- El archivo de noticias debe estar en la ruta `../../tp3/2/output.json` respecto a este proyecto.
- El script descarga automáticamente los stopwords de NLTK la primera vez que se ejecuta. 
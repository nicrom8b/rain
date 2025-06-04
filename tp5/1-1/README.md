# Proyecto: Representación TF-IDF de PDFs

Este proyecto procesa los archivos PDF ubicados en `../../tp1/pdf`, generando representaciones TF-IDF bajo tres variantes:

1. **Texto original**
2. **Eliminando stop-words**
3. **Con bigramas**

Luego, deja uno de los documentos como consulta y calcula el top 3 de documentos más similares usando la métrica de coseno. Para cada resultado, muestra el score y el texto del documento.

## Aclaración sobre la representación RepA (TF-IDF)

La representación utilizada para comparar los documentos es **TF-IDF**, denominada en la consigna como **RepA**. Esto se implementa mediante la clase `TfidfVectorizer` de la librería `scikit-learn`, que transforma cada documento en un vector numérico ponderando cada término según su frecuencia en el documento y su rareza en el corpus. Esta es la representación vectorial utilizada para calcular la similitud entre documentos.

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
- Los PDFs deben estar en la carpeta `../../tp1/pdf` respecto a este proyecto.
- El script descarga automáticamente los stopwords de NLTK la primera vez que se ejecuta. 
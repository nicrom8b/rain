# Scraper de Noticias de Economía - Infobae

Este proyecto implementa un scraper para recolectar información estructurada de las primeras 10 noticias de la sección [Infobae Economía](https://www.infobae.com/economia/), y realiza un análisis textual básico sobre el cuerpo de las noticias.

## Descripción

El script realiza las siguientes operaciones:

1. Recolecta las primeras 10 noticias de la sección economía de Infobae.
2. Para cada noticia, extrae:
   - Título
   - Resumen
   - Autor de la nota
   - Listado de imágenes (ubicación del archivo)
   - Cuerpo de la nota
3. Exporta los resultados en formato JSON para su análisis.
4. Realiza un análisis textual sencillo sobre el cuerpo de las noticias:
   - Tokeniza los textos y elimina stopwords (palabras vacías) en español.
   - Lista los 100 términos más frecuentes y los exporta a `top_100_terminos.txt`.
   - Aplica stemming (raíz de las palabras) y exporta los 100 stems más frecuentes a `top_100_stems.txt`.

## Requisitos

- Python 3.9+
- pipenv (para gestión de dependencias)
- requests
- beautifulsoup4
- nltk

## Instalación

1. Navegar al directorio del proyecto:
   ```bash
   cd tp3/2
   ```
2. Instalar dependencias:
   ```bash
   pipenv install
   ```

## Uso

1. Ejecutar el script principal:
   ```bash
   pipenv run python main.py
   ```

## Salida

- `output.json`: Archivo JSON con la información estructurada de las 10 noticias.
- `top_100_terminos.txt`: Ranking de los 100 términos más frecuentes (sin stopwords).
- `top_100_stems.txt`: Ranking de los 100 stems (raíces) más frecuentes tras stemming. 
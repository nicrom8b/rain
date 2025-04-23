# Análisis de N-gramas en Textos

Este proyecto implementa un analizador de n-gramas para textos en español, permitiendo identificar y contar la frecuencia de secuencias de palabras (2-gramas y 3-gramas) en un texto dado.

## Características

- Extracción del primer párrafo de un texto
- Tokenización y limpieza del texto
- Eliminación de stopwords en español
- Generación y análisis de bigramas (2-gramas) y trigramas (3-gramas)
- Visualización de frecuencias en formato de tabla

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.x
- NLTK (Natural Language Toolkit)
- pandas
- tabulate

## Instalación de dependencias

```bash
pip install nltk pandas tabulate
```

## Uso

1. Coloca tu archivo de texto (por ejemplo, `texto1.txt`) en el mismo directorio que el script
2. Ejecuta el script:

```bash
python main.py
```

El programa:
- Extraerá el primer párrafo del texto
- Procesará el texto eliminando stopwords y caracteres especiales
- Generará y mostrará las frecuencias de bigramas y trigramas
- Mostrará estadísticas generales del análisis

## Estructura del código

- `download_nltk_resources()`: Descarga los recursos necesarios de NLTK
- `get_first_paragraph()`: Extrae el primer párrafo del texto
- `process_text()`: Procesa y tokeniza el texto
- `generate_ngrams()`: Genera n-gramas a partir de los tokens
- `create_ngram_table()`: Crea una tabla con las frecuencias de n-gramas

## Ejemplo de salida

El programa mostrará:
- El primer párrafo del texto
- Tabla de bigramas más frecuentes
- Tabla de trigramas más frecuentes
- Estadísticas generales (número total de tokens, n-gramas únicos) 
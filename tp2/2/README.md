# Comparación de Algoritmos de Stemming

Este proyecto procesa un texto en inglés utilizando NLTK (Natural Language Toolkit) para:
1. Eliminar palabras vacías (stopwords) en inglés
2. Tokenizar el texto
3. Aplicar stemming usando los algoritmos de Porter y Lancaster
4. Comparar los resultados de ambos algoritmos

## Requisitos

- Python 3.9
- pipenv

## Configuración

1. Instalar dependencias:
```bash
pipenv install
```

2. Activar el entorno virtual:
```bash
pipenv shell
```

## Uso

Ejecutar el script:
```bash
python main.py
```

El script realizará:
1. Descarga de recursos necesarios de NLTK
2. Procesamiento del archivo de texto (texto2.txt)
3. Aplicación de stemming con los algoritmos de Porter y Lancaster
4. Visualización de la comparación en formato de tabla
5. Mostrado de estadísticas sobre la reducción de tokens

## Salida

La salida mostrará:
- Una tabla comparativa con las palabras originales y sus stems según cada algoritmo
- Estadísticas sobre el número total de tokens y la reducción lograda por cada algoritmo 
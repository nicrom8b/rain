# Procesamiento de Texto con NLTK

Este proyecto procesa un archivo de texto en español utilizando NLTK (Natural Language Toolkit) para:
1. Eliminar palabras vacías (stopwords) en español
2. Tokenizar el texto
3. Calcular frecuencias de palabras
4. Mostrar los resultados en orden descendente

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
2. Procesamiento del archivo de texto (texto1.txt)
3. Visualización de frecuencias de palabras en orden descendente

## Salida

La salida mostrará cada palabra y su frecuencia en el texto, ordenadas de mayor a menor frecuencia. 
# Procesamiento de Texto con NLTK y Corpus Brown

Este proyecto utiliza el corpus Brown de NLTK para procesar y analizar texto del archivo cg73.

## Descripción

El script realiza las siguientes tareas:
1. Descarga los recursos necesarios de NLTK (corpus Brown y tokenizador de oraciones)
2. Obtiene el texto del archivo cg73 del corpus Brown
3. Realiza una limpieza/eliminación de etiquetas POS y caracteres especiales
4. Tokeniza el texto en oraciones
5. Muestra las primeras 10 oraciones
6. Muestra estadísticas sobre el número total de oraciones
7. Guarda las oraciones en un archivo de texto, una por línea

## Requisitos

- Python 3.9
- pipenv

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pipenv install
```

## Uso

Para ejecutar el script:
```bash
pipenv run python main.py
```

## Salida

El script mostrará:
- Las primeras 10 oraciones del archivo cg73, cada una numerada y separada por líneas
- El número total de oraciones encontradas en el texto

## Dependencias

- nltk: Para el procesamiento de lenguaje natural y acceso al corpus Brown 
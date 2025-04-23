# Procesamiento de Texto con NLTK

Este proyecto implementa un procesador de texto que realiza diversas operaciones de análisis lingüístico utilizando la biblioteca NLTK (Natural Language Toolkit) de Python.

## Descripción

El script procesa un archivo de texto (`output.txt`) y realiza las siguientes operaciones:

1. **Eliminación de ruido**: Limpia el texto de caracteres especiales y números
2. **Tokenización**: Divide el texto en tokens individuales
3. **Normalización**: Filtra tokens que no son palabras
4. **Eliminación de palabras vacías**: Remueve palabras comunes del inglés
5. **Análisis de frecuencia**: Muestra las 50 palabras más frecuentes
6. **Stemming**: Aplica el algoritmo de Porter para reducir palabras a su raíz
7. **Lematización**: Reduce palabras a su forma base (lemma)
8. **Lematización con PoS**: Aplica lematización considerando la categoría gramatical
9. **Tabla comparativa**: Muestra los primeros 30 tokens con sus diferentes formas

## Requisitos

- Python 3.9
- pipenv (para gestión de dependencias)
- Dependencias de NLTK:
  - punkt
  - stopwords
  - wordnet

## Instalación

1. Clonar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd tp2/6
   ```
3. Instalar dependencias:
   ```bash
   pipenv install
   ```

## Uso

1. Asegurarse de que el archivo `output.txt` esté en el mismo directorio que `main.py`
2. Ejecutar el script:
   ```bash
   pipenv run python main.py
   ```

## Salida

El script generará la siguiente información:

- Texto limpio después de eliminar ruido
- Primeros 10 tokens en cada etapa de procesamiento
- Lista de las 50 palabras más frecuentes
- Tabla comparativa de los primeros 30 tokens mostrando:
  - Palabra original
  - Resultado del stemming
  - Resultado de la lematización
  - Resultado de la lematización con PoS

## Notas

- El script está optimizado para procesar texto en inglés
- La lematización con PoS utiliza una lista de verbos comunes para mejorar la precisión
- Los resultados se muestran en la consola en formato tabular 
# Stemming para Texto en Español

Este proyecto procesa un texto en español utilizando diferentes algoritmos de stemming para:
1. Eliminar palabras vacías (stopwords) en español
2. Tokenizar el texto
3. Aplicar diferentes algoritmos de stemming/lemmatización
4. Comparar los resultados de cada algoritmo

## Nota sobre Algoritmos de Stemming en NLTK

Los algoritmos de Porter y Lancaster en NLTK no tienen implementación para el idioma español. 
Estos algoritmos están diseñados específicamente para el idioma inglés y no son adecuados para 
otros idiomas debido a las diferencias en la morfología de las palabras.

En NLTK, el único algoritmo de stemming disponible para español es Snowball (también conocido como Porter2), que:
- Tiene soporte específico para español
- Es considerado una mejora del algoritmo Porter original
- Está diseñado para manejar las particularidades morfológicas del español
- Es el stemmer recomendado por NLTK para el procesamiento de texto en español

## Algoritmos Implementados

1. **Snowball (Porter2) Stemmer** (NLTK)
   - Implementación de NLTK
   - Especializado para español
   - Considerado una mejora del algoritmo Porter original

2. **Porter Stemmer** (stemming)
   - Implementación del algoritmo Porter original
   - Aunque está diseñado para inglés, se incluye para comparación
   - Más agresivo que Snowball

3. **SpaCy Lemmatization**
   - Usa modelos de lenguaje entrenados específicamente para español
   - Proporciona lemas en lugar de stems
   - Considerado más preciso pero más lento

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
1. Descarga de recursos necesarios
2. Procesamiento del archivo de texto (texto1.txt)
3. Aplicación de los diferentes algoritmos de stemming
4. Visualización de la comparación en formato de tabla
5. Mostrado de estadísticas sobre la reducción de tokens para cada algoritmo

## Salida

La salida mostrará:
- Una tabla comparativa con las palabras originales y sus stems según cada algoritmo
- Estadísticas sobre el número total de tokens y la reducción lograda por cada algoritmo 
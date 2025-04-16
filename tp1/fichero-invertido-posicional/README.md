# Índice Invertido con Posiciones de Palabras

Este proyecto crea un índice invertido a partir de documentos PDF, donde se registran las posiciones de cada palabra en el texto y permite calcular la distancia mínima entre pares de palabras.

## Características

- Extracción de texto de archivos PDF
- Eliminación de stopwords (palabras vacías) desde GitHub
- Normalización de texto (minúsculas, sin puntuación)
- Tokenización y filtrado de palabras
- Generación de índice invertido con posiciones de palabras por documento
- Cálculo de distancia mínima entre pares de palabras
- Logs detallados del proceso

## Estructura del Proyecto

```
fichero-invertido-posicional/
├── pdf/                    # Directorio con los PDFs a procesar
├── main.py                # Script principal
├── Pipfile               # Dependencias del proyecto
├── Pipfile.lock         # Versiones exactas de las dependencias
└── pyproject.toml       # Configuración de herramientas de desarrollo
```

## Formato del Índice Invertido

El índice invertido se guarda en formato JSON con la siguiente estructura:
```json
{
    "palabra1": {
        "documento1.pdf": [1, 15, 30],
        "documento2.pdf": [5, 20]
    },
    "palabra2": {
        "documento1.pdf": [10, 25],
        "documento3.pdf": [7, 12, 18]
    }
}
```
Donde:
- Las claves son las palabras encontradas en los documentos (normalizadas a minúsculas)
- Los valores son diccionarios que mapean nombres de documentos a listas de posiciones
- Las posiciones son números enteros que indican la ubicación de la palabra en el texto

## Funcionalidades

1. Generación de índice invertido
2. Cálculo de distancia mínima entre palabras predefinidas:
   - "proyecto" e "investigación"
   - "inteligencia" y "moderno"
3. Búsqueda personalizada de distancias entre cualquier par de palabras
4. Normalización automática de texto para búsquedas case-insensitive

## Requisitos

- Python 3.8+
- pipenv

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd fichero-invertido-posicional
```

2. Instalar pipenv si no está instalado:
```bash
pip install pipenv
```

3. Instalar dependencias:
```bash
pipenv install
```

4. Activar el entorno virtual:
```bash
pipenv shell
```

## Uso

1. Asegúrate de que los PDFs estén en el directorio `pdf/`

2. Ejecutar el script:
```bash
pipenv run python main.py
```

3. Usar el menú interactivo:
   - Opción 1: Generar índice invertido
   - Opción 2: Calcular distancia entre "proyecto" e "investigación"
   - Opción 3: Calcular distancia entre "inteligencia" y "moderno"
   - Opción 4: Calcular distancia entre palabras personalizadas
   - Opción 5: Salir

El script generará dos archivos:
1. `inverted_index.json`: Contiene el índice invertido con las posiciones de cada palabra
2. `processing_logs.txt`: Contiene los logs detallados del proceso

## Formateo y Linting

El proyecto usa:
- `black` para formateo de código
- `ruff` para linting

Para formatear el código:
```bash
pipenv run black .
```

Para ejecutar el linter:
```bash
pipenv run ruff check .
```

## Configuración

Las configuraciones de las herramientas de desarrollo se encuentran en `pyproject.toml`:

- Black: Configuración de formato
- Ruff: Reglas de linting y complejidad
- Python: Versión objetivo 3.11.8 
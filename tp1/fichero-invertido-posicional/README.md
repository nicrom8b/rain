# Índice Invertido con Posiciones de Palabras

Este proyecto crea un índice invertido a partir de documentos PDF, donde se registran las posiciones de cada palabra en el texto.

## Características

- Extracción de texto de archivos PDF
- Eliminación de stopwords (palabras vacías)
- Tokenización y filtrado de palabras
- Generación de índice invertido con posiciones de palabras
- Logs detallados del proceso

## Estructura del Proyecto

```
fichero-invertido-frecuencia/
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
    "palabra1": [pos1, pos2, pos3],
    "palabra2": [pos4, pos5, pos6]
}
```
Donde:
- Las claves son las palabras encontradas en los documentos
- Los valores son listas de posiciones donde aparece cada palabra
- Las posiciones son números enteros que indican la ubicación de la palabra en el texto

## Requisitos

- Python 3.8+
- pipenv

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd fichero-invertido-frecuencia
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
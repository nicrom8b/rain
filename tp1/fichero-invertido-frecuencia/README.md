# Índice Invertido de Frecuencias

Este proyecto genera un índice invertido de frecuencias a partir de documentos PDF, contando la frecuencia de aparición de cada palabra en cada documento.

## Características

- Extracción de texto de archivos PDF
- Eliminación de stopwords
- Normalización de texto (minúsculas, sin puntuación)
- Generación de índice invertido con frecuencias
- Guardado en formato JSON
- Logging detallado del proceso

## Requisitos

- Python 3.11
- pipenv
- black (formateador de código)
- ruff (linter)

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pipenv install
```

## Estructura del Proyecto

```
fichero-invertido-frecuencia/
├── main.py              # Script principal
├── Pipfile              # Dependencias del proyecto
├── pyproject.toml       # Configuración del proyecto
├── requirements.txt     # Dependencias para pip
└── pdf/                 # Directorio con archivos PDF
```

## Uso

1. Colocar los archivos PDF en el directorio `pdf/`
2. Ejecutar el script:
```bash
pipenv run python main.py
```

El script generará:
- `inverted_index.json`: Índice invertido con frecuencias
- `processing_logs.txt`: Logs del proceso

## Formato del Índice

El índice invertido se guarda en formato JSON con la siguiente estructura:
```json
{
    "palabra1": {
        "documento1.pdf": 5,
        "documento2.pdf": 3
    },
    "palabra2": {
        "documento1.pdf": 2
    }
}
```

## Mantenimiento del Código

Para mantener el código limpio y consistente:
```bash
# Formatear código
pipenv run black .

# Verificar estilo
pipenv run ruff check .
``` 
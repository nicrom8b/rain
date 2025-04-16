# Reconstrucción de Texto desde Índice Invertido

Este proyecto implementa un sistema para reconstruir texto original a partir de un índice invertido. El sistema toma un archivo JSON que contiene un índice invertido (palabras y sus posiciones) y reconstruye el texto original manteniendo el orden correcto de las palabras.

## Características

- Reconstrucción de texto basada en índice invertido
- Manejo robusto de errores
- Sistema de logging detallado
- Interfaz de línea de comandos interactiva
- Soporte para codificación UTF-8

## Requisitos

El proyecto utiliza Python y requiere las siguientes dependencias:
```
python >= 3.6
```

## Estructura del Proyecto

```
reconstruir-texto/
├── main.py                 # Script principal
├── index.json             # Archivo de índice invertido
├── reconstructed_text.txt # Texto reconstruido (salida)
├── reconstruction_logs.txt # Archivo de logs
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## Instalación

1. Clonar el repositorio o descargar los archivos
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecutar el script principal:
   ```bash
   python main.py
   ```

2. El programa mostrará un menú con las siguientes opciones:
   - 1: Reconstruir texto desde índice invertido
   - 2: Salir

3. Al seleccionar la opción 1:
   - Ingresar la ruta del archivo de índice (ej: index.json)
   - Especificar la longitud del texto (número de palabras)
   - El programa reconstruirá el texto y lo guardará en `reconstructed_text.txt`

## Formato del Índice Invertido

El archivo `index.json` debe contener un diccionario JSON con el siguiente formato:
```json
{
    "palabra1": [0, 3, 7],
    "palabra2": [1, 4],
    "palabra3": [2, 5, 6]
}
```
Donde:
- Las claves son las palabras del texto
- Los valores son listas de posiciones donde aparece cada palabra

## Logs

El sistema mantiene un registro detallado de operaciones en `reconstruction_logs.txt`, incluyendo:
- Carga exitosa del índice
- Reconstrucción del texto
- Advertencias sobre posiciones fuera de rango
- Errores durante el proceso

## Funcionalidades Principales

### `reconstruct_text()`
- Reconstruye el texto original a partir del índice invertido
- Maneja posiciones fuera de rango
- Valida la integridad de los datos

### `process_reconstruction()`
- Orquesta el proceso completo de reconstrucción
- Maneja la entrada/salida de archivos
- Gestiona errores y logging

## Limitaciones

- Requiere conocer la longitud exacta del texto original
- No verifica palabras faltantes en posiciones intermedias
- Asume que el índice invertido es válido y coherente

# OAI-PMH Harvester - CORA (Dataverse CSUC)

Este proyecto implementa un recolector (harvester) OAI-PMH para obtener al menos 100 registros del repositorio CORA (https://dataverse.csuc.cat/oai), extrayendo los campos principales y exportando los resultados a un archivo CSV.

## Descripción

El script realiza las siguientes operaciones:

1. Recolecta registros usando el endpoint OAI-PMH del repositorio CORA, consultando en formato Dublin Core (`oai_dc`).
2. Para cada registro, extrae:
   - **Titulo** (dc:title)
   - **Resumen** (dc:description)
   - **Autores** (dc:creator)
   - **Palabras claves** (dc:subject)
   - **Fecha** (dc:date)
   - Si hay varios valores para un campo (por ejemplo, varios autores), los une con punto y coma.
3. Exporta los resultados en formato CSV con las columnas: `Titulo`, `Resumen`, `Autores`, `Palabras claves`, `Fecha`.
4. Muestra el progreso en consola y un ejemplo de registro recolectado.

## Requisitos

- Python 3.9+
- pipenv (para gestión de dependencias)
- requests

## Instalación

1. Navegar al directorio del proyecto:
   ```bash
   cd tp4/4
   ```
2. Instalar dependencias:
   ```bash
   pipenv install
   ```

## Uso

1. Ejecutar el script principal:
   ```bash
   pipenv run python main.py
   ```
   El script mostrará el progreso y un ejemplo de registro por consola.

## Salida

- `output.csv`: Archivo CSV con la información estructurada de al menos 100 registros del repositorio CORA. Las columnas son:
  - Titulo
  - Resumen
  - Autores
  - Palabras claves
  - Fecha

## Notas sobre el código

- Solo se guardan registros que tengan al menos un campo con información.
- Si un campo tiene varios valores (por ejemplo, varios autores o palabras clave), se unen con punto y coma en la celda correspondiente del CSV.
- El script utiliza paginación automática (resumptionToken) para recolectar los registros necesarios. 
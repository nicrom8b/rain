# Indexador y Buscador de Documentos con Lucene (Java)

Este proyecto indexa y busca archivos PDF, DOCX, TXT y HTML usando Apache Lucene en Java.

## Estructura
- Los documentos a indexar deben estar en `Libros/` (dentro de `tp4/5`).
- El índice se almacena en `lucene_index/` (dentro de `tp4/5`).

## Requisitos
- Java 11+
- Maven

## Instalación y uso

1. Coloca tus archivos en `Libros/`.
2. Compila el proyecto:
   ```bash
   mvn compile
   ```
3. Ejecuta el indexador/buscador (desde el directorio `tp4/5`):
   ```bash
   mvn exec:java -Dexec.mainClass=org.example.Main
   ```
4. Ingresa el texto a buscar en la consola. Escribe `salir` para terminar.

## ¿Qué hace?
- Indexa todos los archivos PDF, DOCX, TXT y HTML en la carpeta indicada.
- El índice **se almacena y reutiliza** entre ejecuciones: no se borra ni reindexa todo desde cero.
- Si vuelves a ejecutar el programa, solo se actualizan los archivos nuevos o modificados.
- **No se generan duplicados**: antes de indexar un archivo, se elimina cualquier documento previo con el mismo path.
- Permite realizar búsquedas textuales sobre el contenido de los documentos.
- Muestra las rutas de los archivos que coinciden con la búsqueda.

## Dependencias principales
- Apache Lucene
- Apache PDFBox
- Apache POI (para DOCX)
- Jsoup (para limpiar HTML)

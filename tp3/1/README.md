# Crawler de Noticias Deportivas - Infobae

Este proyecto implementa un crawler para recolectar enlaces de noticias de la sección [Infobae Deportes](https://www.infobae.com/deportes/), y construye un grafo de referencias entre las noticias, visualizándolo y exportándolo para análisis avanzado.

## Descripción

El script realiza las siguientes operaciones:

1. Recolecta al menos 30 enlaces de noticias de la sección deportes de Infobae.
2. De cada noticia, extrae todos los enlaces a otras notas de deportes.
3. Construye una estructura de datos tipo grafo dirigido, donde cada nodo es una noticia y las aristas representan enlaces entre ellas, ponderadas por la cantidad de referencias.
4. Visualiza el grafo, destacando relaciones fuertes y dobles referencias.
5. Exporta el grafo en formatos PNG (imagen) y GEXF (para Gephi u otras herramientas de análisis de grafos).

## Requisitos

- Python 3.9+
- pipenv (para gestión de dependencias)
- requests
- beautifulsoup4
- networkx
- matplotlib
- scipy (para layouts avanzados de grafos)

## Instalación

1. Navegar al directorio del proyecto:
   ```bash
   cd tp3/1
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

## Salida

- `grafo_referencias.png`: Imagen del grafo de noticias y sus referencias.
- `grafo_referencias.gexf`: Grafo exportado en formato GEXF para análisis en Gephi.
- `references.json`: Estructura de referencias entre noticias en formato JSON.
- Estadísticas impresas en consola sobre enlaces y nodos.

## Visualización del Grafo

- **Nodos:** Cada nodo es una noticia deportiva (URL).
- **Aristas:** Una flecha de A a B indica que la noticia A enlaza a la noticia B.
- **Grosor de aristas:** Proporcional a la cantidad de enlaces entre dos noticias.
- **Color de aristas:**
  - Rojo: Existe doble referencia (A enlaza a B y B a A).
  - Gris: Referencia simple.
- **Etiquetas:** Solo los nodos con mayor grado muestran su URL para evitar superposición.
- **Distribución:** El grafo usa el layout Kamada-Kawai y escalado para separar los nodos y mejorar la legibilidad.

## Notas

- El crawler respeta las reglas de robots.txt de Infobae.
- El grafo puede exportarse en formatos compatibles con herramientas de visualización y análisis de redes (como Gephi).
- El código es modular y fácilmente adaptable para otras fuentes o secciones. 
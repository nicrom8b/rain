import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urljoin, urlparse
import time
import re
import json

# URL base de la sección deportes de Infobae
BASE_URL = "https://www.infobae.com/deportes/"


def get_news_links(base_url, min_links=30):
    """
    Recolecta al menos min_links enlaces de noticias de la sección deportes.
    Devuelve una lista de URLs de noticias reales (no secciones).
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_links = set()
    noticia_regex = re.compile(r"^/deportes/\d{4}/\d{2}/\d{2}/.+")
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Solo enlaces internos de noticias deportivas
        if href.startswith('http') and 'infobae.com/deportes/' not in href:
            continue
        if 'deportes' in href and not href.startswith('#') and 'undefined' not in href:
            full_url = urljoin(base_url, href)
            # Filtrar solo artículos reales (con fecha en la URL y sin 'undefined')
            path = urlparse(full_url).path
            if noticia_regex.match(path):
                news_links.add(full_url.split('?')[0])
        if len(news_links) >= min_links:
            break
    return list(news_links)[:min_links]


def extract_sports_links(news_url):
    """
    Extrae todos los enlaces a otras notas de deportes desde una noticia dada.
    Devuelve una lista de URLs absolutas.
    """
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        sports_links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http') and 'infobae.com/deportes/' not in href:
                continue
            if 'deportes' in href and not href.startswith('#'):
                full_url = urljoin(news_url, href)
                if full_url.startswith('https://www.infobae.com/deportes/') and full_url.count('/') > 5:
                    sports_links.add(full_url.split('?')[0])
        return list(sports_links)
    except Exception as e:
        print(f"Error extrayendo enlaces de {news_url}: {e}")
        return []


def build_graph_weighted(references):
    """
    Construye un grafo dirigido simple (DiGraph) donde los nodos son noticias y las aristas tienen un atributo 'weight'
    que indica la cantidad de enlaces entre dos noticias.
    """
    G = nx.DiGraph()
    edge_weights = dict()  # (src, dst) -> cantidad de enlaces
    for src, dst_list in references.items():
        for dst in dst_list:
            key = (src, dst)
            edge_weights[key] = edge_weights.get(key, 0) + 1
    for (src, dst), weight in edge_weights.items():
        G.add_edge(src, dst, weight=weight)
    return G


def main():
    # 1. Recolectar enlaces de noticias
    print("Recolectando enlaces de noticias...")
    noticia_regex = re.compile(r"^/deportes/\d{4}/\d{2}/\d{2}/.+")
    news_links = get_news_links(BASE_URL)
    print(f"Se recolectaron {len(news_links)} enlaces de noticias.")
    for i, url in enumerate(news_links, 1):
        print(f"[{i}] {url}")

    # 2. Para cada noticia, recolectar referencias a otras noticias deportivas reales
    references = dict()  # clave: noticia, valor: lista de noticias referenciadas
    for idx, news_url in enumerate(news_links, 1):
        print(f"\nNoticias deportivas referenciadas en la noticia [{idx}]: {news_url}")
        try:
            links = extract_sports_links(news_url)
            references[news_url] = sorted(links)
            if not links:
                print("  [Sin enlaces a otras noticias deportivas en esta noticia]")
            for i, lnk in enumerate(sorted(links), 1):
                print(f"  [{i}] {lnk}")
        except Exception as e:
            print(f"  Error extrayendo enlaces de {news_url}: {e}")
            references[news_url] = []

    # 3. Imprimir resumen de la estructura de referencias
    print("\nResumen de referencias (noticia -> cantidad de referencias):")
    for k, v in references.items():
        print(f"{k} -> {len(v)} referencias")

    # 4. Exportar la estructura a JSON
    with open("references.json", "w", encoding="utf-8") as f:
        json.dump(references, f, ensure_ascii=False, indent=2)
    print("\nEstructura de referencias exportada a references.json")

    # 5. Construir y visualizar el grafo
    print("\nConstruyendo y visualizando el grafo de referencias...")
    G = build_graph_weighted(references)
    plt.figure(figsize=(24, 16), dpi=200)  # Aumenta aún más el tamaño de la figura
    pos = nx.kamada_kawai_layout(G)
    # Escalar posiciones para separar más los nodos
    for k in pos:
        pos[k] = pos[k] * 2.5  # Escala las posiciones para mayor separación

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='skyblue')

    # Dibujar aristas con grosor proporcional al peso
    all_weights = [d['weight'] for u, v, d in G.edges(data=True)]
    max_weight = max(all_weights) if all_weights else 1
    edges = G.edges(data=True)
    for u, v, d in edges:
        width = 1 + 4 * (d['weight'] - 1) / max_weight  # más grueso si hay más enlaces
        color = 'red' if G.has_edge(v, u) else 'gray'  # rojo si hay doble entrada
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=width, edge_color=color, arrowsize=10, alpha=0.7)

    # Etiquetas solo para los nodos con mayor grado
    degrees = dict(G.degree())
    top_nodes = sorted(degrees, key=degrees.get, reverse=True)[:5]
    labels = {n: n for n in top_nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    plt.title("Grafo de referencias entre noticias deportivas (Infobae)\nAristas rojas: doble entrada, grosor: fuerza del enlace")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("grafo_referencias.png", dpi=300)
    print("\nGrafo exportado como grafo_referencias.png")

    # Exportar a GEXF (mejor formato para Gephi, la herramienta de visualización que estoy usando en MacOS)
    nx.write_gexf(G, "grafo_referencias.gexf")
    print("Grafo exportado como grafo_referencias.gexf (GEXF)")

    plt.show()

if __name__ == "__main__":
    main() 
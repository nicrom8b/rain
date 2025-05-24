import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin, urlparse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem.snowball import SnowballStemmer

BASE_URL = "https://www.infobae.com/economia/"


def get_news_links(base_url, max_links=10):
    """
    Recolecta los enlaces de las primeras max_links noticias de la sección economía.
    Devuelve una lista de URLs de noticias.
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_links = []
    # Buscar enlaces a notas reales (con fecha en la URL)
    # Ejemplo de patrón: /economia/2024/06/01/titulo-de-la-nota/
    noticia_regex = re.compile(r"^/economia/\d{4}/\d{2}/\d{2}/.+")
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http') and 'infobae.com/economia/' not in href:
            continue
        if 'economia' in href and not href.startswith('#') and 'undefined' not in href:
            full_url = urljoin(base_url, href)
            path = urlparse(full_url).path
            if noticia_regex.match(path):
                # Evitar duplicados
                if full_url not in news_links:
                    news_links.append(full_url)
        if len(news_links) >= max_links:
            break
    return news_links


def extract_news_data(news_url):
    """
    Extrae título, resumen, autor, imágenes y cuerpo de una noticia.
    Devuelve un diccionario con los datos.
    """
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Título
        titulo = None
        if soup.find('h1'):
            titulo = soup.find('h1').get_text(strip=True)

        # Resumen (bajada o copete)
        resumen = None
        resumen_tag = soup.find('h2')
        if resumen_tag:
            resumen = resumen_tag.get_text(strip=True)
        else:
            # A veces el resumen está en un div con clase 'excerpt' o similar
            resumen_div = soup.find('div', class_='excerpt')
            if resumen_div:
                resumen = resumen_div.get_text(strip=True)

        # Autor
        autor = None
        autor_tag = soup.find('span', class_='byline')
        if autor_tag:
            autor = autor_tag.get_text(strip=True)
        else:
            meta_autor = soup.find('meta', attrs={'name': 'author'})
            if meta_autor and meta_autor.get('content'):
                autor = meta_autor['content']
            else:
                # Buscar en JSON-LD (application/ld+json)
                for script in soup.find_all('script', type='application/ld+json'):
                    try:
                        import json as js
                        data = js.loads(script.string)
                        if isinstance(data, dict) and 'author' in data:
                            author_data = data['author']
                            if isinstance(author_data, dict) and 'name' in author_data:
                                autor = author_data['name']
                                break
                            elif isinstance(author_data, list) and len(author_data) > 0 and 'name' in author_data[0]:
                                autor = author_data[0]['name']
                                break
                    except Exception:
                        continue

        # Imágenes (ubicación de archivo)
        imagenes = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and '/economia/' in src:
                imagenes.append(src)
            elif src and src.startswith('https://www.infobae.com'):
                imagenes.append(src)
        # Eliminar duplicados
        imagenes = list(dict.fromkeys(imagenes))

        # Cuerpo de la nota
        cuerpo = ''
        # Buscar el contenedor principal del cuerpo
        cuerpo_tag = soup.find('div', class_='article-body')
        if not cuerpo_tag:
            cuerpo_tag = soup.find('div', class_='article__content')
        if cuerpo_tag:
            parrafos = cuerpo_tag.find_all(['p', 'h3'])
            cuerpo = '\n'.join(p.get_text(strip=True) for p in parrafos if p.get_text(strip=True))
        else:
            # Fallback: concatenar todos los <p>
            parrafos = soup.find_all('p')
            cuerpo = '\n'.join(p.get_text(strip=True) for p in parrafos if p.get_text(strip=True))

        return {
            "url": news_url,
            "titulo": titulo,
            "resumen": resumen,
            "autor": autor,
            "imagenes": imagenes,
            "cuerpo": cuerpo
        }
    except Exception as e:
        print(f"Error extrayendo datos de {news_url}: {e}")
        return {
            "url": news_url,
            "titulo": None,
            "resumen": None,
            "autor": None,
            "imagenes": [],
            "cuerpo": None
        }


def analizar_texto_cuerpos(noticias):
    """
    Tokeniza, elimina stopwords y lista los 100 términos más frecuentes de los cuerpos de las noticias.
    Exporta el ranking a 'top_100_terminos.txt'.
    También realiza stemming y exporta el ranking a 'top_100_stems.txt'.
    """
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('spanish'))
    stemmer = SnowballStemmer('spanish')
    all_tokens = []
    all_stems = []
    for noticia in noticias:
        cuerpo = noticia.get('cuerpo') or ''
        tokens = word_tokenize(cuerpo.lower())
        tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
        all_tokens.extend(tokens)
        stems = [stemmer.stem(t) for t in tokens]
        all_stems.extend(stems)
    # Ranking sin stemming
    counter = Counter(all_tokens)
    top_100 = counter.most_common(100)
    print("\nTop 100 términos más frecuentes en los cuerpos de las noticias:")
    for palabra, freq in top_100:
        print(f"{palabra}: {freq}")
    with open("top_100_terminos.txt", "w", encoding="utf-8") as f:
        for palabra, freq in top_100:
            f.write(f"{palabra}: {freq}\n")
    print("Ranking exportado a top_100_terminos.txt")
    # Ranking con stemming
    stem_counter = Counter(all_stems)
    top_100_stems = stem_counter.most_common(100)
    print("\nTop 100 raíces (stems) más frecuentes en los cuerpos de las noticias:")
    for stem, freq in top_100_stems:
        print(f"{stem}: {freq}")
    with open("top_100_stems.txt", "w", encoding="utf-8") as f:
        for stem, freq in top_100_stems:
            f.write(f"{stem}: {freq}\n")
    print("Ranking exportado a top_100_stems.txt")


def main():
    print("Recolectando enlaces de noticias...")
    news_links = get_news_links(BASE_URL)
    print(f"Se recolectaron {len(news_links)} enlaces de noticias.")
    for i, url in enumerate(news_links, 1):
        print(f"[{i}] {url}")

    noticias = []
    for url in news_links:
        print(f"Extrayendo datos de: {url}")
        data = extract_news_data(url)
        noticias.append(data)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)
    print("Datos exportados a output.json")

    # Análisis textual de los cuerpos
    analizar_texto_cuerpos(noticias)

if __name__ == "__main__":
    main() 
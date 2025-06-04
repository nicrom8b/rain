import json
import os
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.util import ngrams

nltk.download('stopwords')

NEWS_PATH = '../../tp3/2/output.json'

# Cargar noticias desde el JSON
def load_news(json_path):
    with open(json_path, 'r') as f:
        news = json.load(f)
    # Tomar solo las 10 primeras
    news = news[:10]
    docs = []
    for n in news:
        # Usar el campo 'cuerpo' como texto principal
        docs.append({'titulo': n['titulo'], 'texto': n['cuerpo']})
    return docs

def preprocess_text(text, remove_stopwords=False, use_bigrams=False):
    tokens = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    if remove_stopwords:
        stop_words = set(stopwords.words('spanish'))
        tokens = [t for t in tokens if t not in stop_words]
    if use_bigrams:
        bigrams = ['_'.join(bg) for bg in ngrams(tokens, 2)]
        tokens = tokens + bigrams
    return ' '.join(tokens)

REPRESENTATIONS = [
    {'name': 'Original', 'remove_stopwords': False, 'use_bigrams': False},
    {'name': 'Sin Stopwords', 'remove_stopwords': True, 'use_bigrams': False},
    {'name': 'Con Bigramas', 'remove_stopwords': False, 'use_bigrams': True},
]

def main():
    docs = load_news(NEWS_PATH)
    if len(docs) < 2:
        print('Se requieren al menos 2 noticias.')
        return
    # Dejar una para consulta
    query_doc = docs[-1]
    corpus_docs = docs[:-1]

    print(f"Noticia de consulta: {query_doc['titulo']}")
    print()

    for rep in REPRESENTATIONS:
        print(f"--- Representación: {rep['name']} (TF-IDF RepB) ---")
        corpus = [preprocess_text(d['texto'], rep['remove_stopwords'], rep['use_bigrams']) for d in corpus_docs]
        query = preprocess_text(query_doc['texto'], rep['remove_stopwords'], rep['use_bigrams'])
        # RepB: Representación TF-IDF de las noticias usando TfidfVectorizer de scikit-learn
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        q_vec = vectorizer.transform([query])
        scores = cosine_similarity(q_vec, X)[0]
        top_idx = scores.argsort()[::-1][:3]
        for idx in top_idx:
            print(f"Score: {scores[idx]:.4f}")
            print(f"Título: {corpus_docs[idx]['titulo']}")
            print(f"Texto (primeros 500 chars): {corpus_docs[idx]['texto'][:500]}")
            print()
        print()

if __name__ == '__main__':
    main() 
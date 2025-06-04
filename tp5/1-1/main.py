import os
import glob
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
import string

nltk.download('stopwords')

PDF_DIR = '../../tp1/pdf'

# Utilidad para extraer texto de un PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ''
    return text

# Cargar todos los PDFs
def load_documents(pdf_dir):
    pdf_files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    docs = []
    for pdf in pdf_files:
        text = extract_text_from_pdf(pdf)
        docs.append({'filename': os.path.basename(pdf), 'text': text})
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

# Representaciones
REPRESENTATIONS = [
    {'name': 'Original', 'remove_stopwords': False, 'use_bigrams': False},
    {'name': 'Sin Stopwords', 'remove_stopwords': True, 'use_bigrams': False},
    {'name': 'Con Bigramas', 'remove_stopwords': False, 'use_bigrams': True},
]

def main():
    docs = load_documents(PDF_DIR)
    if len(docs) < 2:
        print('Se requieren al menos 2 documentos PDF.')
        return
    # Dejar uno para consulta
    query_doc = docs[-1]
    corpus_docs = docs[:-1]

    print(f"Documento de consulta: {query_doc['filename']}")
    print()

    for rep in REPRESENTATIONS:
        print(f"--- Representación: {rep['name']} ---")
        # Preprocesar
        corpus = [preprocess_text(d['text'], rep['remove_stopwords'], rep['use_bigrams']) for d in corpus_docs]
        query = preprocess_text(query_doc['text'], rep['remove_stopwords'], rep['use_bigrams'])
        # TF-IDF
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        q_vec = vectorizer.transform([query])
        # Similaridad
        scores = cosine_similarity(q_vec, X)[0]
        # Top 3
        top_idx = scores.argsort()[::-1][:3]
        for idx in top_idx:
            print(f"Score: {scores[idx]:.4f}")
            print(f"Archivo: {corpus_docs[idx]['filename']}")
            print(f"Texto (primeros 500 chars): {corpus_docs[idx]['text'][:500]}")
            print()
        print()

if __name__ == '__main__':
    main() 
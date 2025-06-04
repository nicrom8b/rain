import nltk
import numpy as np
import networkx as nx
from nltk.corpus import inaugural, stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('inaugural')
nltk.download('punkt')
nltk.download('stopwords')

# Cargar el texto de Obama 2009
def get_obama_text():
    raw = inaugural.raw('2009-Obama.txt')
    return raw

# Método 1: Resumen por frecuencia de palabras

def summarize_frequency(text, n_sentences=8):
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalnum() and w not in stop_words]
    freq = nltk.FreqDist(words)
    sentence_scores = {}
    for sent in sentences:
        sent_words = word_tokenize(sent.lower())
        sent_words = [w for w in sent_words if w.isalnum()]
        score = sum(freq[w] for w in sent_words if w in freq)
        sentence_scores[sent] = score
    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ranked[:n_sentences]
    return summary

# Método 2: TextRank (grafo de similitud de oraciones)
def summarize_textrank(text, n_sentences=8):
    sentences = sent_tokenize(text)
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    sim_matrix = (X * X.T).toarray()
    np.fill_diagonal(sim_matrix, 0)
    nx_graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(nx_graph)
    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = [s for _, s in ranked[:n_sentences]]
    return summary

def main():
    text = get_obama_text()
    print('--- Resumen por Frecuencia de Palabras ---')
    freq_summary = summarize_frequency(text, n_sentences=8)
    for s in freq_summary:
        print('-', s)
    print('\n--- Resumen por TextRank ---')
    textrank_summary = summarize_textrank(text, n_sentences=8)
    for s in textrank_summary:
        print('-', s)
    print('\n--- Comparación ---')
    print(f'Oraciones en común: {len(set(freq_summary) & set(textrank_summary))}')
    print('Las oraciones en común son:')
    for s in set(freq_summary) & set(textrank_summary):
        print('-', s)

if __name__ == '__main__':
    main() 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import spacy
from stemming.porter2 import stem
import pandas as pd
from tabulate import tabulate
import re

def download_nltk_resources():
    """Descargar recursos necesarios de NLTK"""
    nltk.download('punkt')
    nltk.download('stopwords')

def process_text(file_path):
    """Procesar el archivo de texto y devolver los tokens"""
    # Leer el archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Eliminar puntuación y caracteres especiales
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Tokenizar el texto
    tokens = word_tokenize(text, language='spanish')
    
    # Obtener stopwords en español
    stop_words = set(stopwords.words('spanish'))
    
    # Eliminar stopwords y filtrar strings vacíos
    filtered_tokens = [word for word in tokens if word not in stop_words and word.strip()]
    
    return filtered_tokens

def apply_stemming(tokens):
    """Aplicar diferentes algoritmos de stemming a los tokens"""
    # Snowball (Porter2) Stemmer
    snowball = SnowballStemmer('spanish')
    snowball_stems = [snowball.stem(token) for token in tokens]
    
    # Porter Stemmer
    porter_stems = [stem(token) for token in tokens]
    
    # Lematización con SpaCy
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(' '.join(tokens))
    spacy_lemmas = [token.lemma_ for token in doc]
    
    return {
        'Snowball': snowball_stems,
        'Porter': porter_stems,
        'SpaCy': spacy_lemmas
    }

def create_comparison_table(tokens, stems_dict):
    """Crear una tabla de comparación de tokens originales y sus stems"""
    data = []
    for i, token in enumerate(tokens):
        row = [token]
        for algorithm in stems_dict:
            row.append(stems_dict[algorithm][i])
        data.append(row)
    
    headers = ['Original'] + list(stems_dict.keys())
    return tabulate(data, headers=headers, tablefmt='grid')

def main():
    # Descargar recursos necesarios de NLTK
    download_nltk_resources()
    
    # Procesar el texto
    tokens = process_text('texto1.txt')
    
    # Aplicar diferentes algoritmos de stemming
    stems_dict = apply_stemming(tokens)
    
    # Crear y mostrar tabla de comparación
    print("\nComparación de diferentes algoritmos de stemming para español:")
    print("-" * 100)
    print(create_comparison_table(tokens, stems_dict))
    
    # Imprimir algunas estadísticas
    print("\nEstadísticas:")
    print(f"Número total de tokens: {len(tokens)}")
    print(f"Número de tokens únicos: {len(set(tokens))}")
    
    for algorithm, stems in stems_dict.items():
        unique_stems = len(set(stems))
        reduction = ((1 - unique_stems/len(set(tokens))) * 100)
        print(f"\n{algorithm}:")
        print(f"  - Número de stems únicos: {unique_stems}")
        print(f"  - Reducción de vocabulario: {reduction:.2f}%")

if __name__ == "__main__":
    main() 
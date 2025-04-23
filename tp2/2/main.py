import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer
import pandas as pd
from tabulate import tabulate
import re

def download_nltk_resources():
    """Descarga los recursos necesarios de NLTK"""
    nltk.download('punkt')
    nltk.download('stopwords')

def process_text(file_path):
    """Procesa el archivo de texto y retorna los tokens"""
    # Leer el archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Eliminar puntuación y caracteres especiales
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Tokenizar el texto (dividir en palabras)
    tokens = word_tokenize(text)
    
    # Obtener palabras vacías (stopwords) en inglés
    stop_words = set(stopwords.words('english'))
    
    # Filtrar palabras vacías y cadenas vacías
    filtered_tokens = [word for word in tokens if word not in stop_words and word.strip()]
    
    return filtered_tokens

def apply_stemming(tokens):
    """Aplica los algoritmos de stemming Porter y Lancaster a los tokens"""
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    
    porter_stems = [porter.stem(token) for token in tokens]
    lancaster_stems = [lancaster.stem(token) for token in tokens]
    
    return porter_stems, lancaster_stems

def create_comparison_table(tokens, porter_stems, lancaster_stems):
    """Crea una tabla de comparación entre los tokens originales y sus stems"""
    data = []
    for token, porter, lancaster in zip(tokens, porter_stems, lancaster_stems):
        data.append([token, porter, lancaster])
    
    return tabulate(data, 
                   headers=['Original', 'Porter Stem', 'Lancaster Stem'],
                   tablefmt='grid')

def main():
    # Descargar recursos necesarios de NLTK
    download_nltk_resources()
    
    # Procesar el texto
    tokens = process_text('texto2.txt')
    
    # Aplicar stemming
    porter_stems, lancaster_stems = apply_stemming(tokens)
    
    # Crear y mostrar tabla de comparación
    print("\nComparación de Stemming (Porter vs Lancaster):")
    print("-" * 80)
    print(create_comparison_table(tokens, porter_stems, lancaster_stems))
    
    # Imprimir estadísticas
    print("\nEstadísticas:")
    print(f"Número total de tokens: {len(tokens)}")
    print(f"Número de tokens únicos: {len(set(tokens))}")
    print(f"Número de stems únicos (Porter): {len(set(porter_stems))}")
    print(f"Número de stems únicos (Lancaster): {len(set(lancaster_stems))}")

if __name__ == "__main__":
    main() 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
import pandas as pd
from tabulate import tabulate
import re

def download_nltk_resources():
    """Descarga los recursos necesarios de NLTK para el procesamiento de texto"""
    try:
        nltk.download('punkt')  # Para tokenización
        nltk.download('stopwords')  # Para palabras vacías
        nltk.download('wordnet')  # Para lematización
    except Exception as e:
        print(f"Error al descargar recursos de NLTK: {e}")
        raise

def read_text(filename):
    """Lee el contenido de un archivo de texto"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def remove_noise(text):
    """Limpia el texto eliminando caracteres especiales y números"""
    # Elimina todo lo que no sean letras o espacios
    text = re.sub(r'[^\w\s]', ' ', text)
    # Elimina espacios múltiples
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    """Divide el texto en palabras individuales (tokens)"""
    return word_tokenize(text.lower())

def normalize(tokens):
    """Filtra los tokens para mantener solo palabras"""
    # Mantiene solo tokens que contienen letras
    return [token for token in tokens if token.isalpha()]

def remove_stopwords(tokens):
    """Elimina palabras comunes que no aportan significado"""
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def get_top_words(tokens, n=50):
    """Calcula las n palabras más frecuentes en el texto"""
    return Counter(tokens).most_common(n)

def stem_tokens(tokens):
    """Reduce las palabras a su raíz usando el algoritmo de Porter"""
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def lemmatize_tokens(tokens):
    """Convierte las palabras a su forma base (lemma)"""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def lemmatize_tokens_with_pos(tokens):
    """Aplica lematización considerando la categoría gramatical de las palabras"""
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    
    # Lista de verbos comunes en inglés para mejor precisión
    common_verbs = {'be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see',
                   'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask',
                   'work', 'seem', 'feel', 'try', 'leave', 'call'}
    
    for token in tokens:
        # Si es un verbo común, lematiza como verbo
        if token in common_verbs:
            lemmatized.append(lemmatizer.lemmatize(token, 'v'))
        else:
            # Intenta primero como sustantivo
            lemma = lemmatizer.lemmatize(token, 'n')
            # Si no cambió, intenta como verbo
            if lemma == token:
                lemma = lemmatizer.lemmatize(token, 'v')
            lemmatized.append(lemma)
    
    return lemmatized

def create_comparison_table(tokens, stemmed, lemmatized, lemmatized_pos, n=30):
    """Crea una tabla comparativa de los primeros n tokens con sus diferentes formas"""
    data = []
    for i in range(min(n, len(tokens))):
        data.append([
            tokens[i],
            stemmed[i],
            lemmatized[i],
            lemmatized_pos[i]
        ])
    
    df = pd.DataFrame(data, columns=[
        'Palabra Original',
        'Stemming',
        'Lematización',
        'Lematización con PoS'
    ])
    
    return tabulate(df, headers='keys', tablefmt='grid', showindex=False)

def main():
    try:
        # Descarga los recursos necesarios de NLTK
        print("Descargando recursos de NLTK...")
        download_nltk_resources()
        print("Recursos descargados correctamente.")
        
        # Lee el archivo de texto
        text = read_text('output.txt')
        
        # A. Limpieza del texto
        print("\nA. Texto después de eliminar ruido:")
        print("-" * 80)
        cleaned_text = remove_noise(text)
        print(cleaned_text[:200] + "...")
        
        # B. Tokenización
        print("\nB. Primeros 10 tokens:")
        print("-" * 80)
        tokens = tokenize(cleaned_text)
        print(tokens[:10])
        
        # C. Normalización
        print("\nC. Primeros 10 tokens normalizados:")
        print("-" * 80)
        normalized_tokens = normalize(tokens)
        print(normalized_tokens[:10])
        
        # D. Eliminación de palabras vacías
        print("\nD. Primeros 10 tokens sin palabras vacías:")
        print("-" * 80)
        filtered_tokens = remove_stopwords(normalized_tokens)
        print(filtered_tokens[:10])
        
        # E. Análisis de frecuencia
        print("\nE. 50 palabras más frecuentes:")
        print("-" * 80)
        top_words = get_top_words(filtered_tokens)
        for word, count in top_words:
            print(f"{word}: {count}")
        
        # F. Stemming
        print("\nF. 50 palabras más frecuentes después de stemming:")
        print("-" * 80)
        stemmed_tokens = stem_tokens(filtered_tokens)
        top_stemmed = get_top_words(stemmed_tokens)
        for word, count in top_stemmed:
            print(f"{word}: {count}")
        
        # G. Lematización básica
        print("\nG. 50 palabras más frecuentes después de lematización:")
        print("-" * 80)
        lemmatized_tokens = lemmatize_tokens(filtered_tokens)
        top_lemmatized = get_top_words(lemmatized_tokens)
        for word, count in top_lemmatized:
            print(f"{word}: {count}")
        
        # H. Lematización con categoría gramatical
        print("\nH. 50 palabras más frecuentes después de lematización con PoS:")
        print("-" * 80)
        lemmatized_pos_tokens = lemmatize_tokens_with_pos(filtered_tokens)
        top_lemmatized_pos = get_top_words(lemmatized_pos_tokens)
        for word, count in top_lemmatized_pos:
            print(f"{word}: {count}")
        
        # I. Tabla comparativa
        print("\nI. Tabla comparativa de los primeros 30 tokens:")
        print("-" * 80)
        table = create_comparison_table(
            filtered_tokens[:30],
            stemmed_tokens[:30],
            lemmatized_tokens[:30],
            lemmatized_pos_tokens[:30]
        )
        print(table)
    
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
        print("Asegúrate de que todos los recursos de NLTK estén correctamente instalados.")
        print("Puedes intentar ejecutar manualmente:")
        print("import nltk")
        print("nltk.download('punkt')")
        print("nltk.download('stopwords')")
        print("nltk.download('wordnet')")

if __name__ == "__main__":
    main() 
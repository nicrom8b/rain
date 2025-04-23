import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from tabulate import tabulate
import re
from collections import Counter

def download_nltk_resources():
    """Descargar recursos necesarios de NLTK"""
    nltk.download('punkt')
    nltk.download('stopwords')

def get_first_paragraph(text):
    """Extraer el primer párrafo del texto"""
    # Dividir por punto seguido de nueva línea para obtener párrafos (punto a parte)
    paragraphs = re.split(r'\.\n', text)
    return paragraphs[0].strip() + '.'  # Agregar de nuevo el punto que fue removido

def process_text(text):
    """Procesar el texto y retornar tokens"""
    # Convertir a minúsculas
    text = text.lower()
    
    # Remover puntuación y caracteres especiales
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Tokenizar el texto
    tokens = word_tokenize(text, language='spanish')
    
    # Obtener stopwords en español
    stop_words = set(stopwords.words('spanish'))
    
    # Remover stopwords y filtrar strings vacíos
    filtered_tokens = [word for word in tokens if word not in stop_words and word.strip()]
    
    return filtered_tokens

def generate_ngrams(tokens, n):
    """Generar n-gramas a partir de tokens"""
    return list(nltk.ngrams(tokens, n))

def create_ngram_table(ngrams):
    """Crear una tabla con frecuencias de n-gramas"""
    # Contar frecuencias de n-gramas
    ngram_counts = Counter(ngrams)
    
    # Convertir a DataFrame para mejor formato
    df = pd.DataFrame({
        'N-gram': [' '.join(ngram) for ngram in ngram_counts.keys()],
        'Frecuencia': ngram_counts.values()
    })
    
    # Ordenar por frecuencia en orden descendente
    df = df.sort_values('Frecuencia', ascending=False)
    
    return tabulate(df, headers='keys', tablefmt='grid', showindex=False)

def main():
    # Descargar recursos necesarios de NLTK
    download_nltk_resources()
    
    # Leer el archivo de texto
    with open('texto1.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Obtener primer párrafo
    first_paragraph = get_first_paragraph(text)
    print("\nPrimer párrafo del texto:")
    print("-" * 80)
    print(first_paragraph)
    print("-" * 80)
    
    # Procesar el texto
    tokens = process_text(first_paragraph)
    
    # Generar y mostrar 2-gramas
    bigrams = generate_ngrams(tokens, 2)
    print("\n2-gramas (bigramas) más frecuentes:")
    print(create_ngram_table(bigrams))
    
    # Generar y mostrar 3-gramas
    trigrams = generate_ngrams(tokens, 3)
    print("\n3-gramas (trigramas) más frecuentes:")
    print(create_ngram_table(trigrams))
    
    # Imprimir algunas estadísticas
    print("\nEstadísticas:")
    print(f"Número total de tokens: {len(tokens)}")
    print(f"Número de 2-gramas únicos: {len(set(bigrams))}")
    print(f"Número de 3-gramas únicos: {len(set(trigrams))}")

if __name__ == "__main__":
    main() 
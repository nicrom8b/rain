import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import re
import matplotlib.pyplot as plt

def download_nltk_resources():
    """Descarga los recursos necesarios de NLTK"""
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

def process_text(file_path):
    """Procesa el archivo de texto y retorna las frecuencias de palabras"""
    # Leer el archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Eliminar puntuación y caracteres especiales
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenizar el texto (dividir en palabras)
    tokens = word_tokenize(text, language='spanish')
    
    # Obtener las palabras vacías (stopwords) en español
    stop_words = set(stopwords.words('spanish'))
    
    # Filtrar palabras vacías y cadenas vacías
    filtered_tokens = [word for word in tokens if word not in stop_words and word.strip()]
    
    # Contar la frecuencia de cada palabra
    word_freq = Counter(filtered_tokens)
    
    return word_freq

def plot_top_words(word_freq, top_n=20):
    """Genera un gráfico de barras con las N palabras más frecuentes"""
    # Obtener las N palabras más comunes y sus frecuencias
    top_words = word_freq.most_common(top_n)
    words = [word for word, _ in top_words]
    frequencies = [freq for _, freq in top_words]
    
    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(words, frequencies)
    plt.title('Top 20 Palabras Más Frecuentes')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Guardar el gráfico
    plt.savefig('top_words.png')
    plt.close()

def main():
    # Descargar recursos necesarios de NLTK
    download_nltk_resources()
    
    # Procesar el texto
    word_freq = process_text('texto1.txt')
    
    # Imprimir resultados en orden descendente
    print("\nFrecuencias de palabras (orden descendente):")
    print("-" * 50)
    for word, freq in word_freq.most_common():
        print(f"{word}: {freq}")
    
    # Generar gráfico de las 20 palabras más frecuentes
    plot_top_words(word_freq)
    print("\nGráfico guardado como 'top_words.png'")

if __name__ == "__main__":
    main() 
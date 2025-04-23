import nltk
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
import re

def download_nltk_resources():
    """Descarga los recursos necesarios de NLTK"""
    nltk.download('brown')
    nltk.download('punkt')

def get_cg73_text():
    """Obtiene el texto del archivo cg73 del corpus Brown"""
    # Obtiene el texto crudo del archivo cg73
    return brown.raw('cg73')

def clean_text(text):
    """Limpia el texto eliminando etiquetas POS y caracteres especiales"""
    # Elimina etiquetas POS (ej: /at, /jj, etc.)
    text = re.sub(r'/[a-zA-Z-]+', '', text)
    
    # Elimina comillas alrededor de cada carácter
    text = re.sub(r'"([^"])"', r'\1', text)
    
    # Elimina patrones especiales de comillas
    text = re.sub(r'``/``', '"', text)
    text = re.sub(r"''/''", '"', text)
    
    # Elimina todas las barras diagonales y sus caracteres circundantes
    text = re.sub(r'[.,]/?[.,]', lambda m: m.group(0)[0], text)
    
    # Elimina cualquier barra diagonal restante
    text = re.sub(r'/', '', text)
    
    # Elimina espacios extra
    text = re.sub(r' +', ' ', text)
    
    # Elimina espacios entre palabras y signos de puntuación
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)
    
    # Elimina espacios y comillas al inicio y final
    text = text.strip().strip('"')
    
    return text

def save_sentences_to_file(sentences, filename='output.txt'):
    """Guarda las oraciones en un archivo de texto, una por línea"""
    with open(filename, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')

def main():
    # Descarga los recursos necesarios de NLTK
    download_nltk_resources()
    
    # Obtiene el texto de cg73
    text = get_cg73_text()
    
    # Limpia el texto
    cleaned_text = clean_text(text)
    
    # Tokeniza en oraciones
    sentences = sent_tokenize(cleaned_text)
    
    # Muestra las primeras 10 oraciones en consola
    print("\nPrimeras 10 oraciones del archivo cg73:")
    print("-" * 80)
    for i, sentence in enumerate(sentences[:10], 1):
        print(f"\nOración {i}:")
        print(sentence)
        print("-" * 80)
    
    # Guarda todas las oraciones en el archivo
    save_sentences_to_file(sentences)
    print(f"\nTodas las oraciones han sido guardadas en output.txt")
    
    # Muestra estadísticas
    print("\nEstadísticas:")
    print(f"Número total de oraciones: {len(sentences)}")

if __name__ == "__main__":
    main() 
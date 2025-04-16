import os
import string
import logging
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple
import functools
import json

import PyPDF2
import requests

# Configurar logging
log_file = Path(__file__).parent / "processing_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


# Cache para stopwords
@functools.lru_cache(maxsize=1)
def get_stopwords_from_github() -> Set[str]:
    """Obtiene y cachea las stopwords desde GitHub."""
    logger.info("Obteniendo stopwords desde GitHub...")
    url = "https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        stopwords = set(
            word.strip() for word in response.text.splitlines() if word.strip()
        )
        logger.info(f"Se obtuvieron {len(stopwords)} stopwords.")
        return stopwords
    except requests.RequestException as e:
        logger.error(f"Error al obtener stopwords: {str(e)}")
        return set()


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extrae texto de un archivo PDF."""
    logger.info(f"Procesando archivo: {pdf_path.name}")
    text_chunks = []

    try:
        with pdf_path.open("rb") as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            logger.info(f"  - Total de páginas: {total_pages}")

            for i, page in enumerate(reader.pages, 1):
                try:
                    text_chunks.append(page.extract_text())
                    if i % 10 == 0:
                        logger.info(f"  - Procesadas {i}/{total_pages} páginas")
                except Exception as page_error:
                    logger.error(f"Error al procesar página {i}: {str(page_error)}")

            logger.info(f"  - Completado: {total_pages} páginas procesadas")
            return "".join(text_chunks)
    except Exception as e:
        logger.error(f"Error al leer {pdf_path}: {str(e)}")
        return ""


def preprocess_text(text: str) -> List[str]:
    """Preprocesa el texto removiendo puntuación y stopwords."""
    try:
        # Convertir a minúsculas y remover puntuación en un solo paso
        text = text.lower().translate(str.maketrans("", "", string.punctuation))
        logger.info("Texto convertido y puntuación removida")

        # Tokenización y filtrado en un solo paso
        stop_words = get_stopwords_from_github()
        tokens = [
            word for word in text.split() if word not in stop_words and len(word) > 1
        ]

        logger.info(f"Procesamiento completado. {len(tokens)} tokens generados")
        return tokens
    except Exception as e:
        logger.error(f"Error en el preprocesamiento del texto: {str(e)}")
        raise


def process_pdf_file(pdf_path: Path, doc_id: int) -> Tuple[Dict[str, int], str]:
    """Procesa un archivo PDF y retorna su índice y nombre."""
    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        logger.warning(f"No se pudo extraer texto de {pdf_path.name}")
        return {}, pdf_path.name

    # Crear diccionario de frecuencias para este documento
    word_freq = defaultdict(int)
    for token in preprocess_text(text):
        word_freq[token] += 1

    return word_freq, pdf_path.name


def create_inverted_index(pdf_files: List[Path]) -> Dict[str, Dict[str, List[int]]]:
    """
    Crea un índice invertido a partir de los archivos PDF, separando las posiciones por documento.
    
    Args:
        pdf_files: Lista de rutas a los archivos PDF.
        
    Returns:
        Diccionario con palabras como claves y otro diccionario como valor,
        donde las claves son nombres de PDF y los valores son listas de posiciones.
    """
    inverted_index: Dict[str, Dict[str, List[int]]] = {}
    
    for pdf_file in pdf_files:
        try:
            logger.info(f"Procesando archivo: {pdf_file.name}")
            text = extract_text_from_pdf(pdf_file)
            if not text:
                logger.warning(f"No se pudo extraer texto del archivo: {pdf_file.name}")
                continue
                
            # Normalizar el texto antes de tokenizar
            text = text.lower().translate(str.maketrans("", "", string.punctuation))
                
            # Tokenización y filtrado en un solo paso
            stop_words = get_stopwords_from_github()
            tokens = [word for word in text.split() 
                     if word not in stop_words and len(word) > 1]
            
            # Agregar palabras al índice invertido con sus posiciones por PDF
            for position, token in enumerate(tokens):
                if token not in inverted_index:
                    inverted_index[token] = {}
                if pdf_file.name not in inverted_index[token]:
                    inverted_index[token][pdf_file.name] = []
                inverted_index[token][pdf_file.name].append(position)
                
        except Exception as e:
            logger.error(f"Error procesando {pdf_file.name}: {str(e)}")
            continue
            
    return inverted_index


def calculate_min_distance(word1: str, word2: str, inverted_index: Dict[str, Dict[str, List[int]]]) -> Tuple[int, str, List[Tuple[int, int]]]:
    """
    Calcula la distancia mínima entre dos palabras en el mismo documento.
    
    Args:
        word1: Primera palabra a buscar
        word2: Segunda palabra a buscar
        inverted_index: Índice invertido con posiciones por documento
        
    Returns:
        Tupla con (distancia_mínima, nombre_del_documento, lista_de_pares_de_posiciones)
    """
    # Normalizar palabras de búsqueda
    word1 = word1.lower()
    word2 = word2.lower()
    
    min_distance = float('inf')
    document_name = ""
    position_pairs = []
    
    # Verificar si ambas palabras existen en el índice
    if word1 not in inverted_index or word2 not in inverted_index:
        print(f"Palabras disponibles en el índice: {list(inverted_index.keys())[:10]}...")  # Mostrar algunas palabras disponibles
        return -1, "Palabra no encontrada", []
    
    # Buscar en documentos comunes
    common_docs = set(inverted_index[word1].keys()) & set(inverted_index[word2].keys())
    
    for doc in common_docs:
        positions1 = inverted_index[word1][doc]
        positions2 = inverted_index[word2][doc]
        
        # Calcular todas las distancias posibles entre las posiciones
        for pos1 in positions1:
            for pos2 in positions2:
                distance = abs(pos1 - pos2)
                if distance < min_distance:
                    min_distance = distance
                    document_name = doc
                    position_pairs = [(pos1, pos2)]
                elif distance == min_distance:
                    position_pairs.append((pos1, pos2))
    
    return min_distance if min_distance != float('inf') else -1, document_name, position_pairs


def save_inverted_index(inverted_index: Dict[str, Dict[str, List[int]]], output_file: Path) -> None:
    """
    Guarda el índice invertido en un archivo JSON.
    
    Args:
        inverted_index: Diccionario con el índice invertido.
        output_file: Ruta del archivo de salida.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(inverted_index, f, ensure_ascii=False)
        logger.info(f"Índice invertido guardado en: {output_file}")
    except Exception as e:
        logger.error(f"Error al guardar el índice invertido: {str(e)}")
        raise


def show_menu() -> None:
    """Muestra el menú de opciones."""
    print("\n=== Menú de Opciones ===")
    print("1. Generar índice invertido")
    print("2. Calcular distancia entre 'proyecto' e 'investigación'")
    print("3. Calcular distancia entre 'inteligencia' y 'moderno'")
    print("4. Calcular distancia entre palabras personalizadas")
    print("5. Salir")
    print("=======================")


def main():
    try:
        # Usar Path para manejo de rutas
        current_dir = Path(__file__).parent
        pdf_directory = current_dir.parent / "pdf"
        output_file = current_dir / "inverted_index.json"
        
        inverted_index = None
        
        while True:
            show_menu()
            option = input("Seleccione una opción (1-5): ")
            
            if option == "1":
                logger.info(f"Buscando PDFs en: {pdf_directory}")
                logger.info(f"Los logs se guardarán en: {log_file}")
                logger.info(f"El índice invertido se guardará en: {output_file}")
                
                # Crear índice invertido
                pdf_files = sorted(pdf_directory.glob('*.pdf'))
                inverted_index = create_inverted_index(pdf_files)
                
                # Guardar resultados
                save_inverted_index(inverted_index, output_file)
                logger.info(f"Proceso completado. Índice guardado en {output_file}")
                logger.info(f"Logs guardados en {log_file}")
                
            elif option == "2":
                if inverted_index is None:
                    print("Primero debe generar el índice invertido (opción 1)")
                    continue
                    
                # Usamos palabras en minúsculas ya que el índice está normalizado
                word1 = "proyecto"
                word2 = "investigación"
                distance, doc, positions = calculate_min_distance(word1, word2, inverted_index)
                if distance != -1:
                    print(f"Distancia mínima entre '{word1}' y '{word2}': {distance} en el documento {doc}")
                    print(f"Posiciones encontradas: {positions}")
                else:
                    print(f"No se encontraron ambas palabras en el mismo documento")
                    
            elif option == "3":
                if inverted_index is None:
                    print("Primero debe generar el índice invertido (opción 1)")
                    continue
                    
                # Usamos palabras en minúsculas ya que el índice está normalizado
                word1 = "inteligencia"
                word2 = "moderno"
                distance, doc, positions = calculate_min_distance(word1, word2, inverted_index)
                if distance != -1:
                    print(f"Distancia mínima entre '{word1}' y '{word2}': {distance} en el documento {doc}")
                    print(f"Posiciones encontradas: {positions}")
                else:
                    print(f"No se encontraron ambas palabras en el mismo documento")
                    
            elif option == "4":
                if inverted_index is None:
                    print("Primero debe generar el índice invertido (opción 1)")
                    continue
                    
                word1 = input("Ingrese la primera palabra: ").strip()
                word2 = input("Ingrese la segunda palabra: ").strip()
                
                if not word1 or not word2:
                    print("Error: Ambas palabras son requeridas")
                    continue
                    
                distance, doc, positions = calculate_min_distance(word1, word2, inverted_index)
                if distance != -1:
                    print(f"Distancia mínima entre '{word1}' y '{word2}': {distance} en el documento {doc}")
                    print(f"Posiciones encontradas: {positions}")
                else:
                    print(f"No se encontraron ambas palabras en el mismo documento")
                    
            elif option == "5":
                print("Saliendo del programa...")
                break
                
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
                
    except Exception as e:
        logger.error(f"Error en el proceso principal: {str(e)}")
        raise


if __name__ == "__main__":
    main()

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


def create_inverted_index(pdf_files: List[Path]) -> Dict[str, List[int]]:
    """
    Crea un índice invertido a partir de los archivos PDF.

    Args:
        pdf_files: Lista de rutas a los archivos PDF.

    Returns:
        Diccionario con palabras como claves y listas de posiciones como valores.
    """
    inverted_index: Dict[str, List[int]] = {}
    current_position = 0

    for pdf_file in pdf_files:
        try:
            logger.info(f"Procesando archivo: {pdf_file.name}")
            text = extract_text_from_pdf(pdf_file)
            if not text:
                logger.warning(f"No se pudo extraer texto del archivo: {pdf_file.name}")
                continue

            # Tokenización y filtrado en un solo paso
            stop_words = get_stopwords_from_github()
            tokens = [
                word
                for word in text.split()
                if word not in stop_words and len(word) > 1
            ]

            # Agregar palabras al índice invertido con sus posiciones
            for token in tokens:
                if token not in inverted_index:
                    inverted_index[token] = []
                inverted_index[token].append(current_position)
                current_position += 1

        except Exception as e:
            logger.error(f"Error procesando {pdf_file.name}: {str(e)}")
            continue

    return inverted_index


def save_inverted_index(
    inverted_index: Dict[str, List[int]], output_file: Path
) -> None:
    """
    Guarda el índice invertido en un archivo JSON.

    Args:
        inverted_index: Diccionario con el índice invertido.
        output_file: Ruta del archivo de salida.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(inverted_index, f, ensure_ascii=False)
        logger.info(f"Índice invertido guardado en: {output_file}")
    except Exception as e:
        logger.error(f"Error al guardar el índice invertido: {str(e)}")
        raise


def main():
    try:
        # Usar Path para manejo de rutas
        current_dir = Path(__file__).parent
        pdf_directory = current_dir.parent / "pdf"
        output_file = current_dir / "inverted_index.json"

        logger.info(f"Buscando PDFs en: {pdf_directory}")
        logger.info(f"Los logs se guardarán en: {log_file}")
        logger.info(f"El índice invertido se guardará en: {output_file}")

        # Crear índice invertido
        pdf_files = sorted(pdf_directory.glob("*.pdf"))
        inverted_index = create_inverted_index(pdf_files)

        # Guardar resultados
        save_inverted_index(inverted_index, output_file)
        logger.info(f"Proceso completado. Índice guardado en {output_file}")
        logger.info(f"Logs guardados en {log_file}")

    except Exception as e:
        logger.error(f"Error en el proceso principal: {str(e)}")
        raise


if __name__ == "__main__":
    main()

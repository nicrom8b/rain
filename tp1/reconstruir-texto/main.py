import json
import logging
from pathlib import Path
from typing import Dict, List

# Configurar logging
log_file = Path(__file__).parent / "reconstruction_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def show_menu() -> None:
    """Muestra el menú de opciones."""
    print("\n=== Menú de Reconstrucción de Texto ===")
    print("1. Reconstruir texto desde índice invertido")
    print("2. Salir")
    print("=======================================")

def get_index_file() -> Path:
    """
    Solicita al usuario la ruta del archivo de índice.
    
    Returns:
        Path: Ruta al archivo de índice.
    """
    while True:
        file_path = input("\nIngrese la ruta del archivo de índice (ej: index.json): ")
        index_file = Path(file_path)
        
        if not index_file.exists():
            print(f"Error: El archivo '{file_path}' no existe.")
            continue
            
        if not index_file.is_file():
            print(f"Error: '{file_path}' no es un archivo.")
            continue
            
        return index_file

def get_text_length() -> int:
    """
    Solicita al usuario la longitud del texto.
    
    Returns:
        int: Longitud del texto.
    """
    while True:
        try:
            length = input("\nIngrese la longitud del texto (número de palabras): ")
            return int(length)
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def load_inverted_index(index_file: Path) -> Dict[str, List[int]]:
    """
    Carga el índice invertido desde un archivo JSON.
    
    Args:
        index_file: Ruta al archivo JSON con el índice invertido.
        
    Returns:
        Diccionario con el índice invertido.
    """
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            inverted_index = json.load(f)
        logger.info(f"Índice invertido cargado desde: {index_file}")
        return inverted_index
    except Exception as e:
        logger.error(f"Error al cargar el índice invertido: {str(e)}")
        raise

def reconstruct_text(inverted_index: Dict[str, List[int]], text_length: int) -> str:
    """
    Reconstruye el texto original a partir del índice invertido.
    
    Args:
        inverted_index: Diccionario con el índice invertido.
        text_length: Longitud total del texto original.
        
    Returns:
        Texto reconstruido.
    """
    try:
        # Crear lista de palabras vacías
        reconstructed = [''] * text_length
        
        # Colocar cada palabra en su posición
        for word, positions in inverted_index.items():
            for pos in positions:
                if pos < text_length:
                    reconstructed[pos] = word
                else:
                    logger.warning(f"Posición {pos} fuera de rango para la palabra '{word}'")
        
        # Unir las palabras con espacios
        text = ' '.join(reconstructed)
        logger.info("Texto reconstruido exitosamente")
        return text
    except Exception as e:
        logger.error(f"Error al reconstruir el texto: {str(e)}")
        raise

def save_reconstructed_text(text: str, output_file: Path) -> None:
    """
    Guarda el texto reconstruido en un archivo.
    
    Args:
        text: Texto reconstruido.
        output_file: Ruta del archivo de salida.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        logger.info(f"Texto reconstruido guardado en: {output_file}")
    except Exception as e:
        logger.error(f"Error al guardar el texto reconstruido: {str(e)}")
        raise

def process_reconstruction() -> None:
    """Procesa la reconstrucción del texto."""
    try:
        # Obtener archivo de índice
        index_file = get_index_file()
        
        # Obtener longitud del texto
        text_length = get_text_length()
        
        # Cargar índice invertido
        inverted_index = load_inverted_index(index_file)
        
        # Reconstruir texto
        reconstructed_text = reconstruct_text(inverted_index, text_length)
        
        # Mostrar texto reconstruido
        print("\n=== Texto Reconstruido ===")
        print(reconstructed_text)
        print("===========================")
        
        # Guardar resultado
        output_file = index_file.parent / "reconstructed_text.txt"
        save_reconstructed_text(reconstructed_text, output_file)
        
        print(f"\nProceso completado exitosamente!")
        print(f"Texto reconstruido guardado en: {output_file}")
        print(f"Logs guardados en: {log_file}")
        
    except Exception as e:
        print(f"\nError durante el proceso: {str(e)}")
        logger.error(f"Error en el proceso de reconstrucción: {str(e)}")

def main():
    while True:
        show_menu()
        choice = input("\nSeleccione una opción (1-2): ")
        
        if choice == "1":
            process_reconstruction()
        elif choice == "2":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor seleccione 1 o 2.")

if __name__ == "__main__":
    main() 
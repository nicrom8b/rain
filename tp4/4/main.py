import requests
import xml.etree.ElementTree as ET
import csv

OAI_ENDPOINT = "https://dataverse.csuc.cat/oai"
METADATA_PREFIX = "oai_dc"
REQUIRED_FIELDS = ["title", "description", "creator", "subject", "date"]
CSV_COLUMNS = ["Titulo", "Resumen", "Autores", "Palabras claves", "Fecha"]
FIELD_TO_CSV = {
    "title": "Titulo",
    "description": "Resumen",
    "creator": "Autores",
    "subject": "Palabras claves",
    "date": "Fecha"
}

def harvest_records(endpoint, metadata_prefix, min_records=100):
    # Armamos los parámetros para la consulta inicial
    params = {
        "verb": "ListRecords",
        "metadataPrefix": metadata_prefix
    }
    records = []
    resumption_token = None
    total_fetched = 0
    # Definimos los namespaces para que ElementTree entienda los prefijos del XML
    ns = {
        'oai': 'http://www.openarchives.org/OAI/2.0/',
        'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
    # Vamos a seguir pidiendo páginas hasta juntar los registros que queremos
    while len(records) < min_records:
        if resumption_token:
            # Si hay resumptionToken, seguimos desde donde quedamos
            params = {"verb": "ListRecords", "resumptionToken": resumption_token}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        # Recorremos cada registro que nos devuelve el XML
        for record in root.findall('.//oai:record', ns):
            metadata = record.find('.//oai:metadata', ns)
            if metadata is not None:
                # Buscamos el bloque con los metadatos Dublin Core
                dc_node = metadata.find('oai_dc:dc', ns)
                if dc_node is not None:
                    record_data = {}
                    # Para cada campo que queremos, buscamos todos los valores (por si hay más de uno)
                    for field in REQUIRED_FIELDS:
                        values = [el.text for el in dc_node.findall(f'dc:{field}', ns) if el.text]
                        # Si hay varios, los juntamos con punto y coma
                        record_data[FIELD_TO_CSV[field]] = "; ".join(values) if values else ""
                    # Solo guardamos el registro si tiene al menos un campo con info
                    if any(record_data.values()):
                        records.append(record_data)
                        total_fetched += 1
                        # Cada 10 registros, avisamos cómo vamos
                        if total_fetched % 10 == 0:
                            print(f"Recolectados {total_fetched} registros...")
                        if len(records) >= min_records:
                            break
        # Si hay más páginas, seguimos; si no, cortamos
        token_elem = root.find('.//oai:resumptionToken', ns)
        if token_elem is not None and token_elem.text:
            resumption_token = token_elem.text.strip()
        else:
            break
    return records[:min_records]


def save_to_csv(records, filename):
    # Guardamos los registros en un CSV, con los nombres de columnas bonitos
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for rec in records:
            row = {col: rec.get(col, "") for col in CSV_COLUMNS}
            writer.writerow(row)


def main():
    print("Recolectando registros de CORA...")
    records = harvest_records(OAI_ENDPOINT, METADATA_PREFIX, min_records=100)
    print(f"Se recolectaron {len(records)} registros.")
    if records:
        print("Ejemplo de registro:")
        for k, v in records[0].items():
            print(f"  {k}: {v}")
    else:
        print("ADVERTENCIA: No se recolectaron registros. Verifique la estructura del XML o la conectividad.")
    save_to_csv(records, "output.csv")
    print("Datos exportados a output.csv")

if __name__ == "__main__":
    main() 
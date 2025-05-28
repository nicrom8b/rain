# Query

```bash
curl -s -A "Mozilla/5.0" "https://ri.conicet.gov.ar/oai/request?verb=GetRecord&identifier=oai:ri.conicet.gov.ar:11336/149241&metadataPrefix=oai_dc" \
| xmllint --format - \
| pygmentize -l xml
```

# Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="static/style.xsl"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2025-05-27T23:17:53Z</responseDate>
  <request verb="GetRecord" identifier="oai:ri.conicet.gov.ar:11336/149241" metadataPrefix="oai_dc">https://ri.conicet.gov.ar/oai/request</request>
  <GetRecord>
    <record>
      <header>
        <identifier>oai:ri.conicet.gov.ar:11336/149241</identifier>
        <datestamp>2021-12-23T16:03:17Z</datestamp>
        <setSpec>com_11336_345</setSpec>
        <setSpec>com_11336_332</setSpec>
        <setSpec>col_11336_90201</setSpec>
        <setSpec>snrd</setSpec>
      </header>
      <metadata>
        <oai_dc:dc xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:doc="http://www.lyncode.com/xoai" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dc="http://purl.org/dc/elements/1.1/" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
          <dc:identifier>http://hdl.handle.net/11336/149241</dc:identifier>
          <dc:title>Bioinformática para la creación y fortalecimiento de empresas de base tecnológica: conceptos y aplicaciones</dc:title>
          <dc:creator>Balatti, Galo Ezequiel</dc:creator>
          <dc:creator>Flórez Zapata, Nathalia V.</dc:creator>
          <dc:contributor>Pellegrini, Pablo Ariel</dc:contributor>
          <dc:subject>BIOINFORMÁTICA</dc:subject>
          <dc:subject>EMPRENDEDORISMO</dc:subject>
          <dc:subject>STARTUPS</dc:subject>
          <dc:subject>https://purl.org/becyt/ford/1.2</dc:subject>
          <dc:subject>https://purl.org/becyt/ford/1</dc:subject>
          <dc:subject>https://purl.org/becyt/ford/5.2</dc:subject>
          <dc:subject>https://purl.org/becyt/ford/5</dc:subject>
          <dc:description>La bioinformática nace como una aproximación multidisciplinaria con el propósito de desarrollar técnicas de recolección, clasificación, almacenamiento y análisis de datos biológicos mediante la gestión de recursos computacionales. En los últimos años, ello generó un crecimiento exponencial de este tipo de datos, y el mayor desafío radica en convertir dicha información en recursos útiles para el sector académico e industrial. Así, la bioinformática ha logrado extenderse a la actividad comercial, donde empresas de base tecnológica (EBT) desarrollan y/o usufructan sus herramientas para ofrecer servicios de alto valor agregado. En el presente artículo describiremos la gama de herramientas disponibles para emprendedores tecnológicos y analizaremos el surgimiento de algunas de estas EBT.</dc:description>
          <dc:description>Fil: Balatti, Galo Ezequiel. Consejo Nacional de Investigaciones Científicas y Técnicas. Oficina de Coordinación Administrativa Ciudad Universitaria. Instituto de Física de Buenos Aires. Universidad de Buenos Aires. Facultad de Ciencias Exactas y Naturales. Instituto de Física de Buenos Aires; Argentina</dc:description>
          <dc:description>Fil: Flórez Zapata, Nathalia V.. Universidad en Envigado; Colombia</dc:description>
          <dc:date>2019</dc:date>
          <dc:type>info:eu-repo/semantics/publishedVersion</dc:type>
          <dc:type>info:eu-repo/semantics/bookPart</dc:type>
          <dc:type>info:ar-repo/semantics/parte de libro</dc:type>
          <dc:identifier>Balatti, Galo Ezequiel; Flórez Zapata, Nathalia V.; Bioinformática para la creación y fortalecimiento de empresas de base tecnológica: conceptos y aplicaciones; Universidad Nacional de Quilmes; 2019; 42-62</dc:identifier>
          <dc:identifier>978-987-558-611-6</dc:identifier>
          <dc:identifier>CONICET Digital</dc:identifier>
          <dc:identifier>CONICET</dc:identifier>
          <dc:language>spa</dc:language>
          <dc:relation>info:eu-repo/semantics/altIdentifier/url/http://www.unq.edu.ar/advf/documentos/5da9f2de18f72.pdf</dc:relation>
          <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>
          <dc:rights>https://creativecommons.org/licenses/by-nc-nd/2.5/ar/</dc:rights>
          <dc:format>application/pdf</dc:format>
          <dc:format>application/pdf</dc:format>
          <dc:format>application/pdf</dc:format>
          <dc:publisher>Universidad Nacional de Quilmes</dc:publisher>
        </oai_dc:dc>
      </metadata>
    </record>
  </GetRecord>
</OAI-PMH>
``` 
# Query

```bash
curl -s -A "Mozilla/5.0" "https://ri.conicet.gov.ar/oai/request?verb=ListMetadataFormats" \
| xmllint --format - \
| pygmentize -l xml
```

# Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="static/style.xsl"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2025-05-25T00:12:21Z</responseDate>
  <request verb="ListMetadataFormats">https://ri.conicet.gov.ar/oai/request</request>
  <ListMetadataFormats>
    <metadataFormat>
      <metadataPrefix>uketd_dc</metadataPrefix>
      <schema>http://naca.central.cranfield.ac.uk/ethos-oai/2.0/uketd_dc.xsd</schema>
      <metadataNamespace>http://naca.central.cranfield.ac.uk/ethos-oai/2.0/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>qdc</metadataPrefix>
      <schema>http://dublincore.org/schemas/xmls/qdc/2006/01/06/dcterms.xsd</schema>
      <metadataNamespace>http://purl.org/dc/terms/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>didl</metadataPrefix>
      <schema>http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-21_schema_files/did/didl.xsd
            </schema>
      <metadataNamespace>urn:mpeg:mpeg21:2002:02-DIDL-NS</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>mods</metadataPrefix>
      <schema>http://www.loc.gov/standards/mods/v3/mods-3-1.xsd</schema>
      <metadataNamespace>http://www.loc.gov/mods/v3</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>ore</metadataPrefix>
      <schema>http://tweety.lanl.gov/public/schemas/2008-06/atom-tron.sch</schema>
      <metadataNamespace>http://www.w3.org/2005/Atom</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>mets</metadataPrefix>
      <schema>http://www.loc.gov/standards/mets/mets.xsd</schema>
      <metadataNamespace>http://www.loc.gov/METS/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>oai_dc</metadataPrefix>
      <schema>http://www.openarchives.org/OAI/2.0/oai_dc.xsd</schema>
      <metadataNamespace>http://www.openarchives.org/OAI/2.0/oai_dc/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>rdf</metadataPrefix>
      <schema>http://www.openarchives.org/OAI/2.0/rdf.xsd</schema>
      <metadataNamespace>http://www.openarchives.org/OAI/2.0/rdf/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>marc</metadataPrefix>
      <schema>http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd</schema>
      <metadataNamespace>http://www.loc.gov/MARC21/slim</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>xoai</metadataPrefix>
      <schema>http://www.lyncode.com/schemas/xoai.xsd</schema>
      <metadataNamespace>http://www.lyncode.com/xoai</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>dim</metadataPrefix>
      <schema>http://www.dspace.org/schema/dim.xsd</schema>
      <metadataNamespace>http://www.dspace.org/xmlns/dspace/dim</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>etdms</metadataPrefix>
      <schema>http://www.ndltd.org/standards/metadata/etdms/1.0/etdms.xsd</schema>
      <metadataNamespace>http://www.ndltd.org/standards/metadata/etdms/1.0/</metadataNamespace>
    </metadataFormat>
  </ListMetadataFormats>
</OAI-PMH>
``` 
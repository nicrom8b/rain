# Query

```bash
curl -s -A "Mozilla/5.0" "https://ri.conicet.gov.ar/oai/request?verb=Identify" \
| xmllint --format - \
| pygmentize -l xml
```
# Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="static/style.xsl"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2025-05-24T14:16:25Z</responseDate>
  <request verb="Identify">https://ri.conicet.gov.ar/oai/request</request>
  <Identify>
    <repositoryName>CONICET Digital</repositoryName>
    <baseURL>https://ri.conicet.gov.ar/oai/request</baseURL>
    <protocolVersion>2.0</protocolVersion>
    <adminEmail>repositorio@conicet.gov.ar</adminEmail>
    <earliestDatestamp>2015-04-21T14:44:27Z</earliestDatestamp>
    <deletedRecord>transient</deletedRecord>
    <granularity>YYYY-MM-DDThh:mm:ssZ</granularity>
    <description>
      <oai-identifier xmlns="http://www.openarchives.org/OAI/2.0/oai-identifier" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai-identifier http://www.openarchives.org/OAI/2.0/oai-identifier.xsd">
        <scheme>oai</scheme>
        <repositoryIdentifier>ri.conicet.gov.ar</repositoryIdentifier>
        <delimiter>:</delimiter>
        <sampleIdentifier>oai:ri.conicet.gov.ar:11336/1234</sampleIdentifier>
      </oai-identifier>
    </description>
  </Identify>
</OAI-PMH>
```

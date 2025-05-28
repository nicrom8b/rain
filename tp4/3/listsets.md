# Query

```bash
curl -s -A "Mozilla/5.0" "https://ri.conicet.gov.ar/oai/request?verb=ListSets" \
| xmllint --format - \
| pygmentize -l xml
```

# Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="static/style.xsl"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2025-05-27T23:21:22Z</responseDate>
  <request verb="ListSets">https://ri.conicet.gov.ar/oai/request</request>
  <ListSets>
    <set>
      <setSpec>snrd</setSpec>
      <setName>Sistema Nacional de Repositorios Digitales</setName>
    </set>
    <set>
      <setSpec>com_11336_73</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - BAHIA BLANCA</setName>
    </set>
    <set>
      <setSpec>com_11336_116</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - CORDOBA</setName>
    </set>
    <set>
      <setSpec>com_11336_169</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - LA PLATA</setName>
    </set>
    <set>
      <setSpec>com_11336_184</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - MAR DEL PLATA</setName>
    </set>
    <set>
      <setSpec>com_11336_199</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - MENDOZA</setName>
    </set>
    <set>
      <setSpec>com_11336_330</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - NOA SUR</setName>
    </set>
    <set>
      <setSpec>com_11336_216</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - NORDESTE</setName>
    </set>
    <set>
      <setSpec>com_11336_85494</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - PATAGONIA CONFLUENCIA</setName>
    </set>
    <set>
      <setSpec>com_11336_229</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - PATAGONIA NORTE</setName>
    </set>
    <set>
      <setSpec>com_11336_252</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - ROSARIO</setName>
    </set>
    <set>
      <setSpec>com_11336_265</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SALTA-JUJUY</setName>
    </set>
    <set>
      <setSpec>com_11336_12</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTIFICO TECNOLOGICO CONICET - SAN JUAN</setName>
    </set>
    <set>
      <setSpec>com_11336_278</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SAN LUIS</setName>
    </set>
    <set>
      <setSpec>com_11336_305</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SANTA FE</setName>
    </set>
    <set>
      <setSpec>com_11336_48</setSpec>
      <setName>AREA DE INFLUENCIA CENTRO CIENTÍFICO TECNOLÓGICO CONICET - TANDIL</setName>
    </set>
    <set>
      <setSpec>com_11336_369</setSpec>
      <setName>AREA DE INFLUENCIA OFICINA DE COORDINACION ADMINISTRATIVA CIUDAD UNIVERSITARIA</setName>
    </set>
    <set>
      <setSpec>com_11336_414</setSpec>
      <setName>AREA DE INFLUENCIA OFICINA DE COORDINACION ADMINISTRATIVA HOUSSAY</setName>
    </set>
    <set>
      <setSpec>com_11336_441</setSpec>
      <setName>AREA DE INFLUENCIA OFICINA DE COORDINACION ADMINISTRATIVA PQUE. CENTENARIO</setName>
    </set>
    <set>
      <setSpec>com_11336_462</setSpec>
      <setName>AREA DE INFLUENCIA OFICINA DE COORDINACION ADMINISTRATIVA SAAVEDRA 15</setName>
    </set>
    <set>
      <setSpec>com_11336_35</setSpec>
      <setName>AREA DE INFLUENCIA SEDE CENTRAL</setName>
    </set>
    <set>
      <setSpec>com_11336_237393</setSpec>
      <setName>Audiovisuales</setName>
    </set>
    <set>
      <setSpec>com_11336_115106</setSpec>
      <setName>Bernardo Alberto Houssay</setName>
    </set>
    <set>
      <setSpec>com_11336_372</setSpec>
      <setName>BIOMED - INSTITUTO DE INVESTIGACIONES BIOMÉDICAS</setName>
    </set>
    <set>
      <setSpec>com_11336_465</setSpec>
      <setName>CADIC - CENTRO AUSTRAL DE INVESTIGACIONES CIENTÍFICAS</setName>
    </set>
    <set>
      <setSpec>com_11336_444</setSpec>
      <setName>CAICYT - CENTRO ARGENTINO DE INFORMACIÓN CIENTÍFICA Y TECNOLÓGICA</setName>
    </set>
    <set>
      <setSpec>com_11336_10</setSpec>
      <setName>CASLEO - COMPLEJO ASTRONÓMICO "EL LEONCITO"</setName>
    </set>
    <set>
      <setSpec>com_11336_138772</setSpec>
      <setName>CCONFINES - CENTRO DE CONOCIMIENTO, FORMACIÓN E INVESTIGACIÓN EN ESTUDIOS SOCIALES</setName>
    </set>
    <set>
      <setSpec>com_11336_202</setSpec>
      <setName>CECOAL - CENTRO DE ECOLOGÍA APLICADA DEL LITORAL</setName>
    </set>
    <set>
      <setSpec>com_11336_417</setSpec>
      <setName>CEDIE - CENTRO DE INVESTIGACIONES ENDOCRINOLÓGICAS "DR. CESAR BERGADA"</setName>
    </set>
    <set>
      <setSpec>com_11336_232</setSpec>
      <setName>CEFOBI - CENTRO DE ESTUDIOS FOTOSINTÉTICOS Y BIOQUÍMICOS</setName>
    </set>
    <set>
      <setSpec>com_11336_374</setSpec>
      <setName>CEFYBO - CENTRO DE ESTUDIOS FARMACOLÓGICOS Y BOTÁNICOS</setName>
    </set>
    <set>
      <setSpec>com_11336_446</setSpec>
      <setName>CEIL - CENTRO DE ESTUDIOS E INVESTIGACIONES LABORALES</setName>
    </set>
    <set>
      <setSpec>com_11336_14369</setSpec>
      <setName>CEMIC - CONICET - CENTRO DE EDUCACIÓN MÉDICA E INVESTIGACIONES CLÍNICAS "NORBERTO QUIRNO"</setName>
    </set>
    <set>
      <setSpec>com_11336_119</setSpec>
      <setName>CENEXA - CENTRO DE ENDOCRINOLOGÍA EXPERIMENTAL Y APLICADA</setName>
    </set>
    <set>
      <setSpec>com_11336_464</setSpec>
      <setName>CENTRO AUSTRAL DE INVESTIGACIONES CIENTÍFICAS</setName>
    </set>
    <set>
      <setSpec>com_11336_50</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - BAHIA BLANCA</setName>
    </set>
    <set>
      <setSpec>com_11336_75</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - CÓRDOBA</setName>
    </set>
    <set>
      <setSpec>com_11336_118</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - LA PLATA</setName>
    </set>
    <set>
      <setSpec>com_11336_171</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - MAR DEL PLATA</setName>
    </set>
    <set>
      <setSpec>com_11336_186</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - MENDOZA</setName>
    </set>
    <set>
      <setSpec>com_11336_307</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET NOA SUR</setName>
    </set>
    <set>
      <setSpec>com_11336_201</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - NORDESTE</setName>
    </set>
    <set>
      <setSpec>com_11336_85487</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - PATAGONIA CONFLUENCIA</setName>
    </set>
    <set>
      <setSpec>com_11336_218</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - PATAGONIA NORTE</setName>
    </set>
    <set>
      <setSpec>com_11336_231</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - ROSARIO</setName>
    </set>
    <set>
      <setSpec>com_11336_254</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET  SALTA-JUJUY</setName>
    </set>
    <set>
      <setSpec>com_11336_1</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SAN JUAN</setName>
    </set>
    <set>
      <setSpec>com_11336_267</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SAN LUIS</setName>
    </set>
    <set>
      <setSpec>com_11336_280</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - SANTA FE</setName>
    </set>
    <set>
      <setSpec>com_11336_37</setSpec>
      <setName>CENTRO CIENTÍFICO TECNOLÓGICO CONICET - TANDIL</setName>
    </set>
    <set>
      <setSpec>com_11336_229015</setSpec>
      <setName>CENTRO DE INVESTIGACIONES Y TRANSFERENCIA DEL NOROESTE DE LA PROVINCIA DE BUENOS AIRES</setName>
    </set>
    <set>
      <setSpec>com_11336_468</setSpec>
      <setName>CENTRO NACIONAL PATAGONICO</setName>
    </set>
    <set>
      <setSpec>com_11336_467</setSpec>
      <setName>CENTRO NACIONAL PATAGONICO</setName>
    </set>
    <set>
      <setSpec>com_11336_121</setSpec>
      <setName>CEPAVE - CENTRO DE ESTUDIOS PARASITOLÓGICOS Y DE VECTORES</setName>
    </set>
    <set>
      <setSpec>com_11336_123</setSpec>
      <setName>CEQUINOR - CENTRO DE QUÍMICA INORGÁNICA "DR. PEDRO J. AYMONINO"</setName>
    </set>
    <set>
      <setSpec>com_11336_308</setSpec>
      <setName>CERELA - CENTRO DE REFERENCIA PARA LACTOBACILOS</setName>
    </set>
    <set>
      <setSpec>com_11336_51</setSpec>
      <setName>CERZOS - CENTRO DE RECURSOS NATURALES RENOVABLES DE LA ZONA SEMIÁRIDA</setName>
    </set>
    <set>
      <setSpec>com_11336_14307</setSpec>
      <setName>CESIMAR - CENPAT - CENTRO PARA EL ESTUDIO DE SISTEMAS MARINOS</setName>
    </set>
    <set>
      <setSpec>com_11336_125</setSpec>
      <setName>CETMIC - CENTRO DE TECNOLOGÍA DE RECURSOS MINERALES Y CERÁMICA</setName>
    </set>
    <set>
      <setSpec>com_11336_448</setSpec>
      <setName>CEUR - CENTRO DE ESTUDIOS URBANOS Y REGIONALES</setName>
    </set>
    <set>
      <setSpec>com_11336_76</setSpec>
      <setName>CEVE - CENTRO EXPERIMENTAL DE LA VIVIENDA ECONÓMICA</setName>
    </set>
    <set>
      <setSpec>com_11336_48340</setSpec>
      <setName>CEVHAN - CENTRO DE VIROLOGÍA HUMANA Y ANIMAL</setName>
    </set>
    <set>
      <setSpec>com_11336_108921</setSpec>
      <setName>CIAP - CENTRO DE INVESTIGACIONES EN ARTE Y PATRIMONIO</setName>
    </set>
    <set>
      <setSpec>com_11336_48183</setSpec>
      <setName>CIBAAL - CENTRO DE INVESTIGACIÓN EN BIOFÍSICA APLICADA Y ALIMENTOS</setName>
    </set>
    <set>
      <setSpec>com_11336_78</setSpec>
      <setName>CIBICI - CENTRO DE INVESTIGACIÓN EN BIOQUÍMICA CLÍNICA E INMUNOLOGÍA</setName>
    </set>
    <set>
      <setSpec>com_11336_419</setSpec>
      <setName>CIBION - CENTRO DE INVESTIGACIONES EN BIONANOCIENCIAS "ELIZABETH JARES ERIJMAN"</setName>
    </set>
    <set>
      <setSpec>com_11336_127</setSpec>
      <setName>CIC - CENTRO DE INVESTIGACIONES CARDIOVASCULARES  "DR. HORACIO EUGENIO CINGOLANI"</setName>
    </set>
    <set>
      <setSpec>com_11336_80</setSpec>
      <setName>CICTERRA - CENTRO DE INVESTIGACIONES EN CIENCIAS DE LA TIERRA</setName>
    </set>
    <set>
      <setSpec>com_11336_15</setSpec>
      <setName>CICYTTP - CENTRO DE INVESTIGACIÓN CIENTÍFICA Y DE TRANSFERENCIA TECNOLÓGICA  A LA PRODUCCIÓN</setName>
    </set>
    <set>
      <setSpec>com_11336_129</setSpec>
      <setName>CIDCA - CENTRO DE INVESTIGACION Y DESARROLLO EN CIENCIA Y TECNOLOGIA DE LOS ALIMENTOS</setName>
    </set>
    <set>
      <setSpec>com_11336_131</setSpec>
      <setName>CIDEPINT - CENTRO DE INVESTIGACIONES EN TECNOLOGÍA DE PINTURAS</setName>
    </set>
    <set>
      <setSpec>com_11336_17</setSpec>
      <setName>CIDIE - CENTRO DE INVESTIGACIÓN Y DESARROLLO EN INMUNOLOGÍA Y ENFERMEDADES INFECCIOSAS</setName>
    </set>
    <set>
      <setSpec>com_11336_138765</setSpec>
      <setName>CIDMEJu - CENTRO DE INVESTIGACIÓN Y DESARROLLO EN MATERIALES AVANZADOS Y ALMACENAMIENTO DE ENERGÍA DE JUJUY</setName>
    </set>
    <set>
      <setSpec>com_11336_82</setSpec>
      <setName>CIECS - CENTRO DE INVESTIGACIONES Y ESTUDIOS SOBRE CULTURA Y SOCIEDAD</setName>
    </set>
    <set>
      <setSpec>com_11336_84</setSpec>
      <setName>CIEM - CENTRO DE INVESTIGACIÓN Y ESTUDIOS DE MATEMÁTICA</setName>
    </set>
    <set>
      <setSpec>com_11336_225</setSpec>
      <setName>CIEMEP - CENTRO DE INVESTIGACIÓN ESQUEL DE MONTAÑA Y ESTEPA PATAGÓNICA</setName>
    </set>
    <set>
      <setSpec>com_11336_14371</setSpec>
      <setName>CIESP - CENTRO DE INVESTIGACIONES EN EPIDEMIOLOGÍA Y SALUD PÚBLICA</setName>
    </set>
    <set>
      <setSpec>com_11336_234</setSpec>
      <setName>CIFASIS - CENTRO INTERNACIONAL FRANCO ARGENTINO DE CIENCIAS DE LA INFORMACIÓN Y DE SISTEMAS</setName>
    </set>
    <set>
      <setSpec>com_11336_38</setSpec>
      <setName>CIFICEN - CENTRO DE INVESTIGACIONES EN FÍSICA E INGENIERÍA DEL CENTRO DE LA PROVINCIA DE BUENOS AIRES</setName>
    </set>
    <set>
      <setSpec>com_11336_133</setSpec>
      <setName>CIG - CENTRO DE INVESTIGACIONES GEOLÓGICAS</setName>
    </set>
    <set>
      <setSpec>com_11336_4</setSpec>
      <setName>CIGEOBIO - CENTRO DE INVESTIGACIONES DE LA GEÓSFERA Y BIÓSFERA</setName>
    </set>
    <set>
      <setSpec>com_11336_333</setSpec>
      <setName>CIHIDECAR - CENTRO DE INVESTIGACIONES EN HIDRATOS DE CARBONO</setName>
    </set>
    <set>
      <setSpec>com_11336_450</setSpec>
      <setName>CIIPME - CENTRO  INTERDISCIPLINARIO DE INVESTIGACIONES EN PSICOLOGÍA MATEMÁTICA Y EXPERIMENTAL "DR. HORACIO J.A RIMOLDI"</setName>
    </set>
    <set>
      <setSpec>com_11336_48147</setSpec>
      <setName>CIITED - CENTRO INTERDISCIPLINARIO DE INVESTIGACIONES EN TECNOLOGÍAS Y DESARROLLO SOCIAL PARA EL NOA</setName>
    </set>
    <set>
      <setSpec>com_11336_335</setSpec>
      <setName>CIMA - CENTRO DE INVESTIGACIONES DEL MAR Y LA ATMÓSFERA</setName>
    </set>
    <set>
      <setSpec>com_11336_15829</setSpec>
      <setName>CIMAS - CENTRO DE INVESTIGACIÓN  APLICADA Y TRANSFERENCIA  TECNOLÓGICA  EN RECURSOS MARINOS "ALMIRANTE STORNI"</setName>
    </set>
    <set>
      <setSpec>com_11336_48294</setSpec>
      <setName>CIM - CENTRO DE INVESTIGACIONES DEL MEDIO AMBIENTE</setName>
    </set>
    <set>
      <setSpec>com_11336_281</setSpec>
      <setName>CIMEC - CENTRO DE INVESTIGACIÓN DE METODOS COMPUTACIONALES</setName>
    </set>
    <set>
      <setSpec>com_11336_135</setSpec>
      <setName>CINDECA - CENTRO DE INVESTIGACIÓN Y DESARROLLO EN CIENCIAS APLICADAS "DR. JORGE J. RONCO"</setName>
    </set>
    <set>
      <setSpec>com_11336_137</setSpec>
      <setName>CINDEFI - CENTRO DE INVESTIGACIÓN Y DESARROLLO EN FERMENTACIONES INDUSTRIALES</setName>
    </set>
    <set>
      <setSpec>com_11336_138758</setSpec>
      <setName>CINTRA - CENTRO DE INVESTIGACIÓN Y TRANSFERENCIA EN ACÚSTICA</setName>
    </set>
    <set>
      <setSpec>com_11336_139</setSpec>
      <setName>CIOP - CENTRO DE INVESTIGACIONES ÓPTICAS</setName>
    </set>
    <set>
      <setSpec>com_11336_376</setSpec>
      <setName>CIPYP - CENTRO DE INVESTIGACIONES SOBRE PORFIRINAS Y PORFIRIAS</setName>
    </set>
    <set>
      <setSpec>com_11336_86</setSpec>
      <setName>CIQUIBIC - CENTRO DE INVESTIGACIONES EN QUÍMICA BIOLÓGICA DE CÓRDOBA</setName>
    </set>
    <set>
      <setSpec>com_11336_421</setSpec>
      <setName>CIS - CENTRO DE INVESTIGACIONES SOCIALES</setName>
    </set>
    <set>
      <setSpec>com_11336_86135</setSpec>
      <setName>CITAAC - CENTRO  DE INVESTIGACIONES EN TOXICOLOGÍA AMBIENTAL Y AGROBIOTECNOLOGÍA DEL COMAHUE</setName>
    </set>
    <set>
      <setSpec>com_11336_88</setSpec>
      <setName>CITEQ - CENTRO DE INVESTIGACIÓN Y TECNOLOGÍA QUÍMICA</setName>
    </set>
    <set>
      <setSpec>com_11336_19</setSpec>
      <setName>CITRA - CENTRO DE INNOVACIÓN DE LOS TRABAJADORES</setName>
    </set>
    <set>
      <setSpec>com_11336_40</setSpec>
      <setName>CIVETAN - CENTRO DE INVESTIGACIÓN VETERINARIA DE TANDIL</setName>
    </set>
    <resumptionToken completeListSize="2444" cursor="0">////100</resumptionToken>
  </ListSets>
</OAI-PMH>
``` 
# Dataset de métricas de los estados de México
Este repositorio es el proceso de creación de un dataset con indicadores de cada estado México que pueden ser pertinentes para el análisis del comportamiento del COVID-19 en este país.

### Objetivo de salida:
Un dataset en la que cada fila es una entidad federativa de México y cada columna un indicador sobre dicha entidad.

## ¿Cómo funciona?
1. Se hizo un proceso manual de recolección de datos en fuentes oficales del Gobierno de México ([datos abiertos](https://datos.gob.mx/) y [INEGI](https://www.inegi.org.mx)). De alli de bajaron selectivamente varios .csv y .xlsx con datos considerados pertinentes. Cada fuente está detallada en el diccionario anexo al readme y como archivos .csv y .xlsx.
2. Posteriormente se usó Python con la librería pandas para limpiar y normalizar los datos.
3. Finalmente se unieron todos los datos en un solo dataset.

## Requerimientos
+ Python (pandas, numpy, matplotlib).
+ Recomendado [Anaconda](https://www.anaconda.com/distribution/).

## Fuentes
La fuente de información de cada columna está especificada en el diccionario (anexo al readme y como archivos .csv y .xlsx). Dichas fuentes incluyen https://datos.gob.mx/ y https://www.inegi.org.mx/.

## Estructura de carpetas
+ `source:` Archivos .csv y .xlsx a partir de los que se generó el dataset final. Aquí también se encuentran los scripts de Python usados para crearlo, tanto en formato .py como en formato .ipynb (jupyter notebook).
+ `out:` Contiene el dataset generado.

## Diccionario
|CLAVE      |DESCRIPCION                                                              |Unidad de medida                  |Definicion                                                                                                     |FUENTE                                                                                               |Archivo           |Notas                    |
|-----------|-------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------|-------------------------|
|EDO        |Entidad federativa                                                       |                                  |                                                                                                               |                                                                                                     |                  |                         |
|DET:DIAB.18|Detección padecimientos Diabetes por delegación, año 2018                |                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/13002ba5-e98d-4e41-bdaa-86500fcd8a63|istabla43_2018.csv|                         |
|DET.DIAB.15|Detección padecimientos Diabetes por delegación, año 2015                |                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/13002ba5-e98d-4e41-bdaa-86500fcd8a63|istabla43_2018.csv|                         |
|DET.HIPT.18|Detección de padecimientos Hipertensión arterial por delegación, año 2018|                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/ec805b62-dc3f-4147-a9f3-e69d93081e29|istabla45_2018.csv|                         |
|DET.HIPT.15|Detección de padecimientos Hipertensión arterial por delegación, año 2015|                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/ec805b62-dc3f-4147-a9f3-e69d93081e30|istabla45_2018.csv|                         |
|DET.TOT.18 |Número total de detecciones por delegación, año 2018                     |                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/f4c845a5-1267-49ba-9211-b191a21c53b8|istabla39_2018.csv|                         |
|DET.TOT.15 |Número total de detecciones por delegación, año 2015                     |                                  |                                                                                                               |https://datos.gob.mx/busca/dataset/informacion-en-salud/resource/f4c845a5-1267-49ba-9211-b191a21c53b9|istabla39_2018.csv|                         |
|POB.DEN.15 |Densidad de población por entidad federativa, año 2015                   |Habitantes por kilómetro cuadrado.|Cociente de la población total entre la superficie territorial.                                                |https://www.inegi.org.mx/app/tabulados/interactivos/?px=Poblacion_07&bd=Poblacion                    |Población_07.xlsx |Convertido a csv en excel|
|POB.ENV.15 |Índice de envejecimiento por entidad federativa                          |Porcentaje.                       |Número de personas adultas mayores (60 y más años de edad) por cada cien niños y jóvenes (0 a 14 años de edad).|https://www.inegi.org.mx/app/tabulados/interactivos/?px=Poblacion_05&bd=Poblacion                    |Población_05.xlsx |Convertido a csv en excel|
|POB.HAB.15 |Poblacion por entidad federativa, año 2015                               |                                  |                                                                                                               |https://www.inegi.org.mx/programas/intercensal/2015/default.html#Tabulados                           |01_poblacion.xls  |Convertido a csv en excel|

## How contribute? :rocket:

Please feel free to contribute to this project, please fork the repository and make a pull request!. :heart:

## Share the Love :heart:

Like this project? Please give it a ★ on [this GitHub](https://github.com/Innovacion-Mexico/sesa-qroo-covid19-extractor)! (it helps me a lot).

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

See [LICENSE](LICENSE) for full details.

    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

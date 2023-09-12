# Escuadrón JADE 
### IA - Reto1_ETL
Momento de Retroalimentación: Reto Limpieza del Conjunto de Datos

Dentro de este repositorio se encuentra un archivo ".pdf" ("Reto_Limpieza_Conjunto_Datos.pdf") en el que podrá encontrar una descripción a detalle de lo realizado para este primer avance del reto con respecto a ETL's; continuando con el otro archivo del repositorio este es un ".zip" ("Avance1_Equipo_JADE.zip") contiene el dataset sobre el que se esta trabajndo el reto y una notebook, los archivos que conforman el dataset son todos ".csv" y tienen los siguientes nombres, "train.csv", "test.csv", "oil.csv", "stores.csv", "sample_submission.csv", "holidays_events.csv" y "transactions.csv". Para el caso de la notebook esta tiene el nombre de "ETL_revisión_JADE.ipynb" y en ella se encuentra la exploración de los datos así como la realización del ETL con respecto al dataset antes mencionado.

**IMPORTANTE:** Para correr el código de la notebook ("ETL_revisión_JADE.ipynb") dentro del ".zip" es NECESARIO haber descargado en su equipo de computo el archivo comprimido "Avance1_Equipo_JADE.zip" y descomprimirlo para poder acceder a los archivos de su interior; una vez realizado lo anterior para ver el correcto funcionamiento del código debe de modificar las reutas de acceso dentro de la segunda celda de la notebook ("ETL_revisión_JADE.ipynb") por la dirección en la que haya guardado la carpeta descomprimida con todos los archivos del dataset dentro de su equipo de computo. Deben de concordar el archivo al que esta llamando con el nombre de la variable dentro del código.

# Descripción de los datos

### train.csv

El archivo `train.csv` contiene datos de entrenamiento para un problema de series temporales. Incluye información sobre las ventas de productos en diferentes tiendas a lo largo del tiempo. Los campos principales en este archivo son:

- **store_nbr**: Identifica la tienda en la que se venden los productos.
- **family**: Identifica el tipo de producto vendido.
- **sales**: Representa las ventas totales de una familia de productos en una tienda en una fecha específica. Las ventas pueden ser valores fraccionarios debido a la posibilidad de vender productos en unidades fraccionarias.
- **onpromotion**: Indica el número total de artículos de una familia de productos que estaban en promoción en una tienda en una fecha determinada.

### test.csv

El archivo `test.csv` contiene datos de prueba que tienen las mismas características que los datos de entrenamiento. El objetivo es predecir las ventas futuras para las fechas en este archivo. Es importante destacar que las fechas en el archivo de prueba son para los 15 días posteriores a la última fecha en el archivo de entrenamiento.

### sample_submission.csv

El archivo `sample_submission.csv` es un archivo de muestra que sigue el formato correcto para presentar las predicciones.

- **id**: El cual es un identificador para las ventas futuras que se predicen
- **sales**: Muestra la proyección  relacionada al id previo


### stores.csv

El archivo `stores.csv` contiene metadatos sobre las tiendas que están involucradas en el conjunto de datos. Incluye información sobre la ciudad:

- **store_nbr**: El cual es un numero que identifica a la tienda en particular
- **city**: Muestra las ciudades donde se ubica la tienda
- **state**: Muestra el estado donde se ubica la tienda
- **type**: Sin descripción en particular
- **cluster**: Sin descripción en particular


### oil.csv

El archivo `oil.csv` proporciona datos diarios sobre los precios del petróleo. Estos datos son relevantes tanto para el período de entrenamiento como para el período de prueba. Dado que Ecuador depende en gran medida del petróleo en términos económicos, las fluctuaciones en los precios del petróleo pueden tener un impacto significativo en las ventas de productos.
- **date**: Muestra una fecha en particular
- **dcoilwtico**: Muestra el precio del barril de petróleo el en un día en particular
 

### holidays_events.csv

El archivo `holidays_events.csv` contiene información sobre días festivos y eventos, junto con metadatos. Es importante prestar atención a la columna "transferred", que indica si un día festivo fue oficialmente transferido a otra fecha por el gobierno. En algunos casos, un día festivo puede ser celebrado en una fecha diferente a la del calendario. También se menciona la columna "type", que describe el tipo de día festivo (como "Transfer" para días transferidos y "Bridge" para días adicionales agregados a un día festivo).

Además, el conjunto de datos puede incluir días festivos adicionales agregados a días festivos regulares, como suele ocurrir alrededor de la Navidad (haciendo que la Nochebuena sea un día festivo). Estos días adicionales a menudo se compensan con días de trabajo tipo "Work Day" que no están programados normalmente para trabajar (por ejemplo, sábados) y están destinados a compensar los días festivos adicionales.


- **date**: Identifica la tienda en la que se venden los productos.
- **type**: Indica el tipo de festividad tales como Holidays, Events, Work day etc.
- **locale**: Indica el alcance de la festividad
- **locale_name**: Indica el número total de artículos de una familia de productos que estaban en promoción en una tienda en una fecha determinada.

- **description**: Descripcion del la festividad

- **transferred**: De tipo booleano que indica si un día festivo que se transfiere oficialmente cae en ese día calendario.

# Normativas de Kaggle

De acuerdo con las normativas de la plataforma **Kaggle**, al participar en el concurso, los miembros de un equipo deben tener en cuenta ciertas consideraciones específicas:

- No está permitido transmitir, duplicar, publicar, redistribuir ni proporcionar los Datos del Concurso a terceros que no estén participando en el Concurso. Cualquier posible transmisión o acceso no autorizado a los Datos de la Competencia debe notificarse inmediatamente a Kaggle, y se debe colaborar con Kaggle para corregir cualquier transmisión o acceso no autorizado.

## Uso de Datos Externos

En cuanto al uso de los datos, se permite la utilización de datos externos además de los proporcionados por la competencia, siempre y cuando estos datos externos sean públicos y estén disponibles de forma gratuita para todos los participantes. Sin embargo, es importante destacar que esta posibilidad de utilizar datos externos no exime a los participantes de sus otras responsabilidades y obligaciones según las reglas de la competencia, incluidas aquellas relacionadas con los ganadores.

## Finalidad Académica

En resumen, nuestro equipo no tiene ningún problema con los términos y condiciones establecidos en la plataforma. El uso que hacemos de los datos es exclusivamente con fines académicos, con el objetivo de poner a prueba nuestra capacidad en el análisis de datos.


# Licencias de Bibliotecas Python

A continuación se presentan las licencias de las bibliotecas Python comúnmente utilizadas en análisis de datos y aprendizaje automático:

## Matplotlib
- **Licencia:** Matplotlib utiliza una licencia estilo BSD.
- **Descripción:** Matplotlib es una biblioteca de trazado en 2D en Python. Es ampliamente utilizado para crear gráficos y visualizaciones.
- **Sitio web oficial:** [Matplotlib License](https://matplotlib.org/stable/users/license.html)

## Seaborn
- **Licencia:** Seaborn utiliza una licencia estilo BSD.
- **Descripción:** Seaborn es una biblioteca de visualización de datos basada en Matplotlib. Proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos.
- **Sitio web oficial:** [Seaborn License](https://seaborn.pydata.org)

## Pandas
- **Licencia:** Pandas utiliza la licencia BSD de 3 cláusulas.
- **Descripción:** Pandas es una biblioteca de manipulación y análisis de datos que proporciona estructuras de datos y herramientas de análisis fáciles de usar para trabajar con datos tabulares.
- **Sitio web oficial:** [Pandas License](https://pandas.pydata.org/pandas-docs/stable/whatsnew/v1.3.3.html#license)

## NumPy
- **Licencia:** NumPy utiliza la licencia BSD de 3 cláusulas.
- **Descripción:** NumPy es una biblioteca fundamental para la computación numérica en Python. Proporciona soporte para matrices y arreglos multidimensionales, así como funciones matemáticas para trabajar con ellos.
- **Sitio web oficial:** [NumPy License](https://numpy.org/doc/stable/license.html)

## Scikit-Learn (sklearn)
- **Licencia:** Scikit-Learn utiliza la licencia BSD de 3 cláusulas.
- **Descripción:** Scikit-Learn es una biblioteca de aprendizaje automático en Python que proporciona herramientas para la clasificación, regresión, agrupación, selección de modelos y más.
- **Sitio web oficial:** [Scikit-Learn License](https://scikit-learn.org/stable/whats_new/v1.1.0.html#id9)

## TensorFlow
- **Licencia:** TensorFlow utiliza la licencia Apache 2.0, que es una licencia de código abierto que permite el uso, la modificación y la distribución del software, siempre y cuando se cumplan ciertas condiciones. Consulta la [licencia de TensorFlow](https://github.com/tensorflow/tensorflow/blob/master/LICENSE) para obtener más detalles.
- **Descripción:** TensorFlow es una biblioteca de código abierto desarrollada por Google para el aprendizaje automático y el aprendizaje profundo. Es ampliamente utilizado en la investigación y la producción de modelos de aprendizaje automático.
- **Sitio web oficial:** [TensorFlow](https://www.tensorflow.org/)


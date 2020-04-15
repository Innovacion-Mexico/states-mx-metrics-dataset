# # Procesando varios datasets de diversas fuentes para juntarlos en uno solo
# Objetivo de salida: un dataset con en la que cada fila es una entidad federativa de México y cada columna un indicador sobre dicha entidad.
import pandas as pd
import matplotlib.pyplot as plt

# ## Empezando por los que ya estan en formato csv y tienen el mismo formato.
# Limpiando los datos inncesarios

# Archivos a constantes
DS_DIABETES = 'istabla43_2018.csv' # Detección padecimientos Diabetes por delegación, por año hasta el 2015
DS_HIPERTENSION = 'istabla45_2018.csv' # Detección de padecimientos Hipertensión arterial por delegación, por año hasta el 2015
DS_PADECIMIENTOS = 'istabla39_2018.csv' # Número total de detecciones por delegación, por año hasta el 2015

db = pd.read_csv(DS_DIABETES, encoding='latin')
# Ignorando la fila de totales y seleccionando solo las filas de estados
db = db[1:36]
# Seleccionando solo las columnas de interés
db = db[[db.columns[0], '2015', '2018']]
# Renombrando las columnas a su clave definida en el diccionario del dataset
db = db.rename(columns={
    db.columns[0] : 'EDO',
    '2015' : 'DET.DIAB.15',
    '2018' : 'DET.DIAB.18'
    })

# Resultado de procesado de DS_DIABETES
print('DS_DIABETES', db)

# Repitiendo el proceso para DS_HIPERTENSION
hp = pd.read_csv(DS_HIPERTENSION, encoding='latin')
# Ignorando la fila de totales y seleccionando solo las filas de estados
hp = hp[1:36]
# Seleccionando solo las columnas de interés
hp = hp[[hp.columns[0], '2015', '2018']]
# Renombrando las columnas a su clave definida en el diccionario del dataset
hp = hp.rename(columns={
    hp.columns[0] : 'EDO',
    '2015' : 'DET.HIPT.15',
    '2018' : 'DET.HIPT.18'
    })

# Resultado parcial de DS_HIPERTENSION
print('DS_HIPERTENSION', hp)

# Repitiendo el proceso para DS_PADECIMIENTOS
pad = pd.read_csv(DS_PADECIMIENTOS, encoding='latin')
# Ignorando la fila de totales y seleccionando solo las filas de estados
pad = pad[1:36]
# Seleccionando solo las columnas de interés
pad = pad[[pad.columns[0], '2015', '2018']]
# Renombrando las columnas a su clave definida en el diccionario del dataset
pad = pad.rename(columns={
    pad.columns[0] : 'EDO',
    '2015' : 'DET.TOT.15',
    '2018' : 'DET.TOT.18'
    })

# Resultado parcial de DS_HIPERTENSION
print('DS_HIPERTENSION', pad)

# ## Uniendo los datasets anteriores
todos = pd.merge(db, hp, on='EDO')
todos = pd.merge(todos, pad, on='EDO')

# Resultado final de esta parte
print('resultado de merges', todos)

# Removiendo espacios en blanco en la columna EDO
todos['EDO'] = todos['EDO'].str.strip()

# Haciendo que EDO sea el indice
todos = todos.set_index('EDO')

# Sumando filas de estado de mexico
todos.loc['México Oriente'] += todos.loc['México Poniente']

# Borrando la columna ya sumada
todos.drop(['México Poniente'], inplace=True)

# Renombrando la columna con la suma
todos = todos.rename(index={'México Oriente' : 'México'})

# Repitiendo el proceso para el DF
todos.loc['D.F. Norte'] += todos.loc['D.F. Sur']
todos.drop(['D.F. Sur'], inplace=True)# Renombrando la columna con la suma
todos = todos.rename(index={'D.F. Norte' : 'CIUDAD DE MÉXICO'})

# Repitiendo el proceso para el Veracruz
todos.loc['Veracruz Norte'] += todos.loc['Veracruz Sur']
todos.drop(['Veracruz Sur'], inplace=True)# Renombrando la columna con la suma
todos = todos.rename(index={'Veracruz Norte' : 'Veracruz'})

for estado in todos.index:
    todos = todos.rename(index={estado : estado.upper()})

print('Resultado de limpieza (final): ', todos)

todos.to_csv('EDO_DIAB_HIP_PAD.csv')
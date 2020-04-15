# # Procesando dataset de habitantes por estados
import pandas as pd
DS_HABITANTES = '01_poblacion.csv' # Poblacion por entidad federativa, año 2015
hab = pd.read_csv(DS_HABITANTES, encoding='latin')

# Seleccionando solo los totales de los grupos de edad
hab = hab[hab[hab.columns[1]] == 'Total']

# Seleccionando unicamente los valores
hab = hab[hab[hab.columns[2]] == 'Valor']

# Seleccionando solo las columnas de estado y de población total
hab = hab[[hab.columns[0], hab.columns[3]]]

hab = hab.rename(columns={
    hab.columns[0] : 'EDO',
    hab.columns[1] : 'POB.HAB.15'
    })

hab['EDO'] = hab['EDO'].str.strip()

# Quitando la fila del total del pais y solo conservando los estados
hab = hab[1:]

# Reseteando el indice del dataframe (consevaba los indices enormes del dataset original)
hab = hab.reset_index(drop=True)

# Removiendo numeros del inicio de cada estado
hab = hab.replace(to_replace ={'EDO' : r'^\d{2}.'}, value = {'EDO' : ''}, regex = True) 

# Poniendo en mayúsculas la columna EDO
hab['EDO'] = hab['EDO'].str.upper()

# Uniendo con dataset creado anteriormente
todos = pd.read_csv('EDO_DIAB_HIP_PAD.csv')

# Imprimiendo merge de los dos dataset sin guardar para ver que se halla hecho correctamente
todos.merge(hab, left_index=True, right_index=True)

# Guardando el merge omitiendo la columna de EDO de hab
todos.merge(hab['POB.HAB.15'], left_index=True, right_index=True)

print('Resultdo:\n', todos)

todos.to_csv('dataset_estados_con_indicadores.csv')
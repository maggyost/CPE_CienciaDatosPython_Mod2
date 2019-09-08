'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 07/09/2019
Version : 1
Author : Jaime Gomez
'''

import pandas as pd

print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')

df.round(3)
print(df.head())

print(df.tail())

print(df.info())

print(df.shape)

print(df.columns.values)

print(df.index.values)

print(df.keys())

print(type(df.columns))
print(type(df.index))


# Eliminar columnas
df.drop(['WEO Country Code', 'ISO', 'WEO Subject Code',
         'Subject Descriptor', 'Subject Notes',
         'Country/Series-specific Notes',
         'Estimates Start After'], axis=1, inplace=True)

print(df.head())

print(df.info())

print(df.keys())
print("---------------------------------")
print(df.isnull().sum())
print("---------------------------------")

# Cambiar nombre de columnas
df.rename(columns={'Country':'Pais',
                   'Units':'Unidad','Scale':'Escala'}, inplace=True)

print(df.head())

print(df.keys())


# Todas las cabeceras son cadenas
resultado = all(isinstance(column, str) for column in df.columns)
print(resultado)

df.rename(columns={'2000':2000}, inplace=True)

# Todas las cabeceras son cadenas
resultado = all(isinstance(column, str) for column in df.columns)
print(resultado)

# Convertir todas las cabeceras a cadenas
df.columns = list(map(str, df.columns))

# Todas las cabeceras son cadenas
resultado = all(isinstance(column, str) for column in df.columns)
print(resultado)

print("---------------------------------")
print(df.isnull().sum())
print("---------------------------------")
print(df.describe())

# Busqueda por paises

df.set_index('Pais', inplace=True)
print(df.head())
print ('data dimensions:', df.shape)
print('*****************************')
print(df.loc['Peru', '2010'])
print(df.loc['Peru', ['2010','2011']])
print('*****************************')
anhos = list(map(str, range(2000, 2024)))
print(anhos)
print(df.loc['Peru', anhos])
print('*****************************')

# Visualizacion de datos

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print('Matplotlib version: ', mpl.__version__ ) # >= 2.0.0
peru = df.loc['Peru', anhos]
print(peru.head())
peru.show()
#pais.show()
'''
Area Plots
'''


'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets - Array Manipulation
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np


# Loading and Saving Data in Binary Files

print("------------------------------------")
NOMBRE_ARCHIVO = 'archivo_binario.npy'
datos = np.random.random(9).reshape((3,3))
print("datos : \n",datos)

np.save(NOMBRE_ARCHIVO,datos)
datos_cargados = np.load(NOMBRE_ARCHIVO)

print("datos_cargados : \n",datos_cargados)

# Reading Files with Tabular Data

print("------------------------------------")
NOMBRE_ARCHIVO = \
    'medallero_Panamericanos_Lima2019.csv'

datos = \
    np.genfromtxt(NOMBRE_ARCHIVO, delimiter=','
                  ,names=True, dtype=None)

print(datos)

print("------------------------------------")
NOMBRE_ARCHIVO = \
    'medallero_Panamericanos_Lima2019.csv'

datos = \
    np.genfromtxt(NOMBRE_ARCHIVO, delimiter=','
                  ,names=True, dtype=None
                  ,encoding="utf-8")

print(datos)

# encode() y decode()
print("------------------------------------")
s = "Perú"
print(s.encode())
b = b'Per\xc3\xba'
print(b.decode())


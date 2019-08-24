'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets - Shape Manipulation
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

# Shape Manipulation
print("------------------------------------")

a = np.random.random(12)

a = a.reshape(3, 4)
print(type(a))
print(a.ndim)
print(a)

a = a.ravel()
print(type(a))
print(a.ndim)
print(a)

# Shape Manipulation
print("------------------------------------")

a = np.random.random(12)

a = a.reshape(3, 4)
print(type(a))
print(a.ndim)
print(a)

a = a.transpose()
print(type(a))
print(a.ndim)
print(a)
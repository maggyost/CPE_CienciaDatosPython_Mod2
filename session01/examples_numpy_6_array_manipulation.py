'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets - Array Manipulation
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

# Array Manipulation

# Joining Arrays

print("------------------------------------")

a = np.ones((3,3))
print(a)
print("    ")

b = np.zeros((3,3))
print(b)
print("    ")

# Incrementa la cantidad de filas
c = np.vstack((a,b))
print(c)
print("    ")

# Incrementa la cantidad de columnas
d = np.hstack((a,b))
print(d)

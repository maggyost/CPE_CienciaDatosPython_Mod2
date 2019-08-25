'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets - Array Manipulation
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

# General Concepts

# Joining Arrays


# References of Objects
print("------------------------------------")
a = np.array([1, 2, 3, 4])
# Se asigna una referencia
b = a

print("Antes de hacer cambios")
print("a :",a)
print("b :",b)

a[2] = 12
print("Despues de hacer cambios")
print("a :",a)
print("b :",b)

# Views of Objects
print("------------------------------------")
a = np.array([1, 2, 3, 4])
# Se crea una vista
c = a[1:3]

print("Antes de hacer cambios")
print("a :",a)
print("c :",c)

a[1] = 11

print("Despues de hacer cambios")
print("a :",a)
print("c :",c)

# Copies of Objects

print("------------------------------------")
a = np.array([1, 2, 3, 4])
# Se realiza una copia
b = a.copy()
print("Antes de hacer cambios")
print("a :",a)
print("b :",b)

a[2] = 12
print("Despues de hacer cambios")
print("a :",a)
print("b :",b)

# Vectorization


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

print("------------------------------------")
dat_1 = np.array([1,2,3])
dat_2 = np.array([4,5,6])
dat_3 = np.array([7,8,9])
print(dat_1)
print(dat_2)
print(dat_3)

# Unificar arreglos unidimensionales en columnas
col_datos \
    = np.column_stack((dat_1,dat_2,dat_3))
print(col_datos)
print("    ")

# Unificar arreglos unidimensionales en filas
filas_datos \
    = np.row_stack((dat_1,dat_2,dat_3))
print(filas_datos)

# Splitting Arrays
print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("    ")
[b,c] = np.hsplit(a,2)
print(b)
print("    ")
print(c)

print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("    ")

[b,c] = np.vsplit(a,2)
print(b)
print("    ")
print(c)

print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("    ")

[b,c,d] = np.split(a,[2,3],axis=1)
print(b)
print("    ")
print(c)
print("    ")
print(d)

print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("    ")

[b,c,d] = np.split(a,[2,3],axis=0)
print(b)
print("    ")
print(c)
print("    ")
print(d)

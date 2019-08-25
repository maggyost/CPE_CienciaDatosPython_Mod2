'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

# Basic Operations
print("------------------------------------")

# Arithmetic Operators
a_array = np.arange(4)
print(a_array)
print(a_array + 4)
print(a_array * 4)

b_array = np.arange(4,8)
print(b_array)
print(b_array + 4)
print(b_array * 4)

print("------------------------------------")
print(a_array)
print(b_array)
print("a_array + b_array \n",a_array + b_array)
print("a_array - b_array \n",a_array - b_array)
print("a_array * b_array \n",a_array * b_array)

print("------------------------------------")
print("a_array : \n",a_array)
print("a_array*5 : \n",a_array * 5)

print("------------------------------------")
c_array = a_array * np.sqrt(b_array)
print("a_array : \n",a_array)
print("b_array : \n",b_array)
print("a_array * np.sqrt(b_array) : \n", c_array)

print("------------------------------------")
a_matriz = np.arange(0,16).reshape(4,4)
b_matriz = np.ones((4,4))
c_matriz = a_matriz*b_matriz
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("a_matriz * b_matriz : \n", c_matriz)

# The Matriz Product
print("------------------------------------")
c_matriz = np.dot(a_matriz,b_matriz)
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("np.dot(a_matriz,b_matriz) : \n", c_matriz )

print("------------------------------------")
c_matriz = a_matriz.dot(b_matriz)
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("a_matriz.dot(b_matriz) : \n", c_matriz)

# Increment and Decrement Operators

print("------------------------------------")

a_matriz = np.arange(4,8)
print("a_matriz : \n",a_matriz)
a_matriz += 3
print("a_array += 3 : \n",a_matriz)
a_matriz -= 2
print("a_array -= 2 : \n",a_matriz)
a_matriz -= 5
print("a_array -= 2 : \n",a_matriz)


# Universal Functions (ufunc)
print("------------------------------------")

a_array = np.arange(4,8)
print("a_array : \n",a_array)
print("np.power(a_array,2) : \n",np.power(a_array,2))

# Aggregate Functions

print("------------------------------------")

a_array = np.arange(4,8)
print("a_array : \n",a_array)
print("a_array.sum() : ",a_array.sum())
print("a_array.min() : ",a_array.min())
print("a_array.max() : ",a_array.max())
print("a_array.mean(): ",a_array.mean())
print("a_array.std() : ",a_array.std())




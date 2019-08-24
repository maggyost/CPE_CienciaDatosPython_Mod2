'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

print("------------------------------------")

# Define listado
nro_list = [1,2,3,4,5,6]
nro_array = np.array(nro_list)

print(type(nro_array))
print("nro_array --> ",nro_array)
print("dtype --> ",nro_array.dtype)
print("ndim --> ",nro_array.ndim)
print("size --> ",nro_array.size)
print("shape --> ",nro_array.shape)

print("itemsize --> ",nro_array.itemsize)
print("data --> ",nro_array.data)

print("------------------------------------")

# Define listado
nro_list = [[1.1,2.3],[4.2,5.8]]
nro_array = np.array(nro_list)

print(type(nro_array))
print("nro_array --> ",nro_array)
print("dtype --> ",nro_array.dtype)
print("ndim --> ",nro_array.ndim)
print("size --> ",nro_array.size)
print("shape --> ",nro_array.shape)

print("itemsize --> ",nro_array.itemsize)
print("data --> ",nro_array.data)

# Create arrays
print("------------------------------------")

nro_array = np.array([[1,2,3],[4,5,6]])
print(nro_array)

nro_array = np.array(((1,2,3),(4,5,6)))
print(nro_array)

nro_array = np.array([(1,2,3),(4,5,6)])
print(nro_array)

# Tipo de datos
print("------------------------------------")

abc_array = np.array([["a","b","c"],["d","e","f"]])
print(abc_array)
print("abc_array --> ",abc_array)
print("dtype --> ",abc_array.dtype)
print("dtype.name --> ",abc_array.dtype.name)
print("size --> ",abc_array.size)
print("shape --> ",abc_array.shape)

# Intrinsic Creation of an Array
print("------------------------------------")

ceros_array = np.zeros((3,3))
print("np.zeros((3,3)) --> ",ceros_array)

unos_array = np.ones((3,3))
print("np.ones((3,3)) --> ",ceros_array)

nros_array = np.arange(8)
print("np.arange(8) --> ",nros_array)

nros_array = np.arange(3,8)
print("np.arange(3,8) --> ",nros_array)

nros_array = np.arange(1,16,3)
print("np.arange(1,16,3) --> ",nros_array)

nros_array = np.arange(0,15).reshape(5,3)
print("np.arange(0,15).reshape(5,3) --> ",nros_array)

nros_array = np.linspace(0,15,7)
print("np.linspace(0,15,7) --> ",nros_array)

nros_array = np.random.random(4)
print("np.random.random(4) --> ",nros_array)

nros_array = np.random.random((2,3))
print("np.random.random((2,3)) --> ",nros_array)
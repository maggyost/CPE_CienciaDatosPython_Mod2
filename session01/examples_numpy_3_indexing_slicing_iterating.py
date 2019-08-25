'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

import numpy as np

# Indexing
print("------------------------------------")
a_array = np.arange(0,8)
print("a_array    : \n",a_array)
print("a_array[2] : \n",a_array[2])

a_matriz = np.arange(0,8).reshape(2,4)
print("a_matriz      : \n",a_matriz)
print("a_matriz[1,1] : \n",a_matriz[1,1])

# Slicing, and Iterating
print("------------------------------------")
a_array = np.arange(0,10)
print("a_array        : ",a_array)
print("a_array[0:5]   : ",a_array[0:5])
print("a_array[0:5:2] : ",a_array[0:5:2])
print("a_array[::2]   : ",a_array[::2])
print("a_array[:5:2]  : ",a_array[:5:2])
print("a_array[:5:]   : ",a_array[:5:])
print("a_array[::3]   : ",a_array[::3])

print("------------------------------------")
a_matriz = np.arange(0,12).reshape(3,4)
print("a_matriz : \n",a_matriz)
print("a_matriz[:,0] : \n",a_matriz[:,0])
print("a_matriz[0,:] : \n",a_matriz[0,:])
print("a_matriz[0:2,0:2] : \n",
      a_matriz[0:2,0:2])
print("a_matriz[[0,2],0:2] : \n",
      a_matriz[[0,2],0:2])

# Iterating an Array
print("------------------------------------")
a_array = np.arange(0,10)
print("a_array :",a_array)
for i in a_array:
    print(i)

print("------------------------------------")
a_matriz = np.arange(0,12).reshape(3,4)
print("a_matriz : \n",a_matriz)

for row in a_matriz:
    print("row --> ",row)

for value in a_matriz.flat:
    print("value --> ",value)

# Iterating an Array
print("------------------------------------")
a_array = np.arange(0,10)
print("a_array :",a_array)
for i in a_array:
    print(i)

print("------------------------------------")
a_matriz = np.arange(0,12).reshape(3,4)
print("a_matriz : \n",a_matriz)

for row in a_matriz:
    print("row --> ",row)

for value in a_matriz.flat:
    print("value --> ",value)

print("------------------------------------")
a_matriz = np.arange(0,12).reshape(3,4)
print("a_matriz : \n",a_matriz)

# Procesa el promedio de la matriz por columna
a_m = np.apply_along_axis(np.mean,axis=0
                          ,arr=a_matriz)
print(a_m)

# Procesa el promedio de la matriz por fila
a_m = np.apply_along_axis(np.mean,axis=1,
                          arr=a_matriz)
print(a_m)

print("------------------------------------")
a_matriz = np.arange(0,12).reshape(3,4)
print("a_matriz : \n",a_matriz)

# Definamos funcion al cuadrado
def potencia(x):
    return x*x

# Procesa el promedio de la matriz por columna
a_m = np.apply_along_axis(potencia, axis=0,
                          arr=a_matriz)
print(a_m)

# Procesa el promedio de la matriz por fila
a_m = np.apply_along_axis(potencia, axis=1,
                          arr=a_matriz)
print(a_m)
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

# Array
print("------------------------------------")
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print("a   : \n",a)
print("b   : \n",b)
print("a*b : \n",c)

# Matriz
print("------------------------------------")
a = np.arange(9).reshape((3,3))
b = np.arange(8,17).reshape((3,3))
c = a*b
print("a   : \n",a)
print("b   : \n",b)
print("a*b : \n",c)

# The Matriz Product
print("------------------------------------")
a_matriz = np.arange(0,16).reshape(4,4)
b_matriz = np.ones((4,4))
c_matriz = np.dot(a_matriz,b_matriz)
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("np.dot(a_matriz,b_matriz) : \n", c_matriz )

print("------------------------------------")
a_matriz = np.arange(0,16).reshape(4,4)
b_matriz = np.ones((4,4))
c_matriz = a_matriz.dot(b_matriz)
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("a_matriz.dot(b_matriz) : \n", c_matriz)


# Broadcasting
print("------------------------------------")
A = np.arange(16).reshape(4, 4)
b = np.arange(4)
C = A + b

print("A   : \n",A)
print("b   : \n",b)
print("A+b : \n",C)

print("------------------------------------")
m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
r = m + n

print("m   : \n",m)
print("n   : \n",n)
print("m+n : \n",r)

# Structured Arrays

print("------------------------------------")
estructura \
    = np.array([(1,"Uno",0.5),
                (2,"Dos",1.5),
                (3,"Tres",2.5)])

print(estructura.dtype)
print(estructura)

'''
bytes                b1
int                  i1, i2, i4, i8
unsigned ints        u1, u2, u4, u8
floats               f2, f4, f8
complex              c8, c16
fixed length strings a<n>
'''
print("------------------------------------")
estructura \
    = np.array([(1,"Uno",0.5),
                (2,"Dos",1.5),
                (3,"Tres",2.5)],dtype=('i2,a6,f4'))

print(estructura.dtype)
print(estructura)

print("estructura[0] : ",estructura[0])
print("estructura['f0'] : ",estructura['f0'])

print("------------------------------------")
estructura \
    = np.array([(1,"Uno",0.5),
                (2,"Dos",1.5),
                (3,"Tres",2.5)],
            dtype=[('id','i2'),
                   ('orden','a6'),
                   ('valor','f4')])

print(estructura.dtype)
print(estructura.dtype.names)
print(estructura)

print("estructura[0] : ",
                estructura[0])
print("estructura['orden'] : ",
                estructura['orden'])
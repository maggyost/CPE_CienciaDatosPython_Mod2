'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Importación de Datasets
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

##########################################
# Functional Programming
##########################################

#  map() - lambda

print("------------------------------------")

'''
 Caso 1
'''

# Define listado
nro_list = [1,2,3,4,5]

# Define funcion
def inc(x):
    return x + 1

# Recorre todo el listado
for i in range(len(nro_list)):
    nro_list[i] = inc(nro_list[i])

# Muestra los resultados
print("Caso 1 :",nro_list)

'''
 Caso 2
'''

# Define listado
nro_list = [1,2,3,4,5]

# Define funcion
def inc(x): return x + 1

res_list = list(map(inc, nro_list))

print("Caso 2 :",res_list)

'''
 Caso 3
'''
# Define listado
nro_list = [1,2,3,4,5]

res_list = list(map(lambda x : x+1, nro_list))

print("Caso 3 :",res_list)


# Mapping a List of Functions

nro_list = [1,2,3,4,5]

def map_funciones(valor, funciones):
    '''Mapa de funciones'''
    res = []
    for funcion in funciones:
        res.append(funcion(valor))
    return res

funciones = [sum,min,max]

print("Resultado --> ", map_funciones(nro_list, funciones))


#  filter() - lambda

print("------------------------------------")
# Define listado
nro_list = [1,2,3,4,5]

# Obtiene los numeros que osn menores que 4
res_list = list(filter(lambda x : x < 4, nro_list))

print("filter() :",res_list)


#  reduce() - lambda

from functools import reduce

print("------------------------------------")
# Define listado
nro_list = [1,2,3,4,5]

# Calcula la suma de todos los elementos del listado
res = reduce(lambda x,y : x+y, nro_list)

print("reduce() :",res)


print("------------------------------------")

# Calcula la suma de todos los "n" primeros numeros
n = 100
res = reduce(lambda x,y : x+y, range(n + 1))

print("reduce() :",res)




# List comprehension.

print("------------------------------------")

'''
Caso 1
'''
potencias = [ n**2 for n in range(5) ]

print("Potencias --> ",potencias)

'''
Caso 2
'''

nro_list = [1,2,3,4,5]

funciones = [sum,min,max]

def map_funciones_2(valor, functiones):
    return [funcion(valor) for funcion in functiones]

print("Resultado --> ", map_funciones_2(nro_list, funciones))


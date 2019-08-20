'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Examples
Fecha : 18/08/2019
Version : 1
Author : Jaime Gomez
'''

# Functional Programming

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
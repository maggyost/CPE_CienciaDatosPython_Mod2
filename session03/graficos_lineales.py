'''

'''

import matplotlib.pyplot as plt
import numpy as np

# Los rangos de las X se definen :
LIM_INF = -10
LIM_SUP = 10
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
#print(x)

def graficos_lineales_1():
    plt.plot(x, x , label="linea 1" )
    plt.plot(x, 4*x + 20, label="linea 2")
    plt.plot(x, 8*x + 20, label="linea 3")
    plt.legend()
    plt.xlabel("Valores de X")
    plt.ylabel("Valores de Y")
    plt.title("Graficos de Lineas con Python")
    plt.xlim(4,8)
    plt.ylim(40,60)
    plt.show()
    #plt.savefig("fig-01")

def graficos_lineales_2():
    plt.plot(x, np.sin(x) , label="Funcion Sin" )
    plt.show()

def graficos_lineales_3():
    plt.plot(x, np.log10(x) , label="Funcion Log" )
    plt.show()

def graficos_lineales_4():
    plt.plot(x, mi_patron(x) , label="Mi funcion" )
    plt.show()

def mi_patron(x):
#    modelo = 3*x
#    modelo = 3*pow(x,3) + 5*pow(x,2) + 4*x + 4
    modelo = 3*x**3 + 5*x**2 + 4 * x + 4
    modelo = np.log10(x)*modelo
    return modelo

def graficos_lineales_5():
    plt.subplot(2,2,1)
    plt.plot(x, np.sin(x) ,'.c')
    plt.subplot(2,2,2)
    plt.plot(x, np.cos(x))
    plt.subplot(2,2,3)
    plt.plot(x, np.tan(x))
    plt.subplot(2,2,4)
    plt.plot(x, 1/np.tan(x))
    plt.show()

if __name__ == '__main__':
    graficos_lineales_5()

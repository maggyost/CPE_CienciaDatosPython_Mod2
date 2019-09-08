'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 07/09/2019
Version : 1
Author : Jaime Gomez
Link : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

'''
import pandas as pd

print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
anhos = list(map(str, range(2000, 2024)))


def grafico_linea_1():
    peru = df.loc['Peru', anhos]
    print(peru.head())
    peru.plot()
    plt.show()
    #plt.show(block=True)
    #plt.interactive(False)

def grafico_linea_2():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='line')
    plt.title('Perú PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_3():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='line')
    plt.title('Perú PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.text(8, 250, '2008 Crisis') # see note below
    plt.show()

def grafico_linea_4():
    paises = df.loc[['Peru','Chile'], anhos]
    print(paises.head())
    paises.plot(kind='line')
    plt.show()

def grafico_linea_5():
    paises = df.loc[['Peru','Chile'], anhos]
    paises = paises.transpose()
    print(paises.head())
    paises.plot(kind='line')
    plt.show()

def grafico_linea_6():
    paises = df.loc[['Peru','Chile'], anhos]
    paises = paises.transpose()
    print(paises.head())
    paises.plot(kind='line')
    plt.title('Perú vs Chle ')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_7():
    df.sort_values(by='2018', ascending=False, axis=0, inplace=True)
    df_top5 = df[anhos].head(5)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
    plt.title('Top 5 Paises por PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()


if __name__ == '__main__':
    grafico_linea_7()
'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 07/09/2019
Version : 1
Author : Jaime Gomez
'''
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')

df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
anhos = list(map(str, range(2000, 2024)))

def grafico_barras_1():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='bar', figsize=(10, 6))
    plt.title('Perú PBI : 2000 - 2024')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.text(8, 250, '2008 Crisis')  # see note below
    plt.show()

def grafico_barras_2():
    #df.reset_index(inplace=True)
    df_top = df.sort_values(by = '2018',  ascending=True, inplace=True)
    df_top = df['2018'].tail(10)
    print(df_top)
    df_top.plot(kind='barh', figsize=(10, 10), color='steelblue')
    plt.title('Top Country ')
    plt.xlabel('Billones de $')
    # annotate value labels to each country
    for index, value in enumerate(df_top):
        label = format(int(value), ',')  # format int with commas
        #label = value
        # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
        plt.annotate(label, xy=(value-1450, index-0.1), color='white')

    plt.show()


if __name__ == '__main__':
    grafico_barras_2()
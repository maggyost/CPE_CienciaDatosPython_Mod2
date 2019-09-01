'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Fundamentos de Estadistica
Fecha : 01/09/2019
Version : 1
Author : Jaime Gomez
'''

import pandas as pd
import numpy as np

#df = pd.read_csv("medallero_Panamericanos_Lima2019.csv", header= 0)
df = pd.read_csv("medallero_Panamericanos_Lima2019.csv")

print(df.head())

def calc_suma():
    ''' Obtiene la suma de una columna de un dataframe'''
    print(df['Oro'].sum())
    print(df.Oro.sum())
    print(np.sum(df['Oro']))
    print(np.sum(df.Oro))

def calc_nro_elementos():
    print(len(df['Oro']))
    print(len(df.Oro))
    print(df['Oro'].count())
    print(df.Oro.count())
    print(np.size(df['Oro']))
    print(np.size(df.Oro))

def calc_media():
    print( df.Oro.sum()/df.Oro.count())
    print( df.Oro.mean())
    print(np.mean(df.Oro))

def obtener_media(redondeo = 2):
    media = df.Oro.mean()
    media =  round(media,redondeo)
    return media

if __name__ == '__main__':
    #calc_suma()
    #calc_nro_elementos()
    #calc_media()
    print(obtener_media())
    print(obtener_media(redondeo = 4))
    print(df.Oro.mean())
    print(df.mean())
    print(round(df.mean(),2))
    print(type(df.mean()))

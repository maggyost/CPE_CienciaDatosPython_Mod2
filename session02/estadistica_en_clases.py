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
print(df)
#print(df.head())

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

def obtener_mediana():

    nro_item = np.size(df.Oro)
    pos_mediana = round(nro_item / 2)
    print("posicion mediana = ",pos_mediana)
    mediana = df.Oro[pos_mediana-1]

#    mediana =  np.median(df.Oro)

#    mediana = df.Oro.median()

    return mediana


def obtener_moda():

    moda = df.Oro.mode()
    return moda

# Percentiles
def cal_percentiles():
    print("---------------------------------")
    tramos = [25,50,75]
    percentiles = np.percentile(df['Oro'],tramos)
    print("percentiles = ", percentiles )

# Grafico Percentiles
def graph_percentiles():
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.boxplot(y="Oro", data= df)
    plt.show()

# Varianza
def cal_varianza():

#    print(type(df['Oro'] ))
#    print(type(df[['Oro']] ))

    diff = df['Oro'] - df['Oro'].mean()
    print(type(diff))
    diff2 = np.power(diff,2)
    print(type(diff2))
    nro_item = np.size(df['Oro'])
    print("diff2.sum() = ", diff2.sum())
    var_manual = (diff2.sum()/nro_item)  #['Oro']
    print("type(var_manual) = ", type(var_manual))
    print("varianza manual = ", var_manual)

    var = df['Oro'].var(ddof=0)  # corrección de Bessel
    print("varianza = ", var)
    print("varianza = ", np.var(df['Oro']))

# Varianza
def cal_varianza_2():
    diff = df['Oro'] - df['Oro'].mean()
    diff2 = np.power(diff,2)
    nro_item = np.size(df['Oro'])
    var_manual = (diff2.sum()/nro_item)
    print("type(var_manual) = ", type(var_manual))
    print("varianza manual = ", var_manual)

    var = df['Oro'].var(ddof=0)  # corrección de Bessel
    print("varianza = ", var)
    print("varianza = ", np.var(df['Oro']))

if __name__ == '__main__':
    #calc_suma()
    #calc_nro_elementos()
    #calc_media()
    '''
    print(obtener_media())
    print(obtener_media(redondeo = 4))
    print(df.Oro.mean())
    print(df.mean())
    print(round(df.mean(),2))
    print(type(df.mean()))
    '''
    '''
    print(obtener_mediana())

    print("------------")
    print(np.sort(df.Plata)[16-1])
    print(df.Plata.median())

    print("------------")
    print(np.sort(df.Bronce)[16-1])
    print(df.Bronce.median())
    '''
    '''
    print(obtener_moda())
    print(df.Oro.value_counts())
    cal_percentiles()
    graph_percentiles()
    '''
    cal_varianza_2()
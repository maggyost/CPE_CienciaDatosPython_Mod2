'''

'''
import pandas as pd
import numpy as np
import scipy.stats as ss

# Media
print("---------------------------------")
NOMBRE_ARCHIVO \
    = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(NOMBRE_ARCHIVO)
print(df.head())
#print(df['Oro'])

# Media
def cal_media():
    print("---------------------------------")
    mean = df['Oro'].mean()
    sumatoria = np.sum(df['Oro'])
    nro_item = np.size(df['Oro'])
    print("sumatoria ,", sumatoria)
    print("elementos ,", nro_item)
    print("media manual = ", sumatoria/nro_item)
    print("media = ", mean)

# Outliers
def cal_outliers():
    print("---------------------------------")
    print("mayor valor = ", df['Oro'].max())
    print("menor valor = ", df['Oro'].min())

# Mediana
def cal_mediana():
    print("---------------------------------")
    mediana = df['Oro'].median()
    nro_item = np.size(df['Oro'])
    pos_mediana = round(nro_item/2)
    print("pos_mediana = ", pos_mediana)
    print("mediana manual = ",
          df['Oro'][pos_mediana-1])
    print("mediana = ", mediana)

# Mode
def cal_mode():
    print("---------------------------------")
    print(df['Oro'].value_counts())
    mode = df['Oro'].mode()
    print("moda = " , mode)

# Coeficiente de correlacion
def cal_correlacion():
    print("---------------------------------")
    print(df.corr().head())

# Percentiles
def cal_percentiles():
    print("---------------------------------")
    tramos = [25,50,75]
    percentiles = np.percentile(df['Oro'],tramos)
    print("percentiles = ", percentiles )

# Percentiles
def cal_percentiles_2():
    print("---------------------------------")
    tramos = [25,50,75]
    percentiles = df['Oro'].quantile(0.50)
    print("percentiles = ", percentiles )

# Grafico Percentiles
def graph_percentiles():
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.boxplot(y="Oro", data= df)
    plt.show()


# Grafico Percentiles
def graph_percentiles_2():
    import matplotlib.pyplot as plt
    red_square = dict(markerfacecolor='r', marker='s')
    fig1, ax1 = plt.subplots()
    ax1.set_title('Mi primer Boxplot')
    ax1.boxplot(df['Oro'], flierprops=red_square)

# Grafico Paises x Medalla de Oro
def graph_paises_med_oro():
    import matplotlib.pyplot as plt
    import seaborn as sns
    _ = sns.boxplot(x="Oro", y ="Pais", data= df)
    plt.show()

# Varianza
def cal_varianza():
    diff = df[['Oro']] - df['Oro'].mean()
    print(type(diff))
    diff2 = np.power(diff,2)
    print(type(diff2))
    nro_item = np.size(df['Oro'])
    var_manual = (diff2.sum()/nro_item)['Oro']
    #print(type(var_manual))
    print("varianza manual = ", var_manual)

    var = df['Oro'].var(ddof=0)  # corrección de Bessel
    print("varianza = ", var)
    print("varianza = ", np.var(df['Oro']))

# Desviacion Estandar
def cal_desviacion_estandar():
    std_manual = np.sqrt(df['Oro'].var(ddof=0)) # corrección de Bessel
    print("desviacion estandar manual = ", std_manual)
    std = df['Oro'].std(ddof=0) # corrección de Bessel
    print("desviacion estandar = ", std)


if __name__ == '__main__':
    #print(df.Oro.describe())
    #cal_correlacion()
    graph_percentiles()
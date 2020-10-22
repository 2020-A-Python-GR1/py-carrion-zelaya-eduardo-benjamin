#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#g_iloc_loc.py

import pandas as pd

path_guardado = "data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc

filtrado_horizontal = df.loc[1035] #Serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indice columnas 

serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index) # Indice son los indices

#Filtrado por indice

df_1035 = df[df.index == 1035] #Filtrar por indice (1)

segundo = df.loc[[1035, 1036]] #Filtrar por arr indice
segundo = df.loc[3:5] # Filtrado desde X indice hasta Y indice
segundo = df.loc[df.index == 1035] # Filtrar por
                                   # Arreglo -> True False


segundo = df.loc[1035, 'artist']
segundo = df.loc[1035, ['artist','medium']] #Varios indices

#print(df.loc[0]) # Indice dentro del DataFrame
#print(df[0])#Indice dentro del DataFrame

#iloc -> acceder grupo filas y columnas indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]


tercero = df.iloc[0:10, 0:4] #Filtrado indices por rango de indices 0:4

###############

datos = {
    "nota 1":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9
        },
    "nota 2":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9
        },
    "disciplina":{
        "Pepito":4,
        "Juanita":9,
        "Maria":2
        }
    }

notas = pd.DataFrame(datos)


condicion_nota = notas["nota 1"] <= 7
condicion_nota_dos = notas["nota 2"] <= 7
condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota,["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]


notas.loc["Maria", "disciplina"] = 7

notas.loc[:, "disciplina"] = 7

######## Promedio de las 3 notas (no1 + no2 + disc) /3



#nota_1_mean = notas.loc[:,"nota 1"].mean()
#nota_2_mean = notas.loc[:,"nota 2"].mean()
#disiciplina_mean = notas.loc[:,"disciplina"].mean()


#mean_total = (nota_1_mean + nota_2_mean + disiciplina_mean) / 3



notas["promedio"] = (notas.loc[:,"nota 1"] + notas.loc[:,"nota 2"] + notas.loc[:,"disciplina"])/3












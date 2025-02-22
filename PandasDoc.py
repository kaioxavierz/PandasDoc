import pandas as pd
import numpy as np
import json
# Estrutura do pandas DataFrame
# pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
# DataFrame.[info(), diff(), aggregate(), abs(), corr(), describe(), explode, astype, head()]
 
#Primeiro DataBase: Padrões basicos parametros do metodo DataFrame
columns = ["a", "b", "AeB"]
dataset =  [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]
]
ordf = pd.DataFrame(dataset, columns = columns)
print("Primeiro DataFrame:")
print(ordf, ordf.info())


# Segundo DataBase: Utilizando metodos do numpy
data = np.array(
    [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
    dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")]
    )
df1 = pd.DataFrame(data)
print("Segundo DataFrame:")
print(df1)


# Terceiro DataBase: Utilizando Json
json_array = [ {'a':1,'b':2}, {'a':3,'b':4}, {'a':5,'b':6} ]
df = pd.DataFrame(json_array)
#(dados.to_json, excel, xml, csv...)
df.to_json('saves/arquivo.json')
df.to_excel("saves/arquivo3.xlsx")
print("Terceiro DataFrame")
print(df, df.describe())


# Quarto DataBase: Dicionarios com utilização de agrupamento pela coluna animal e calcula média.
dados = pd.DataFrame({'Animal': ['falcon', 'falcon', 'Parrot', 'Parrot'],
                      'Max_Speed': [380., 370., 24., 26.]}
                    )
agrupamento = dados.groupby(['Animal'])
print(agrupamento.mean(), dados) 

print("Buscando dados")
print(dados.iloc[0])

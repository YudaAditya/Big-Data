import pandas as pd
import csv

dataa = pd.read_csv('data.txt', sep=",", header=None, names=["url", "akronim", "skor"])


# print(dataa[dataa['skor'].isnull()])
dataa['skor'] = pd.to_numeric(dataa['skor'], errors='coerce')
dataa = dataa.dropna(subset=['skor'])
dataa['skor'] = dataa['skor'].astype(float)

dataa = dataa.where(dataa['skor'] >= 0.92)
# dropping null value columns to avoid errors 
dataa.dropna(inplace = True) 

dataa = pd.concat(g for _, g in dataa.groupby("akronim") if len(g) > 1)

dataa = dataa.sort_values(by=['skor'])

print(dataa)

lala = dataa.groupby('akronim', 'skor')['url'].apply('::'.join).reset_index().head(1)

print(lala)

export_csv = lala.to_csv (r'lala.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

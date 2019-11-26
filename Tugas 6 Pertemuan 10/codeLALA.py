import pandas as pd
import numpy as np
# import cufflinks as cf
import plotly as py
import gzip
import json
import matplotlib.pyplot as plt
import pdb


def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('meta_All_Beauty.json.gz')

new = df["rank"].str.split("i", n = 1, expand = True) 

# making separate first name column from new data frame 
df["salesRank"]= new[0] 
  
# making separate last name column from new data frame 
df["gabutuh"]= new[1] 
  
# Dropping old Name columns 
df.drop(columns =["rank"], inplace = True) 

df['salesRank'] = df['salesRank'].str.replace(',', '')

# print(df[df['salesRank'].isnull()])
df['salesRank'] = pd.to_numeric(df['salesRank'], errors='coerce')
df = df.dropna(subset=['salesRank'])
df['salesRank'] = df['salesRank'].astype(int)

df[['brand', 'salesRank']]
df.sort_values(by=['salesRank'], inplace=True)

# dropping ALL duplicte values 
df.drop_duplicates(subset ="brand", 
                     keep = 'first', inplace = True) 

print(df)


df1=df[:20] #nampilin berapa yang mo ditampilin
grafik = df1.plot('brand',['salesRank'],kind = 'bar')
plt.show(grafik)
# pd.show(aa)

# ala = df['salesRank'].head(3)
# print(ala)



# kol.plot()
# plt.show()


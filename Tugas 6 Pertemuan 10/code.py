import pandas as pd
import gzip
import json
# import plotly.graph_objs
# import plotly.offline as py
# import cufflinks as cf
# import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


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


df = getDF('Software_5.json.gz')
# print(df[['reviewText','overall','summary','reviewTime']])
# print(df[['overall','reviewTime']])

new = df["reviewTime"].str.split(", ", n=1, expand=True)

df["time"] = new[0]

df["year"] = new[1]

time = df["time"].str.split(" ", n=1, expand=True)

df["month"] = time[0]

df["date"] = time[1]

# df["overall"]=df["overall"].astype(str)

df["month"] = df["month"].astype(int)

df["date"] = df["date"].astype(int)

df.drop(columns=["verified","reviewTime","reviewerID","asin","style","vote","image","reviewerName","reviewText","summary","unixReviewTime","time"], inplace=True)

# df["time"]=df["time"].replace(" ", ":", regex=True)

tahun = df["year"].unique()
bulan = df["month"].unique()
overall = df["overall"].unique()
get_tahun ="2016"
df2016 = df[df["year"]=="2016"]
df2016.sort_values(by=['month'], inplace=True)
# df2016 = df.loc[(df["year"]=="2016")& df["month"]==1]
# print(tahun)
print(df2016)
# print(df["overall"])



df1=df2016[:10]
df1.plot("month","overall",kind='bar')

# plt.scatter(df['month'],df['overall
# df.groupby(['year']).boxplot(fontsize=20, rot=90,
#                                 figsize=(20, 10), patch_artist=True)

plt.show()

# py.offline.plot(
#   {
#     'data': [
#       {
#         'x': df[df['year']==tahun1]['hour'],
#         'y': df[df['year']==tahun1]['overall'],
#         'name':tahun1, 'mode': 'markers',
#       } for tahun1 in tahun
#     ],
#     'layout':{
#         'xaxis': {'title': "Waktu"},
#         'yaxis': {'title': "Rating"}
#     }
#   }, filename='cufflinks/scatter-group-by'
# )

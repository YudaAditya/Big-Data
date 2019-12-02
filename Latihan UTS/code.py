import re
import pandas as pd
import matplotlib.pyplot as plt


# data = open("data.txt").read()
data = pd.read_csv('data.txt', sep=",", header=None,
                   names=["url", "akronim", "skor"])
# data = re.sub("[][]","",str(data))
kamus = []
datas = {}
values = 1
# data['url'] =  [re.sub(r"[[]]",'', str(x)) for x in data['url']]
# url = data['url'].unique()
# akronim = data['akronim'].unique()
data['url'] = data['url'].str.replace('[', '')
data['skor'] = data['skor'].str.replace(']', '')
data['skor'] = pd.to_numeric(data['skor'], errors='coerce')
data1 = data.loc[data['skor'] > 0.9]
# data1 = data1.sort_values('skor',inplace=True)
url = data1['url'].unique()
akronim = data1['akronim'].unique()
new = data1["akronim"].str.split("=>", n=1, expand=True)
data1['akro']=new[0]
data1['etendakro']=new[1]
# group =data1.groupby('akronim')['url'].groups
# print(group)

# for x in group:
#     print(x)
df1 = data1['akronim']+" , "+str(data1['skor'])+" , "+data1['url']
# print(df1)
# cari = data1.loc[data1['url'].isin(x)]
# count=+1
# print(count)

# print(data1[cari])
# cari = data1.loc[data1['url'].isin(url)]
# # cari = data1.where()

# cari = data1.groupby(['url','akronim']).cumcount()
# df1= data1.set_index(['url','akronim', cari]).unstack().sort_index(level=1, axis=1)
# df1.columns=[f'{x}{y}' for x, y in df1.columns]
# df1 = df1.reset_index()

# print(url,akronim)

for x in url:
    kamus.append(x)
# print(kamus)

#     print(kamus)df1= data1[data1['url'].notnull() & (data1['akronim'])]
# print(data1)
df1 = data1[:20]  # nampilin berapa yang mo ditampilin
grafik = df1.plot('akronim', ['skor'], kind='bar')
plt.show(grafik)


def clean_data(text):
    text = re.sub("[][]", "", text)
    return text


for line in kamus:
    if line not in datas:
        datas[line] = values
    elif line in datas:
        datas[line] = values+1
#     kamus=clean_data(line)
# print(datas)
group = data1.groupby('akronim','skor')['url'].apply('::'.join).reset_index()
print(group)
#     # kamus=re.findall("\s\d.+",line)
#     for term in kamus.split("\n ") :
#         datas['url']=term
#         datas['akronim']=term
#         datas['skor']=term
#     #     datas['akronim']=akronim
#     #     data['skor']=skor
#         print(datas)

# print(datas)
# print(kamus)

# print(data)

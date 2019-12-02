import pandas as pd
import re
import matplotlib.pyplot as plt


data = pd.read_csv('data.txt', sep=",", header=None,
                   names=["url", "akronim", "skor"])
data['url'] = data['url'].str.replace('[', '')
data['skor'] = data['skor'].str.replace(']', '')

data['skor'] = pd.to_numeric(data['skor'], errors='coerce')
data = data.dropna(subset=['skor'])
data['skor'] = data['skor'].astype(float)

data = data.loc[data['skor'] >= 0.92]

data.dropna(inplace=True)

data = pd.concat(g for _, g in data.groupby("akronim") if len(g) > 1)

data['hitung'] = data.groupby(["akronim", "skor"])['url'].transform('count')

hasil = data.groupby(['akronim', 'skor', "hitung"])[
    'url'].apply('::'.join).reset_index()
hasil = hasil.sort_values(by=['hitung'], ascending=False)
# print(hasil)

# print to file
export_csv = hasil.to_csv(r'hasil.txt', index=None, header=True)

# pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,0.9,0.9])
ax.axis('equal')
df = hasil[:15]
colors = ["#8F9BFF", "#82A8E8", "#9CDBFF",
          "#82DDE8", "#8FFFEC", "#FFAD80", "#E88D74", "#FF938C", "#E87494", "#FF80E2", "#FFFB80", "#CBE874", "#BAFF8B", "#7AE874", "#80FF9E"]

ax.pie(df['hitung'], labels=df['akronim'],
        colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.title("top 15 akronim dalam situs website")
plt.show()

import nltk
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re

# lala = open('contoh.txt').read().strip().split('\n')


# Definisikan sentence
sentence = open('detik/detik- 1.html').read()

print(sentence)
# hapus stopword
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
stop = stopword.remove(sentence)

# Definisikan regex
ps = '\w+'

# Mencari semua kata di sentence yang cocok dengan regex kemudian cetak
tokens = re.findall(ps, stop)

# Menginisialisasi ke dalam list
words = []

# Loop dari list tokens dan buat huruf kecil/lower case
for word in tokens:
    words.append(word.lower())
    # print(word)

kata = nltk.word_tokenize(words)
print(kata)
import matplotlib.pyplot as plt

# Buat frekuensi distribusi dan plot 10 kata dalam 2000 file
freqdist1 = nltk.FreqDist(words)
freqdist1.plot(10)






import nltk
import re

kata = open("hasil/2018/07/01/detik- 1.txt").read()

def clr_str(text) :
    text = re.sub("\."," ", text)
    text = re.sub("\?"," ", text)
    text = re.sub("-"," ", text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub("[:,!/'\"]", " ", text)
    text = re.sub("[0-9]", " ", text)
    text = re.sub("\s+"," ", text)
    text = re.sub("\s+$","", text)
    text = re.sub("^\s+","", text)
    text = text.lower()
    return text

kamus_semua={}

title = re.findall(r'<title>(.*?)</title>', kata)
content = re.findall(r'<content>(.*?)</content>', kata)
title = clr_str(title[0])
content = clr_str(content[0])

text = title+" "+content
kata = text.split(" ")
for word in kata:
    if word in (kamus_semua):
        kamus_semua[word]+=1
    else:
        kamus_semua[word]=1

f =open("freq.txt","w+")
for x in sorted(kamus_semua.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
    f.write(x[0]+"\t"+str(x[1])+"\n")
f.close
    
import sys
import re
import subprocess
# from nltk.util import ngrams

#Argumen check
if len(sys.argv) !=4 :
    print ("\n\nPenggunaan\n\tword-count.py [pathClean] [PathOutput] [stopword]\n")
    sys.exit(1)

#load argumen
source = sys.argv[1]
output = sys.argv[2]
sp = open(sys.argv[3]).read()

#load stopword
stopword = {}
for x in sp.split("\n") :
    stopword[x]=1

#def clean str
def clean_str(text) :
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

#dictionary global
dict_all = {}

#get list file from source
list_file = str(subprocess.getoutput("ls "+source+" -v"))

for list in list_file.split("\n") :
    #dictionary each date
    dict_date = {}
    data = str(subprocess.getoutput("ls "+source+"/"+list+" -v"))
    for file in data.split("\n") :
        isi = open(source+"/"+list+"/"+file).read()
        title = re.findall(r'<title>(.*?)</title>', isi)
        content = re.findall(r'<content>(.*?)</content>', isi)
        title = clean_str(title[0])
        content = clean_str(content[0])

        #get word
        text = title+" "+content
        words = text.split(" ")
        for word in words :
            if word in stopword :
                continue

            if word in (dict_date) :
                dict_date[word]+=1
            else :
                dict_date[word]=1

            if word in (dict_all):
                dict_all[word]+=1
            else:
                dict_all[word]=1

    #make file for each date
    freq = open(output+"/freq-"+list+".txt", "w+")
    print("Created : freq-"+list+".txt")
    for x in sorted(dict_date.items(), key = lambda kv:(kv[1], kv[0]), reverse=True) :
        freq.write(x[0]+"\t"+str(x[1])+"\n")
    freq.close

    #clear after write    
    dict_date.clear()


#make file output to all file
ou = open(output+"/freq-all.txt", "w+")
print("Created : freq-all.txt")
for x in sorted(dict_all.items(), key = lambda kv:(kv[1], kv[0]), reverse=True) :
    ou.write(x[0]+"\t"+str(x[1])+"\n")
ou.close    

        
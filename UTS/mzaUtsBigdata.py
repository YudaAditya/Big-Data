#  Muammar Zikri Aksana
#  1608107010045
#  UTS BIGDATA

import sys
import re
import os
from collections import OrderedDict
import matplotlib
from matplotlib import pyplot as plt



data={}
program={}
counter=1

def orderDict(data):
   return OrderedDict(sorted(data.items(), key=lambda kv: kv[1]['support'], reverse=True))

def makeData():
    srcdata=os.popen('cat '+str(program['--data'])).read()
    srcdata=srcdata.split("\n")
    for row in srcdata :
        rowData=spliteDataRow(row)

def spliteDataRow(line):
    rowLineData=[x.strip(' ') for x in line[1:-1].split(",")]
    dataValid(rowLineData)

def dataValid(rowLineData):
    global data
    global counter
    if len(rowLineData)!=3:
        return

    acroExpn=rowLineData[1].split("=>")
    if len(acroExpn)<2:
        return

    acronymExpansion=acroExpn[0]+"=>"+acroExpn[1]
    if acronymExpansion in data:
        if data[acronymExpansion]['skor']<float(rowLineData[2]):
            data[acronymExpansion]['skor']=float(rowLineData[2])

        if rowLineData[0] in data[acronymExpansion]['URLs']:
            data[acronymExpansion]['URLs'][rowLineData[0]]+=1
        else:
            data[acronymExpansion]['URLs'][rowLineData[0]]=1
            data[acronymExpansion]['support']+=1
    else:
        if (float(rowLineData[2])<0.9):
            return
        data[acronymExpansion]={
            'skor':float(rowLineData[2]),
            'support':1,
            'URLs':{
                rowLineData[0]:1
            }
        }
        counter+=1

def visual(size):
    global data
    labels = []
    data_grafik=[]
    counter=1
    for key in data:
        if(counter>size):
            break
        labels.append(key)
        data_grafik.append(data[key]['support'])
        counter+=1

    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered
    xs = [i + 0.5 for i, _ in enumerate(labels)]
    # plot bars with left x-coordinates [xs], heights [num_oscars]
    r=0.2
    b=0.4
    g=0.6
    plt.rcParams["figure.figsize"] = (13, 9)
    plt.xticks(rotation=30,ha='right')
    plt.bar(xs, data_grafik,color=(r,g,b))
    plt.ylabel("# Counts")
    plt.xlabel("# Words")
    plt.title("Words Rank")
    plt.subplots_adjust(bottom= 0.3)

    # label x-axis with movie names at bar centers

    plt.xticks([i + 0.5 for i, _ in enumerate(labels)], labels)
    # plt.legend(labels)
    # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def writeData(dstFileSave):
    file=open(dstFileSave,"w+")

    for key in data:
        line=key+","+str(data[key]['skor'])+","+str(data[key]['support'])+","
        for url in data[key]['URLs']:
            line+=url+"::"
        file.write(line[:-2]+"\n")
    file.close()
    print("saveFile",dstFileSave)

def main():
        global program
        global data
        counter=1
        # for get cmd with -flag
        for cmd in sys.argv[1:]:
            if(cmd[:1]=='-' and counter+1<len(sys.argv)):
                program[cmd]=sys.argv[counter+1]
            counter+=1

        print(program)
        for i in ['--data','--save','--top']:
            if(i not in program):
                print("please set value for run mode: ... --data path/data.txt --save path/savefile.txt --top top-rank")
                print("ex : ... --data path/data.txt --save path/savefile.txt --top 10")
                return
        makeData()
        data=orderDict(data)
        visual(int(program['--top']))
        writeData(program['--save'])
main()

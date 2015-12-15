__author__ = 'YiHao'
import os
import csv
import re
from textblob import TextBlob
import string
from nltk.corpus import stopwords
import pickle
from collections import Counter

def csvReader(fileName):
    cr = csv.reader(open(fileName,'r'))
    skipHeader = next(cr,None)
    return cr

bizNameSet = set()
stops = stopwords.words('english')
stops.append("n't")
stops.append('one')
stops.append("really")
stops.append('ve')
stops.append('get')
stops.append('went')
stops.append('would')
stops.append('go')
stops.append('m')
stops.append('could')
stops.append('never')
stops.append('could')
stops.append('de')
stops.append("'s")
stops.append('')
stops.append('de')
stops.append('4')
stops.append("'ve")
stops.append("give")
stops.append("tried")
stops.append("even")
stops.append("place")
stops.append("back")
stops.append("know")
stops.append("ordered")
#stops.append("6.99")
stops.append("across")
stops.append("ca")
stops.append("food..but")
stops.append("'")
stops.append("due")
stops.append("ready")
stops.append("able")
stops.append("fact")
stops.append("n")
stops.append("ish")
stops.append("")
stops.append("v-8")
stops.append("a-1")

def dictSplit():
    dictReview = {}
    imptInfo = {}
    bizIDinfo = {}
    cw = csvWriter("../Tableau Data/tableau_db_2_final.csv")
    #headers0 = ["Business_Id","Business_Name","Business_Category","State","City","Neigh","Neigh1","Neigh2","Lat","Lon","Rating","Price_Range","Num_Review","Word","WordCount","Adj","AdjPolarity","AdjCount","Noun","NounCount"]
    #cw.writerow(headers0)
    cr1 = csvReader("../Data/<=2stars.csv")
    #cr1 = csvReader("../Data/>-2.5<=3.5.csv")
    #cr1 = csvReader("../Data/>=4stars.csv")
    for r in cr1:
        if len(r) > 0:
            bizName = r[0].split("|")[1]
            bizID = r[0].split("|")[0]
            info = r[0].split("|")[2:14]
            text = r[0].split("|")[14]
            if bizName not in bizIDinfo:
                bizIDinfo[bizName] = bizID
            if bizName not in dictReview:
                dictReview[bizName] = " ";
            else:
                dictReview[bizName] += text + " ";
            if bizName not in imptInfo:
                imptInfo[bizName] = info
                #print info[0]

    for k in dictReview:
        blob = TextBlob(dictReview[k])
        textArray = []
        adjArray = []
        nounArray = []
        for word,pos in blob.tags:
            if word not in stops:
                textArray.append(word)
            if word not in stops and pos == 'JJ':
                adjArray.append(word)
            if word not in stops and pos == "NN":
                nounArray.append(word)

        wordCount = Counter(textArray)
        wordOutput = wordCount.most_common(20)
        nounCount = Counter(nounArray)
        nounOutput = nounCount.most_common(20)
        adjCount = Counter(adjArray)
        adjOutput = adjCount.most_common(20)
        for i in range(0,20):
            try:
                first = [bizIDinfo[k],k,imptInfo[k][0],imptInfo[k][1],imptInfo[k][2],imptInfo[k][3],imptInfo[k][4],imptInfo[k][5],imptInfo[k][6],imptInfo[k][7],"<=2stars",imptInfo[k][10],imptInfo[k][11],wordOutput[i][0],wordOutput[i][1]]

            except IndexError:
                #print k
                first = [bizIDinfo[k],k,imptInfo[k][0],imptInfo[k][1],imptInfo[k][2],imptInfo[k][3],imptInfo[k][4],imptInfo[k][5],imptInfo[k][6],imptInfo[k][7],"<=2stars",imptInfo[k][10],imptInfo[k][11],"NA",0]
            try:
                 print adjOutput[i][0]
                 blob = TextBlob(adjOutput[i][0])
                 if blob.polarity < 0:
                     pol = "neg"
                 elif blob.polarity > 0:
                    pol = "pos"
                 else:
                    pol = "neu"
                 second = [adjOutput[i][0],pol,adjOutput[i][1]]
            except IndexError:
                 second = ["NA","NA",0]
            try:
                 third = [nounOutput[i][0],nounOutput[i][1]]
            except IndexError:
                third = ["NA",0]

            first.extend(second);
            first.extend(third);
            cw.writerow(first);

dictSplit()






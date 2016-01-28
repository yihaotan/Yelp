__author__ = 'YiHao'

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

def initialiseInputStr(textReviewArray):
    inputStr = " ".join(textReviewArray)
    return repr(inputStr)

def initialiseTextBlob(inputStr,cl):
    blob = TextBlob(inputStr,cl)
    return blob

def csvWriter(fileName):
    cw = csv.writer(open(fileName, "a"), delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')
    return cw

def excludeFunction(regex,rep,string):
    string = re.sub(regex,rep,string)
    return string

def loadClassifier():
    f = open('my_classifier.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def splitByStateCategory(state,cat):
    cr = csvReader("../Data/data.csv")
    doc = []
    headers0 = ["Business_ID","Business_Name","Business_Category","State","City","Neigh","Neigh1","Neigh2","Lat","Lon","Rating","Date","Price_Range","Num_Review","Text_Review"]
    fileOutputName = state+"_"+cat+".csv"
    cw = csvWriter(fileOutputName)
    cw.writerow(headers0)

    for row in cr:
        try:
            info = []
            allCat = []
            bizId = row[1]
            bizName = row[34]
            bizCat1 = row[12]
            bizCat2 = row[13]
            bizCat3 = row[14]
            bizCat4 = row[15]
            bizCat5 = row[16]
            bizCat6 = row[17]
            bizCat7 = row[18]
            bizCat8 = row[19]
            bizCat9 = row[20]
            bizCat10 = row[21]
            bizCat11 = row[22]
            bizState = row[51]
            bizCity = row[73]
            bizNeigh = row[111]
            bizNeigh1 = row[112]
            bizNeigh2 = row[113]
            lat = float(row[23])
            lon = float(row[86])
            bizRating = float(row[77])
            date  = row[125]
            priceRange = row[84]
            numReview = int(row[49])
            text = row[121].lower()
            text = excludeFunction(r'\\n'," ",text) #remove \n
            text = excludeFunction(r'\\r'," ",text) #remove \r
            text = excludeFunction(r'\\'," ",text) #remove \
            text = excludeFunction(r'<[^>]+>'," ",text) #remove # HTML tags
            text = excludeFunction( r'(?:@[\w_]+)'," ",text) #remove @
            text = excludeFunction(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'," ",text) #remove html function
            text = excludeFunction(r'\s\s+',' ',text) #remove multi space"""
            text = text.lstrip() #left trim
            text = text.rstrip() #right trim
            info.append(bizId)
            info.append(bizName)
            allCat.append(bizCat1)
            allCat.append(bizCat2)
            allCat.append(bizCat3)
            allCat.append(bizCat4)
            allCat.append(bizCat5)
            allCat.append(bizCat6)
            allCat.append(bizCat7)
            allCat.append(bizCat8)
            allCat.append(bizCat9)
            allCat.append(bizCat10)
            allCat.append(bizCat11)
            if cat == 'Desserts':
                if 'Desserts' or 'Ice Cream & Frozen Yogurt' in allCat:
                    info.append('Desserts')
            elif cat in allCat:
                info.append(cat)
            info.append(bizState)
            info.append(bizCity)
            info.append(bizNeigh)
            info.append(bizNeigh1)
            info.append(bizNeigh2)
            info.append(lat)
            info.append(lon)
            info.append(bizRating)
            info.append(date)
            info.append(priceRange)
            info.append(numReview)
            info.append(text)
            doc.append(info)
        except IndexError:
            pass

    for d in doc:
        if cat in d and d[3] == state:
            cw.writerow(d)


def splitByStateCategoryRating(state,cat,ratingGroup):
    cr = csvReader("../Data/data.csv")
    doc = []
    for row in cr:
        try:
            info = []
            allCat = []
            bizId = row[1]
            bizName = row[34]
            bizName = bizName.replace(","," ");
            bizCat1 = row[12]
            bizCat2 = row[13]
            bizCat3 = row[14]
            bizCat4 = row[15]
            bizCat5 = row[16]
            bizCat6 = row[17]
            bizCat7 = row[18]
            bizCat8 = row[19]
            bizCat9 = row[20]
            bizCat10 = row[21]
            bizCat11 = row[22]
            bizState = row[51]
            bizCity = row[73]
            bizNeigh = row[111]
            bizNeigh1 = row[112]
            bizNeigh2 = row[113]
            lat = float(row[23])
            lon = float(row[86])
            bizRating = float(row[77])
            date  = row[125]
            priceRange = row[84]
            numReview = int(row[49])
            text = row[121].lower()
            text = excludeFunction(r'\\n'," ",text) #remove \n
            text = excludeFunction(r'\\r'," ",text) #remove \r
            text = excludeFunction(r'\\'," ",text) #remove \
            text = excludeFunction(r'<[^>]+>'," ",text) #remove # HTML tags
            text = excludeFunction( r'(?:@[\w_]+)'," ",text) #remove @
            text = excludeFunction(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'," ",text) #remove html function
            text = excludeFunction(r'\s\s+',' ',text) #remove multi space"""
            text = text.lstrip() #left trim
            text = text.rstrip() #right trim
            info.append(bizId)
            info.append(bizName)
            allCat.append(bizCat1)
            allCat.append(bizCat2)
            allCat.append(bizCat3)
            allCat.append(bizCat4)
            allCat.append(bizCat5)
            allCat.append(bizCat6)
            allCat.append(bizCat7)
            allCat.append(bizCat8)
            allCat.append(bizCat9)
            allCat.append(bizCat10)
            allCat.append(bizCat11)
            if cat == 'Desserts':
                if 'Desserts' or 'Ice Cream & Frozen Yogurt' in allCat:
                    info.append('Desserts')
            elif cat in allCat:
                info.append(cat)
            info.append(bizState)
            info.append(bizCity)
            info.append(bizNeigh)
            info.append(bizNeigh1)
            info.append(bizNeigh2)
            info.append(lat)
            info.append(lon)
            info.append(bizRating)
            info.append(date)
            info.append(priceRange)
            info.append(numReview)
            info.append(text)
            doc.append(info)
        except IndexError:
            pass

    headers0 = ["Business_ID","Business_Name","Business_Category","State","City","Neigh","Neigh1","Neigh2","Lat","Lon","Rating","Date","Price_Range","Num_Review","Text_Review"]
    ratingName = ""
    if ratingGroup == 1:
        ratingName = "<=2.0stars"
    elif ratingGroup == 2:
        ratingName = ">=2.5starsAnd<=3.5stars"
    elif ratingGroup == 3:
        ratingName = ">=4.0stars"
    fileOutputName = "../newtrain/"+state+"_"+cat+"_"+ratingName+".csv"
    cw = csvWriter(fileOutputName)
    cw.writerow(headers0)
    #1 rating < 2.5
    for d in doc:
        if ratingGroup == 1:
            if cat == 'Desserts':
                if d[10] < 2.5 and d[3] == state and 'Desserts' or 'Ice Cream & Frozen Yogurt' in d:
                    cw.writerow(d)
            else:
                if d[10] < 2.5 and d[3] == state and cat in d:
                    cw.writerow(d)
        #2 rating between 2.5 and 3.5
        elif ratingGroup == 2:
           if cat == 'Desserts':
                if d[10] >= 2.5 and d[10] <= 3.5 and d[3] == state and 'Desserts' or 'Ice Cream & Frozen Yogurt' in d:
                    cw.writerow(d)
           else:
                if d[10] >=2.5 and d[10] <= 3.5 and d[3] == state and cat in d:
                    cw.writerow(d)
        #3 rating > 3.5
        elif ratingGroup == 3:
             if cat == 'Desserts':
                if d[10] >=4 and d[3] == state and 'Desserts' or 'Ice Cream & Frozen Yogurt' in d:
                    cw.writerow(d)
             else:
                if d[10] >=4  and d[3] == state and cat in d:
                    cw.writerow(d)

def splitByStateCategorySentiment(state,cat,sentiment):
     cr = csvReader("../Data/data.csv")
     doc = []
     headers0 = ["Business_ID","Business_Name","Business_Category","State","City","Neigh","Neigh1","Neigh2","Lat","Lon","Rating","Date","Price_Range","Num_Review","Text_Review"]
     fileOutputName = state+"_"+cat+"_"+sentiment+".csv"
     cw = csvWriter(fileOutputName)
     cw.writerow(headers0)
     for row in cr:
        try:
            info = []
            allCat = []
            bizId = row[1]
            bizName = row[34]
            bizCat1 = row[12]
            bizCat2 = row[13]
            bizCat3 = row[14]
            bizCat4 = row[15]
            bizCat5 = row[16]
            bizCat6 = row[17]
            bizCat7 = row[18]
            bizCat8 = row[19]
            bizCat9 = row[20]
            bizCat10 = row[21]
            bizCat11 = row[22]
            bizState = row[51]
            bizCity = row[73]
            bizNeigh = row[111]
            bizNeigh1 = row[112]
            bizNeigh2 = row[113]
            lat = float(row[23])
            lon = float(row[86])
            bizRating = float(row[77])
            date  = row[125]
            priceRange = row[84]
            numReview = int(row[49])
            text = row[121].lower()
            text = excludeFunction(r'\\n'," ",text) #remove \n
            text = excludeFunction(r'\\r'," ",text) #remove \r
            text = excludeFunction(r'\\'," ",text) #remove \
            text = excludeFunction(r'<[^>]+>'," ",text) #remove # HTML tags
            text = excludeFunction( r'(?:@[\w_]+)'," ",text) #remove @
            text = excludeFunction(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'," ",text) #remove html function
            text = excludeFunction(r'\s\s+',' ',text) #remove multi space"""
            text = text.lstrip() #left trim
            text = text.rstrip() #right trim
            info.append(bizId)
            info.append(bizName)
            allCat.append(bizCat1)
            allCat.append(bizCat2)
            allCat.append(bizCat3)
            allCat.append(bizCat4)
            allCat.append(bizCat5)
            allCat.append(bizCat6)
            allCat.append(bizCat7)
            allCat.append(bizCat8)
            allCat.append(bizCat9)
            allCat.append(bizCat10)
            allCat.append(bizCat11)
            if cat == 'Desserts':
                if 'Desserts' or 'Ice Cream & Frozen Yogurt' in allCat:
                    info.append('Desserts')
            elif cat in allCat:
                info.append(cat)
            info.append(bizState)
            info.append(bizCity)
            info.append(bizNeigh)
            info.append(bizNeigh1)
            info.append(bizNeigh2)
            info.append(lat)
            info.append(lon)
            info.append(bizRating)
            info.append(date)
            info.append(priceRange)
            info.append(numReview)
            info.append(text)
            doc.append(info)
        except IndexError:
            pass

     for d in doc:
        blob = initialiseTextBlob(d[14])
        if cat in d and d[3] == state and blob.sentiment > 0:
            cw.writerow(d)



def splitByStateCategory():
    cr = csvReader("../Data/data.csv")
    doc = []
    #headers0 = ["Business_ID","Business_Name","Business_Category","State","City","Neigh","Neigh1","Neigh2","Lat","Lon","Rating","Date","Price_Range","Num_Review","Text_Review","Polarity"]
    fileOutputName = "dashboard_latest_1.csv"
    cw = csvWriter(fileOutputName)
    #cw.writerow(headers0)
    rState = ["AZ","IL","MA","NC","NV","PA","SC","WI"]
    for row in cr:
        try:
            info = []
            allCat = []
            bizId = row[1]
            bizName = row[34]
            bizCat1 = row[12]
            bizCat2 = row[13]
            bizCat3 = row[14]
            bizCat4 = row[15]
            bizCat5 = row[16]
            bizCat6 = row[17]
            bizCat7 = row[18]
            bizCat8 = row[19]
            bizCat9 = row[20]
            bizCat10 = row[21]
            bizCat11 = row[22]
            bizState = row[51]
            bizCity = row[73]
            bizNeigh = row[111]
            bizNeigh1 = row[112]
            bizNeigh2 = row[113]
            lat = float(row[23])
            lon = float(row[86])
            bizRating = float(row[77])
            date  = row[125]
            priceRange = row[84]
            numReview = int(row[49])
            text = row[121].lower()
            text = excludeFunction(r'\\n'," ",text) #remove \n
            text = excludeFunction(r'\\r'," ",text) #remove \r
            text = excludeFunction(r'\\'," ",text) #remove \
            text = excludeFunction(r'<[^>]+>'," ",text) #remove # HTML tags
            text = excludeFunction( r'(?:@[\w_]+)'," ",text) #remove @
            text = excludeFunction(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'," ",text) #remove html function
            text = excludeFunction(r'\s\s+',' ',text) #remove multi space"""
            text = text.lstrip() #left trim
            text = text.rstrip() #right trim
            info.append(bizId)
            info.append(bizName)
            allCat.append(bizCat1)
            allCat.append(bizCat2)
            allCat.append(bizCat3)
            allCat.append(bizCat4)
            allCat.append(bizCat5)
            allCat.append(bizCat6)
            allCat.append(bizCat7)
            allCat.append(bizCat8)
            allCat.append(bizCat9)
            allCat.append(bizCat10)
            allCat.append(bizCat11)
            #if 'Desserts' or 'Ice Cream & Frozen Yogurt' in allCat:
                #info.append('Desserts')
                #print("Desserts")
            #if "Bars" in allCat:
                #info.append("Bars")
                #print "Bars"
            #"Bakeries" in allCat:
                #info.append("Bakeries")

            #if "Breakfast & Brunch" in allCat:
                #info.append("Breakfast & Brunch")
            #if "Coffee & Tea" in allCat:
                #info.append("Coffee & Tea")
                #print ("coffee")
            info.append(bizState)
            info.append(bizCity)
            info.append(bizNeigh)
            info.append(bizNeigh1)
            info.append(bizNeigh2)
            info.append(lat)
            info.append(lon)
            info.append(bizRating)
            info.append(date)
            info.append(priceRange)
            info.append(numReview)
            #print text
            """
            try:
                text = unicode(text)
            except UnicodeDecodeError:
                continue
            """
            #info.append(text)
            blob = TextBlob(text)
            posCount = 0;
            negCount = 0;
            for s in blob.sentences:
                if s.polarity > 0:
                    posCount +=1;
                elif s.polarity < 0:
                    negCount +=1;

            if posCount > negCount:
                pol = "pos"
            elif negCount > posCount:
                pol = "neg"
            else:
                pol = "neu"
            info.append(pol)
            if info[3] in rState:
                print ("In")
                cw.writerow(info)
        except IndexError:
            pass

#new method
def getWordCount(inputFileName):
    cr = csvReader(inputFileName)
    inputStr = ""
    for row in cr:
        inputStr += row[0].split("|")[14]

    blob = TextBlob(inputStr)
    return blob.word_counts

w = getWordCount("PA_Bars.csv")
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
number = 0

#split adjective into positive and negative

"""
for k in sorted(w, key = w.get, reverse = True):
    blob = TextBlob(k)
    if k not in stops and blob.tags[0][1] == 'JJ' and w[k] > 3:
        print (k,w[k])

def getAdjective(inputFileName):
    cr = csvReader(inputFileName)
    inputStr = ""
    for row in cr:
        inputStr += row[0].split("|")[14]

    blob = TextBlob(inputStr)


def getNoun(inputFileName):
    cr = csvReader(inputFileName)
    inputStr = ""
    for row in cr:
        inputStr += row[0].split("|")[14]
    blob = TextBlob(inputStr)
    for word, pos in blob.tags:
        if pos == 'JJ':
            print("happy")
"""

#splitByStateCategory()


splitByStateCategoryRating("AZ","Bakeries",1)
splitByStateCategoryRating("AZ","Bars",1)
splitByStateCategoryRating("AZ","Breakfast & Brunch",1)
splitByStateCategoryRating("AZ","Coffee & Tea",1)
splitByStateCategoryRating("AZ","Desserts",1)

splitByStateCategoryRating("AZ","Bakeries",2)
splitByStateCategoryRating("AZ","Bars",2)
splitByStateCategoryRating("AZ","Breakfast & Brunch",2)
splitByStateCategoryRating("AZ","Coffee & Tea",2)
splitByStateCategoryRating("AZ","Desserts",2)

splitByStateCategoryRating("AZ","Bakeries",3)
splitByStateCategoryRating("AZ","Bars",3)
splitByStateCategoryRating("AZ","Breakfast & Brunch",3)
splitByStateCategoryRating("AZ","Coffee & Tea",3)
splitByStateCategoryRating("AZ","Desserts",3)
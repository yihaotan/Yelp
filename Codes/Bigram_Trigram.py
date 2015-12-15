__author__ = 'YiHao'

import csv
import re
from textblob import TextBlob
import string
from nltk.corpus import stopwords
from collections import Counter


def csvReader(fileName):
    cr = csv.reader(open(fileName,'r'))
    skipHeader = next(cr,None)
    return cr


def csvWriter(fileName):
    cw = csv.writer(open(fileName, "a"), delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')
    return cw

def initialiseInputStr(textReviewArray):
    inputStr = " ".join(textReviewArray)
    return repr(inputStr)

def initialiseTextBlob(inputStr):
    blob = TextBlob(inputStr)
    return blob

def excludeFunction(regex,rep,string):
    string = re.sub(regex,rep,string)
    return string

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def generateNgram(inputFileName,state,cat,ratingGroup,n):
    textReviewArray = []
    cr = ""
    cr1 = csvReader('../Data/stopwords.csv')
    fileNameDirectory = ""
    outputFileName = state+"_"+cat+"_"+str(ratingGroup)+"_"+"trigram.csv"
    cw = csvWriter(outputFileName)
    if ratingGroup == 1:
        fileNameDirectory = "../rating1/"
    elif ratingGroup == 2:
        fileNameDirectory = "../rating2/"
    elif ratingGroup == 3:
        fileNameDirectory = "../rating3/"
    else:
        fileNameDirectory = "../train1/"
    cr = csvReader(fileNameDirectory + inputFileName)
    for row in cr:
        print row[14]
        #print row[0]
        #textReviewArray.append(row[14])
    inputStr = initialiseInputStr(textReviewArray)

    stop = stopwords.words('english')
    stop.append("doesn\\'t")
    stop.append("didn\\'t")
    stop.append("don\\'t")
    stop.append("wasn\\'t")
    stop.append("isn\\'t")
    stop.append("couldn\\'t")
    stop.append("can\\'t")
    stop.append("wouldn\\'t")
    stop.append("glac\\xc3\\xa9")
    stop.append("aren\\'t")
    stop.append("haven\\'t")
    stop.append("won\\'t")
    stop.append("also")
    stop.append("dell\\'arizona")
    stop.append("d\\'italia")
    stop.append("weren\\'t")

    for row in cr1:
        stop.extend(row)

    for i in stop:
        print i
    blob = initialiseTextBlob(inputStr)
    ngrams = blob.ngrams(n)
    #use hashmap
    map = {}
    for ngram in ngrams:
        condition = True
        for i in range(0,len(ngram)):
            if ngram[i] in stop or len(ngram[i]) <= 3 or hasNumbers(ngram[i]):
                condition = False
        if condition:
            if n == 2:
                key = ngram[0] +" "+ ngram[1]
            else:
                key = ngram[0] +" "+ ngram[1] + " "+ngram[2]
            #print key

            if key in map:
                map[key] += 1
            else:
                map[key] = 1
            #print map[key]

    for k in sorted(map, key=map.get, reverse=True):
        print k, map[k]
        d = [k,map[k]]
        if map[k] > 2:
            cw.writerow(d)

def getBigramCount(inputFileName,state,cat,rating):

    #create the 5 different category hashmaps to store the bigram and the frequency from the csv file
    service = {}
    value = {}
    variety = {}
    ambience = {}
    taste = {}
    accessibility = {}
    cr = csvReader("../Data/bigramCombined.csv")
    for r in cr:
        if r[2] == "value":
            k = r[0]
            if k not in value:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                value[k] = score
        elif r[2] == "service":
            k = r[0]
            if k not in service:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                service[k] = score
        elif r[2] == "ambience":
            k = r[0]
            if k not in ambience:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                ambience[k] = score
        elif r[2] == "taste":
            k = r[0]
            if k not in taste:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                taste[k] = score
        elif r[2] == "variety":
            k = r[0]
            if k not in variety:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                taste[k] = score
        else:
            k = r[0]
            if k not in accessibility:
                polarity = r[3]
                score = int(r[4])
                if polarity == "Neg":
                    score *= -1
                accessibility[k] = score

    cr = csvReader(inputFileName)
    inputStr = " "
    for r in cr:
        print r[0].split("|")[1]
        print r[0].split("|")[0]
        text = r[0].split("|")[14]
        try:
            text = unicode(text)
            inputStr += text + " "
        except UnicodeDecodeError:
            pass

    blob = TextBlob(inputStr)
    wordsArray = blob.words
    bigrams = blob.ngrams(2)
    bigramsList = []
    for i in bigrams:
        bigramsList.append(i[0]+" "+i[1])

    cw1 = csvWriter("../Tableau Data/")
    #headers1 = ["State","Business_Category","Business_Rating","Bigram","Bigram_Cat","Bigram_Freq","Bigram_Sentiment","Bigram_Importance"]
    #cw1.writerow(headers1)


    serviceList = {}
    for k in service:
        #check whether the word in the service category exists in the textreview
        if k in bigramsList:
            #store the frequency of the word in the serviceList hashmap
            if k not in serviceList:
                serviceList[k] = 1;
            else:
                serviceList[k] +=1

    #write into the csv output file used for tableau visualisation
    for k in serviceList:
        d = []
        d.append(state)
        d.append(cat)
        d.append(rating)
        d.append(k)
        d.append("Service")
        freq = serviceList[k]
        d.append(freq)
        sentiment = service[k]
        d.append(sentiment)
        #importance of word is calculated by the number of times it appears in the textreview
        #and the sentiment score assigned to the word
        #for example, happy hour will have 25 importance when it appears 25 times in the
        #textreview and is assigned a sentiment score of 1
        importance = freq * sentiment
        d.append(importance)
        cw1.writerow(d)

    ambienceList = {}
    for k in ambience:
        if k in bigramsList:
            print k
            if k not in ambienceList:
                ambienceList[k] = 1;
            else:
                ambienceList[k] +=1
        else:
            print "nothing"

    for k in ambienceList:
        d = []
        d.append(state)
        d.append(cat)
        d.append(rating)
        d.append(k)
        d.append("Ambience")
        freq = ambienceList[k]
        d.append(freq)
        sentiment = ambience[k]
        d.append(sentiment)
        importance = freq * sentiment
        d.append(importance)
        cw1.writerow(d)

    varietyList = {}
    for k in variety:
        if k in bigramsList:
            print k
            if k not in varietyList:
                varietyList[k] = 1;
            else:
                varietyList[k] +=1
        else:
            print "nothing"

    for k in varietyList:
        d = []
        d.append(state)
        d.append(cat)
        d.append(rating)
        d.append(k)
        d.append("Variety")
        freq = varietyList[k]
        d.append(freq)
        sentiment = variety[k]
        d.append(sentiment)
        importance = freq * sentiment
        d.append(importance)
        cw1.writerow(d)

    tasteList = {}
    for k in taste:
        if k in bigramsList:
            print k
            if k not in tasteList:
                tasteList[k] = 1;
            else:
                tasteList[k] +=1
        else:
            print "nothing"

    for k in tasteList:
        d = []
        d.append(state)
        d.append(cat)
        d.append(rating)
        d.append(k)
        d.append("Taste")
        freq = tasteList[k]
        d.append(freq)
        sentiment = taste[k]
        d.append(sentiment)
        importance = freq * sentiment
        d.append(importance)
        cw1.writerow(d)

    accessibilityList = {}
    for k in accessibility:
        if k in bigramsList:
            print k
            if k not in accessibilityList:
                accessibilityList[k] = 1;
            else:
                accessibilityList[k] +=1
        else:
            print "nothing"

    for k in accessibilityList:
        d = []
        d.append(state)
        d.append(cat)
        d.append(rating)
        d.append(k)
        d.append("Accessibility")
        freq = accessibilityList[k]
        d.append(freq)
        sentiment = accessibility[k]
        d.append(sentiment)
        importance = freq * sentiment
        d.append(importance)
        cw1.writerow(d)

#AZ
getBigramCount("../newtrain/AZ_Bakeries_>=4.0stars.csv","AZ","Bakeries",">=4.0stars")
getBigramCount("../newtrain/AZ_Bakeries_>=4.0stars.csv","AZ","Bakeries",">=4.0stars")
getBigramCount("../newtrain/AZ_Bars_>=4.0stars.csv","AZ","Bars",">=4.0stars")
getBigramCount("../newtrain/AZ_Breakfast & Brunch_>=4.0stars.csv","AZ","Breakfast & Brunch",">=4.0stars")
getBigramCount("../newtrain/AZ_Coffee & Tea_>=4.0stars.csv","AZ","Coffee & Tea",">=4.0stars")
getBigramCount("../newtrain/AZ_Desserts_>=4.0stars.csv","AZ","Desserts",">=4.0stars")

getBigramCount("../newtrain/AZ_Bakeries_>=2.5starsAnd<=3.5stars.csv","AZ","Bakeries",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/AZ_Bars_>=2.5starsAnd<=3.5stars.csv","AZ","Bars",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/AZ_Breakfast & Brunch_>=2.5starsAnd<=3.5stars.csv","AZ","Breakfast & Brunch",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/AZ_Coffee & Tea_>=2.5starsAnd<=3.5stars.csv","AZ","Coffee & Tea",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/AZ_Desserts_>=2.5starsAnd<=3.5stars.csv","AZ","Desserts",">=2.5starsAnd<=3.5stars")

getBigramCount("../newtrain/AZ_Bakeries_<=2.0stars.csv","AZ","Bakeries","<=2.0stars.csv")
getBigramCount("../newtrain/AZ_Bars_<=2.0stars.csv","AZ","Bars","<=2.0stars.csv")
getBigramCount("../newtrain/AZ_Breakfast & Brunch_<=2.0stars.csv","AZ","Breakfast & Brunch","<=2.0stars.csv")
getBigramCount("../newtrain/AZ_Coffee & Tea_<=2.0stars.csv","AZ","Coffee & Tea","<=2.0stars.csv")
getBigramCount("../newtrain/AZ_Desserts_<=2.0stars.csv","AZ","Desserts","<=2.0stars.csv")

#PA
getBigramCount("../newtrain/PA_Bakeries_>=4.0stars.csv","PA","Bakeries",">=4.0stars")
getBigramCount("../newtrain/PA_Bars_>=4.0stars.csv","PA","Bars",">=4.0stars")
getBigramCount("../newtrain/PA_Breakfast & Brunch_>=4.0stars.csv","PA","Breakfast & Brunch",">=4.0stars")
getBigramCount("../newtrain/PA_Coffee & Tea_>=4.0stars.csv","PA","Coffee & Tea",">=4.0stars")
getBigramCount("../newtrain/PA_Desserts_>=4.0stars.csv","PA","Desserts",">=4.0stars")

getBigramCount("../newtrain/PA_Bakeries_>=2.5starsAnd<=3.5stars.csv","PA","Bakeries",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/PA_Bars_>=2.5starsAnd<=3.5stars.csv","PA","Bars",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/PA_Breakfast & Brunch_>=2.5starsAnd<=3.5stars.csv","PA","Breakfast & Brunch",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/PA_Coffee & Tea_>=2.5starsAnd<=3.5stars.csv","PA","Coffee & Tea",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/PA_Desserts_>=2.5starsAnd<=3.5stars.csv","PA","Desserts",">=2.5starsAnd<=3.5stars")

getBigramCount("../newtrain/PA_Bakeries_<=2.0stars.csv","PA","Bakeries","<=2.0stars.csv")
getBigramCount("../newtrain/PA_Bars_<=2.0stars.csv","PA","Bars","<=2.0stars.csv")
getBigramCount("../newtrain/PA_Breakfast & Brunch_<=2.0stars.csv","PA","Breakfast & Brunch","<=2.0stars.csv")
getBigramCount("../newtrain/PA_Coffee & Tea_<=2.0stars.csv","PA","Coffee & Tea","<=2.0stars.csv")
getBigramCount("../newtrain/PA_Desserts_<=2.0stars.csv","PA","Desserts","<=2.0stars.csv")

#NV
getBigramCount("../newtrain/NV_Bakeries_>=4.0stars.csv","NV","Bakeries",">=4.0stars")
getBigramCount("../newtrain/NV_Bars_>=4.0stars.csv","NV","Bars",">=4.0stars")
getBigramCount("../newtrain/NV_Breakfast & Brunch_>=4.0stars.csv","NV","Breakfast & Brunch",">=4.0stars")
getBigramCount("../newtrain/NV_Coffee & Tea_>=4.0stars.csv","NV","Coffee & Tea",">=4.0stars")
getBigramCount("../newtrain/NV_Desserts_>=4.0stars.csv","NV","Desserts",">=4.0stars")

getBigramCount("../newtrain/NV_Bakeries_>=2.5starsAnd<=3.5stars.csv","NV","Bakeries",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NV_Bars_>=2.5starsAnd<=3.5stars.csv","NV","Bars",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NV_Breakfast & Brunch_>=2.5starsAnd<=3.5stars.csv","NV","Breakfast & Brunch",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NV_Coffee & Tea_>=2.5starsAnd<=3.5stars.csv","NV","Coffee & Tea",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NV_Desserts_>=2.5starsAnd<=3.5stars.csv","NV","Desserts",">=2.5starsAnd<=3.5stars")

getBigramCount("../newtrain/NV_Bakeries_<=2.0stars.csv","NV","Bakeries","<=2.0stars.csv")
getBigramCount("../newtrain/NV_Bars_<=2.0stars.csv","NV","Bars","<=2.0stars.csv")
getBigramCount("../newtrain/NV_Breakfast & Brunch_<=2.0stars.csv","NV","Breakfast & Brunch","<=2.0stars.csv")
getBigramCount("../newtrain/NV_Coffee & Tea_<=2.0stars.csv","NV","Coffee & Tea","<=2.0stars.csv")
getBigramCount("../newtrain/NV_Desserts_<=2.0stars.csv","NV","Desserts","<=2.0stars.csv")

#NC
getBigramCount("../newtrain/NC_Bakeries_>=4.0stars.csv","NC","Bakeries",">=4.0stars")
getBigramCount("../newtrain/NC_Bars_>=4.0stars.csv","NC","Bars",">=4.0stars")
getBigramCount("../newtrain/NC_Breakfast & Brunch_>=4.0stars.csv","NC","Breakfast & Brunch",">=4.0stars")
getBigramCount("../newtrain/NC_Coffee & Tea_>=4.0stars.csv","NC","Coffee & Tea",">=4.0stars")
getBigramCount("../newtrain/NC_Desserts_>=4.0stars.csv","NC","Desserts",">=4.0stars")

getBigramCount("../newtrain/NC_Bakeries_>=2.5starsAnd<=3.5stars.csv","NC","Bakeries",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NC_Bars_>=2.5starsAnd<=3.5stars.csv","NC","Bars",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NC_Breakfast & Brunch_>=2.5starsAnd<=3.5stars.csv","NC","Breakfast & Brunch",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NC_Coffee & Tea_>=2.5starsAnd<=3.5stars.csv","NC","Coffee & Tea",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/NC_Desserts_>=2.5starsAnd<=3.5stars.csv","NC","Desserts",">=2.5starsAnd<=3.5stars")

getBigramCount("../newtrain/NC_Bakeries_<=2.0stars.csv","NC","Bakeries","<=2.0stars.csv")
getBigramCount("../newtrain/NC_Bars_<=2.0stars.csv","NC","Bars","<=2.0stars.csv")
getBigramCount("../newtrain/NC_Breakfast & Brunch_<=2.0stars.csv","NC","Breakfast & Brunch","<=2.0stars.csv")
getBigramCount("../newtrain/NC_Coffee & Tea_<=2.0stars.csv","NC","Coffee & Tea","<=2.0stars.csv")
getBigramCount("../newtrain/NC_Desserts_<=2.0stars.csv","NC","Desserts","<=2.0stars.csv")

#WI
getBigramCount("../newtrain/WI_Bakeries_>=4.0stars.csv","WI","Bakeries",">=4.0stars")
getBigramCount("../newtrain/WI_Bars_>=4.0stars.csv","WI","Bars",">=4.0stars")
getBigramCount("../newtrain/WI_Breakfast & Brunch_>=4.0stars.csv","WI","Breakfast & Brunch",">=4.0stars")
getBigramCount("../newtrain/WI_Coffee & Tea_>=4.0stars.csv","WI","Coffee & Tea",">=4.0stars")
getBigramCount("../newtrain/WI_Desserts_>=4.0stars.csv","WI","Desserts",">=4.0stars")

getBigramCount("../newtrain/WI_Bakeries_>=2.5starsAnd<=3.5stars.csv","WI","Bakeries",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/WI_Bars_>=2.5starsAnd<=3.5stars.csv","WI","Bars",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/WI_Breakfast & Brunch_>=2.5starsAnd<=3.5stars.csv","WI","Breakfast & Brunch",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/WI_Coffee & Tea_>=2.5starsAnd<=3.5stars.csv","WI","Coffee & Tea",">=2.5starsAnd<=3.5stars")
getBigramCount("../newtrain/WI_Desserts_>=2.5starsAnd<=3.5stars.csv","WI","Desserts",">=2.5starsAnd<=3.5stars")

getBigramCount("../newtrain/WI_Bakeries_<=2.0stars.csv","WI","Bakeries","<=2.0stars.csv")
getBigramCount("../newtrain/WI_Bars_<=2.0stars.csv","WI","Bars","<=2.0stars.csv")
getBigramCount("../newtrain/WI_Breakfast & Brunch_<=2.0stars.csv","WI","Breakfast & Brunch","<=2.0stars.csv")
getBigramCount("../newtrain/WI_Coffee & Tea_<=2.0stars.csv","WI","Coffee & Tea","<=2.0stars.csv")
getBigramCount("../newtrain/WI_Desserts_<=2.0stars.csv","WI","Desserts","<=2.0stars.csv")














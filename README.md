# Yelp Text and Sentiment Analysis

Yelp was founded in 2003. It is a community review portal that provides users with business recommendations in areas such as home services, health services and restaurants etc. Over the past decade, it has collected a tremendous amount of review data due to its large active users base. In order to utilise the review data efficiently, a Tableau dashboard was developed to analyse the review data for the US resturants. 

The Tableau dashboard allows the users to evaluate the frequency of the positive, neutral and negative sentiment keywords associated with the resturant category / name for both self and competitor analysis. These keywords include adjectives and bigrams (adjectives + nouns). Besides this, the users can also easily identify the category which required the greatest improvement as the bigrams were grouped into 5 distinct categories with different polarity scores ranging from -3 to -1 and 3 to 1. The categories are namely accessibility, ambience, service, taste and variety. 

Demo: goo.gl/RbKSdw

##Core Features 
- Text and Sentiment classifier (Textblob)
- General Overview of the resturants (Location of the popular and unpopular resturants)
- Competitor Analysis for the resturants with similar business category and location etc. (Side by Side Wordclouds to display the positive, neutral and negative keywords)
- Bigram Analysis for the resturants with similar business category and location etc. (Wordcloud and barcharts to display the importance, frequency * polarity score, of positve and negative keywords) 

##Architecture
Yelp Text and Sentiment Analysis dashboard uses Tableau and Python for data visualisation and data cleansing / mining respectively.

##Documentation
###Data
1. Tableau dashboard1 data: https://goo.gl/Ij0MTN
2. Tableau dashboard2 data: https://goo.gl/TkOD0W
3. Tableau dashboard3 data: https://goo.gl/DoIP4u
4. Yelp data: https://goo.gl/WbJ3eo (TextSplit.py)
5. Restaurants by category,state and rating https://goo.gl/qae86U (Tableau2.py)
6. Restaurants <= 2.0stars: https://goo.gl/1SrPpG (Tableau3.py)
7. Restaurants >= 2.5stars: && <= 3.5 stars https://goo.gl/XhOqo1 (Tableau3.py)
8. Restaurants >= 4.0stars: https://goo.gl/ujzzeq (Tableau3.py)
9. Bigram data https://goo.gl/fVMq7L (Tableau3.py)
10. Stopwords https://goo.gl/GBQSKp (Tableau3.py)


###Codes
1. TextSplit.py
2. Tableau2.py
3. Tableau3.py

###Getting Started

CSV package
```
def csvReader(fileName):
    cr = csv.reader(open(fileName,'r'))
    skipHeader = next(cr,None)
    return cr
```
- read the csv file by each row
- skip the header row
```
def csvWriter(fileName):
    cw = csv.writer(open(fileName, "a"), delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')
    return cw
```
- append the content into the csv file with the delimiter '|'

TextBlob package
```
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
```
- initialise TextBlob, a sentiment classifier for text review
- read the text review by each sentence
- classify each sentence based on polarity namely negative, neutral and positive
- if the number of positive sentences > negative sentences, text review == positive and vice-versa
- use to get data required for Tableau dashboard1



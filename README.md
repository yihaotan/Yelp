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
1. Yelp data: https://goo.gl/WbJ3eo
2. Tableau dashboard1 data: https://goo.gl/Ij0MTN
3. Tableau dashboard2 data: https://goo.gl/TkOD0W
4. Restaurants <= 2.0stars https://goo.gl/1SrPpG
5. Restaurants >= 2.5stars && <= 3.5 stars https://goo.gl/XhOqo1
6. Restaurants >= 4.0stars https://goo.gl/ujzzeq
7. Tableau dashboard3 data: https://goo.gl/DoIP4u


###Codes
1. TextSplit.py
2. Tableau2.py 

###Getting Started



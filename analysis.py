'''
uses TextBlob to obtain sentiment for unique tweets
'''

import csv
from textblob import TextBlob
import sys


alltweets = csv.reader(open("search-data/searchTweets.csv",'r', encoding="utf-8"))
sntTweets = csv.writer(open("search-data/sentimentUniqueTweets.csv",'w', encoding="utf-8"))

for row in alltweets:
    if any(row):
        blob = TextBlob(row[2])
        print (blob.sentiment.polarity)
        if blob.sentiment.polarity > 0:
            sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "positive"])
        elif blob.sentiment.polarity < 0:
            sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "negative"])
        elif blob.sentiment.polarity == 0.0:
            sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "neutral"])

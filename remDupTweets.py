'''
removing duplicate tweets from gathered
'''

import csv

alltweets = csv.reader(open("search-data/searchTweets.csv",'r', encoding="utf-8"))

noDup = csv.writer(open("search-data/uniqueSearchTweets.csv",'w', encoding="utf-8")) # store unique tweets
# airwayTweet = csv.writer(open("tweets-data/airwayTweets.csv", "wb")) # store tweets by ariways

tweets = set()
i = 0;
for row in alltweets:
    if any(row):
        i = i + 1
        print (i)
        if row[2] not in tweets:
            t = row[2].lower()
            t = t.replace('\n', '')
            noDup.writerow([row[0], row[1], t])
            print ("writing row..")
            tweets.add( row[2] )

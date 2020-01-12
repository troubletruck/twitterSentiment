'''
compute total, positive, negative and neutral tweets for each airline
'''

import csv

def getStats(s, fileRead):
    tot = 0;
    pos = 0;
    neg = 0;
    neu = 0;
    for row in fileRead:
        if any(row):
            tot = tot + 1;
            if row[4] == "positive":
                pos = pos + 1;
            elif row[4] == "negative":
                neg = neg + 1;
            elif row[4] == "neutral":
                neu = neu + 1;
    print ("Tweets Stats for", s)
    print ("total tweets: ", tot)
    print ("positive: ", pos)
    print ("negative: ", neg)
    print ("neutral: ", neu)
    results.writerow([s, tot, pos, neg, neu])

topicTweets = csv.reader(open("search-data/twitchsupportTweets.csv",'r', encoding="utf-8"))
results = csv.writer(open("search-data/results.csv",'w', encoding="utf-8"))

getStats("twitchsupport", topicTweets)

'''
scraps and stores tweets by airline
'''

import csv

sntTweets = csv.reader(open("search-data/sentimentUniqueTweets.csv",'r', encoding="utf-8"))

def scrapTweets(topic):
    topicTweet = csv.writer(open("search-data/"+topic+"Tweets.csv",'w', encoding="utf-8"))
    # store tweets by airways
    count = 1
    for row in sntTweets:
        if any(row):
            r = row[2].lower()
            r = row[2].strip('#').strip('@')
            if topic in r:
                count = count + 1
                topicTweet.writerow(row)
    print ("# of rows", count)

scrapTweets("twitchsupport") # replace with emirates and etihadairways and run this script again

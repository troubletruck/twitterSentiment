import tweepy
from textblob import TextBlob

import sys
import csv
import io


alltweets = csv.writer(open("search-data/searchTweets.csv",'w', encoding="utf-8", newline=''))

consumer_key = 'RnizfvMt4v3H323KBA9gT4ssM'
consumer_key_secret = '3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi'

access_token = '1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm'
access_token_secret = 'tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userSearch = 'SamStrake'
ignoreTweetsFrom = 'SamStrake'
max_tweets = 500


def search(keywords):
    access_key = "1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm"
    access_secret = "tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk"
    consumer_key = "RnizfvMt4v3H323KBA9gT4ssM"
    consumer_secret = "3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi"

    #to authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=userSearch, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            break

    count = 1;
    for tweet in searched_tweets:
        if tweet.user.screen_name != ignoreTweetsFrom: #Removing all tweets from the user
            created_at =  tweet.created_at  # accessing tweet time
            tweet_id = tweet.id_str         # accessing tweet id
            tweet_text = tweet.text         # accessing tweet text
            user_followers_count = tweet.user.followers_count
            retweet_count = tweet.retweet_count
            favorite_count = tweet.favorite_count
            alltweets.writerow([created_at, tweet_id, tweet_text, user_followers_count, retweet_count, favorite_count])

search(userSearch)

alltweets = csv.reader(open("search-data/searchTweets.csv",'r', encoding="utf-8"))
noDup = csv.writer(open("search-data/uniqueSearchTweets.csv",'w', encoding="utf-8", newline='')) # store unique tweets

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

alltweets = csv.reader(open("search-data/searchTweets.csv",'r', encoding="utf-8"))
sntTweets = csv.writer(open("search-data/sentimentUniqueTweets.csv",'w', encoding="utf-8", newline=''))

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


sntTweets = csv.reader(open("search-data/sentimentUniqueTweets.csv",'r', encoding="utf-8"))

def scrapTweets(topic):
    topicTweet = csv.writer(open("search-data/"+topic+"Tweets.csv",'w', encoding="utf-8", newline=''))
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

scrapTweets(userSearch) # replace with emirates and etihadairways and run this script again

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

topicTweets = csv.reader(open("search-data/"+userSearch+"Tweets.csv",'r', encoding="utf-8"))
results = csv.writer(open("search-data/results.csv",'w', encoding="utf-8", newline=''))

getStats(userSearch, topicTweets)

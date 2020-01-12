import tweepy
from textblob import TextBlob

import sys
import csv
import io


alltweets = csv.writer(open("search-data/searchTweets.csv",'w', encoding="utf-8"))

consumer_key = 'RnizfvMt4v3H323KBA9gT4ssM'
consumer_key_secret = '3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi'

access_token = '1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm'
access_token_secret = 'tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userSearch = 'SamStrake'
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

    count = 1;
    for tweet in api.search(keywords,'en', count = 100):
        created_at =  tweet.created_at  # accessing tweet time
        tweet_id = tweet.id_str         # accessing tweet id
        tweet_text = tweet.text         # accessing tweet text
        print ("gathered tweet ",count)
        count = count + 1
        alltweets.writerow([created_at, tweet_id, tweet_text])

file = open('hashtags-keywords.txt', 'r') # contains a list of keywords
queries = file.readlines()

for q in queries:
    # read one keyword at a time
    print ("----")
    print (q)
    search(q)

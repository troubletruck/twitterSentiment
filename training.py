import tweepy
from textblob import TextBlob

import sys
import csv
import io

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd, numpy as np, re, time
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


alltweets = csv.writer(open("search-data/searchTweets.csv",'w', encoding="utf-8", newline=''))

consumer_key = 'RnizfvMt4v3H323KBA9gT4ssM'
consumer_key_secret = '3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi'

access_token = '1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm'
access_token_secret = 'tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userSearch = 'TwitchSupport'
ignoreTweetsFrom = 'TwitchSupport'
max_tweets = 500

access_key = "1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm"
access_secret = "tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk"
consumer_key = "RnizfvMt4v3H323KBA9gT4ssM"
consumer_secret = "3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi"

#to authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

searched_tweets = []
tweets_text = []
stemmed_text = []
labels = []
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
        tweets_text.append(tweet.text)
        alltweets.writerow([created_at, tweet_id, tweet_text, user_followers_count, retweet_count, favorite_count])


## Stemming our data
ps = PorterStemmer()

for w in tweets_text:
    stemmed_text.append(ps.stem(w))

# vectorizing the data with maximum of 5000 features
tv = TfidfVectorizer(max_features = 5000)
features = list(stemmed_text)
features = tv.fit_transform(features).toarray()

# getting training and testing data
features_train, features_test = train_test_split(features, test_size = .05, random_state = 0)

# model 1:-
# Using linear support vector classifier
lsvc = LinearSVC()
# training the model
lsvc.fit(features_train)
# getting the score of train and test data
print(lsvc.score(features_train)) # 90.93
print(lsvc.score(features_test))   # 83.75

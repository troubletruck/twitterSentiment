import tweepy
from textblob import TextBlob

consumer_key = 'RnizfvMt4v3H323KBA9gT4ssM'
consumer_key_secret = '3Elb0jq2tdWIC462buY2Lx71KCLGiu1iLgphubYZ9lGQ4IUNHi'

access_token = '1002569857890684928-ZWgqplY8KgEXCmnEkg9QrVKXSz8LFm'
access_token_secret = 'tKm9kYdHzFKL1fabCW6htogL01TTQVY5TkzUya01RHiNk'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Alinity')

goodTweets = 0
badTweets = 0

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
        goodTweets = goodTweets + 1
	else:
		print ('Negative')
        badTweets = badTweets + 1
	print("")
print("Number of good tweets: " + goodTweets)
print("Number of bad tweets: " + badTweets)
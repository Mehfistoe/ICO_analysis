"""
In order to authorize our app to access Twitter on out behalf,
we need to use the OAuth interface.
"""
import tweepy
from tweepy import OAuthHandler
import datetime as dt
import time
#import pandas as pd
import json

consumer_key = open('API_Key.txt', 'r').read().replace('\n', '')
consumer_secret = open('API_Secret.txt', 'r').read().replace('\n', '')
access_token = open('Access_Token.txt', 'r').read().replace('\n', '')
access_secret = open('Access_Token_Secret.txt', 'r').read().replace('\n', '')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
"""
The api variable is now our entry point for most of the operations we
can perform with Twitter.
"""
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#ico_list = pd.read_csv('ico_masterlist.csv', header=0)
komodo_tweets = open('komodo_tweets.txt', 'w')


# TODO: collect tweets from each coins ICO period

def get_tweets(api, search_string):
	#tweets = api.search(search_string, 'en', show_user=True)
	for tweet in tweepy.Cursor(api.search, q=search_string, since_id=2016-10-14, include_entities=True).items():
		print(tweet._json)
		json.dump(tweet._json, komodo_tweets)

# more stuff onward
get_tweets(api, 'komodo')
komodo_tweets.close()
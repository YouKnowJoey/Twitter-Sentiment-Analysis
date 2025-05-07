"""
Using Twitter API v2 to collect tweets and analyze them.
This requires a X (Twitter) Developer account and a Bearer Token for authentication (changed in 2023).
With the free tier developer account, data rates are limited.

Credits:

Project uses code from [@vprusso](https://github.com/vprusso)'s repository: [YouTube Tuturials/ Twitter Sentiment Analysis](https://github.com/vprusso/youtube_tutorials/blob/master/twitter_python/part_5_sentiment_analysis_tweet_data/sentiment_anaylsis_twitter_data.py).  
Thank you [@vprusso](https://github.com/vprusso) for your contribution to the open-source community.
"""

import tweepy
from tweepy import Cursor
from tweepy.streaming import StreamingClient
from tweepy import Client
 
import twitter_credentials

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.client = Client(bearer_token=twitter_credentials.BEARER_TOKEN)
        self.user_client = tweepy.API(self.auth, wait_on_rate_limit=True)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        client = tweepy.OAuth1UserHandler(
            consumer_key=twitter_credentials.CONSUMER_KEY,
            consumer_secret=twitter_credentials.CONSUMER_SECRET,
            access_token=twitter_credentials.ACCESS_TOKEN,
            access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET
        )
        return client

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.client = TwitterAuthenticator().authenticate_twitter_app() 

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app() 
        stream_listener = TwitterListener(auth.bearer_token, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream_listener.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamingClient):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
            raise e
          
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        #return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\\w+:\\/\\/\\S+)", " ", tweet).split())

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['author_id'] = np.array([tweet.author_id for tweet in tweets])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['length'] = np.array([len(tweet.text) for tweet in tweets])
        df['created_at'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['geo'] = np.array([tweet.geo for tweet in tweets])
        df['attachments'] = np.array([tweet.attachments for tweet in tweets])

        # save to csv file, since there is limited data in the free tier
        df.to_csv("tweets_output.txt", sep='\t', index=False)

        return df

 
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    #Obtain desired user's tweets
    user = api.get_user(username= "realDonaldTrump")
    user_id = user.data.id
    print(user.data.username, user.data.id, user.data.name, user.data.description)

    tweets = api.get_users_tweets(
        id=user_id,
        max_results=15,
        exclude='replies'
        ).data

    df = tweet_analyzer.tweets_to_data_frame(tweets)

    print(df.head(5))

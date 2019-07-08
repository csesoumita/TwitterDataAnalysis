# Program for Crawling Twitter Data using Streaming API start for 1% data (via sample method) Start
from pymongo.mongo_client import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import json
import tweepy

# Accessing the Authentication Keys
#consumer key, consumer secret, access token, access secret.
API_key=""
API_secret_key = ""
Access_token = ""
Access_token_secret = ""
# Twitter stream listener
# Twitter stream listener

# Mongo DB Connections
MONGO_HOST= 'mongodb://localhost/webscience'

class listener(StreamListener):

    def on_data(self, data):
        client = MongoClient(MONGO_HOST)
        # webscience in the Mongo DB name being used to store Twitter data
        db = client.webscience
        # To print data in json format
        result_dict = json.loads(data)
        # Inserting json format Twitter crawled data to Mongo DB. twitter_search is the collection name.
        db.twitter_search.insert(result_dict)

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
 auth = OAuthHandler(API_key, API_secret_key)
# Creating object for OAuthHandler class
 auth.set_access_token(Access_token, Access_token_secret)
# Setting Accessing tokens
#Passing class listener  & OAuthHandler class object to Stream class
twitterStream = Stream(auth, listener())
#Sample method is used to return 1% percent of Twitter recent data
twitterStream.sample()
#Program for Crawling Twitter Data using Streaming API start for 1% data (via sample method) End
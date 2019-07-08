# Program for Crawling Twitter Data using Streaming API start(based of certain users and keywords) start
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from pymongo.mongo_client import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import json
import pymongo
# Accessing the Authentication Keys
API_key=""
API_secret_key = ""
Access_token = ""
Access_token_secret = ""

# Mongo DB Connections
MONGO_HOST= 'mongodb://localhost/webscience'

# Printing data from Twitter
class StdOutListener(StreamListener):
    def on_data(self,data):
     client=MongoClient(MONGO_HOST)
     #webscience in the Mongo DB name being used to store Twitter data
     db=client.webscience
     #To print data in json format
     datajson = json.loads(data)
     #Inserting json format Twitter crawled data to Mongo DB. twitter_search is the collection name.
     db.twitter_search.insert(datajson)
     # Printing created date of each twitter message
     created_at = datajson['created_at']
     print(created_at)
     return True
     #Printing errror while accessing Twitter Data
    def on_error(self, status):
     print (status)


if __name__ == '__main__':
    #Creating object for StdOutListener class
    list_data = StdOutListener()
    # Creating object for OAuthHandler class
    auth = OAuthHandler(API_key, API_secret_key)
    #Setting Accessing tokens
    auth.set_access_token(Access_token, Access_token_secret)
    #Passing objects from StdOutListener & OAuthHandler to Stream class
    stream_data = Stream(auth, list_data)

# Getting Twiiter data with keywords Glasgow and Weather
    stream_data.filter(track=['Brexit', 'weather'],languages=['en'])

# Geo-tagged data for user UoGfintech
    stream_data.filter(languages=['en'], track=['@NarendraModi'])


# Program for Crawling Twitter Data using Streaming API start(based of certain users and keywords) end

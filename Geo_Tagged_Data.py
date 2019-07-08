import tweepy
from pymongo.mongo_client import MongoClient
import json

from tweepy import StreamListener, OAuthHandler, Stream

API_key = ""
API_secret_key = ""
Access_token = ""
Access_token_secret = ""
MONGO_HOST = 'mongodb://localhost/webscience'
client = MongoClient(MONGO_HOST)
db = client.webscience
class GeoData_Twitter_RESTAPI:
    client = MongoClient(MONGO_HOST)
    db = client.webscience

    # Search tweets based on specific locations
    def Rest_Geo(self):
        # Insertion in Local Mongo DB
        global API_key
        global API_secret_key
        global Access_token
        global Access_token_secret
        auth = tweepy.OAuthHandler(API_key, API_secret_key)
        auth.set_access_token(Access_token, Access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        for tweet_location in tweepy.Cursor(api.search ,
                                            geocode="55.8642,-4.2518,1mi" ,
                                            since='2018-10-28',
                                            language=['en']).items():
         global db
         db.twitter_search.insert(tweet_location._json)

        print("Geo-tagged Data from REST API Twitter Crawling Completed")
# Program for Twitter Data Crawling via REST API using tweepy End
class GeoData_Twitter_StreamingAPI(StreamListener):
    def on_data(self,data):
        datajson = json.loads(data)
        db.twitter_search.insert(datajson)
if __name__ == '__main__':
    # Geo-tagged data for Glasgow via Streaming API
    list_data = GeoData_Twitter_StreamingAPI()
    auth = OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(Access_token, Access_token_secret)
    stream_data = Stream(auth, list_data)
    stream_data.filter(locations=[-4.5332097324, 55.7874547116, -4.0799567461, 55.9379167225])
    # Geo-tagged data for Glasgow via REST API
    rest_data=GeoData_Twitter_RESTAPI()
    rest_data.Rest_Geo()


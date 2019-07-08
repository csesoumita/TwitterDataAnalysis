# Program for Twitter Data Crawling via REST API using tweepy Start
import tweepy
from pymongo.mongo_client import MongoClient

class filter_Twitter:
    # Accessing the Authentication Keys
    API_key=""
    API_secret_key = ""
    Access_token = ""
    Access_token_secret = ""
    # Passing objects for Twitter Authentication
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(Access_token, Access_token_secret)
    api=tweepy.API(auth,wait_on_rate_limit=True)
    #Insertion in Local Mongo DB
    MONGO_HOST= 'mongodb://localhost/webscience'
    client=MongoClient(MONGO_HOST)
    db=client.webscience

    #Tweets from own twitter account
    public_tweets=api.home_timeline()
    for tweet in public_tweets:
        #db.twitter_search.insert(tweet._json)
        print(tweet)
    # Displaying own Twitter Details
    user= api.me()
    print("Name: "+user.name)
    print ("Location:"+user.location)
    print ("Screen Name:"+user.screen_name)


    #Search tweets via specific twiiter user : Narendra Modi
    search=api.user_timeline(screen_name='NarendraModi',languages=['en'])
    for status in search:
        db.twitter_search.insert(status._json)
    #Search tweets based on specific hastags
    hash_tag='Brexit','weather'
    tweet_keyword=api.search(q=hash_tag,languages=['en'])
    for keywords in tweet_keyword:
        db.twitter_search.insert(keywords._json)




#Program to show Data Analytics of Twitter Data Crawled via Streaming API and REST API start
import pymongo
from pymongo.mongo_client import MongoClient
#Mongo DB Details
MONGO_HOST= 'mongodb://localhost/webscience'
client=MongoClient(MONGO_HOST)
db=client.webscience
# Data Analytics of Twitter Data Start
# Count from Mongo DB
print ("---------Start of Twitter  Data Analytics------------")
#Total data collected in the dataset
total_data=db.twitter_search.find().count()
print ("Total Amount of Data collected:",total_data)
#Amount of geo-tagged data in the dataset
geo_tagged_count=db.twitter_search.find({"user.geo_enabled": True}).count()
print ("Amount of geo-tagged data:",geo_tagged_count)
#Amount of geo-tagged datafrom Glasgow
geo_tagged_glasgow_count=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"}]}).count()
print ("Amount of geo-tagged data from Glasgow:",geo_tagged_glasgow_count)
#Amount of Redundant data
#redundant_data=db.twitter_search.aggregate([{"$group":{"_id":"$id","count":{"$sum":1}}},{"$match":{"count":{"$gt": 1}}},{"$count": "redundant data"}])
exp=[{"$group":{"_id":"$id","count":{"$sum":1}}},{"$match":{"count":{"$gt": 1}}},{"$count": "r"}]
cur=db.twitter_search.aggregate(exp)
f=list(cur)
c=str(f)
d=c.split(" ")
e=str(d[1])
redundant_data=e[0]
print("Count of Ids with  Redundant Data:",redundant_data)
#Amount of retweets in the dataset
retweets_count=db.twitter_search.find({"retweeted_status":{"$exists": True}}).count()
print ("Amount of retweets:",retweets_count)
#Amount of quotes in the dataset
quotes_count=db.twitter_search.find({"is_quote_status":True}).count()
print ("Amount of quotes:",quotes_count)
print ("---------End of Twitter  Data Analytics------------")
# Data Analytics of Twitter Data End
#Program to show Data Analytics of Twitter Data Crawled via Streaming API and REST API end

#Saving the Data Analytics Result to witter_DataAnalytics_DataAnalytics.txt
twitter_plus_data=[total_data,geo_tagged_count,geo_tagged_glasgow_count,redundant_data,retweets_count,quotes_count]
f = open(r'C:\Users\SOUMITA\PycharmProjects\Webscience_CourseWork_Final\Twitter_DataAnalytics.txt','w')
f.write("---------Start of Twitter  Data Analytics------------\n")
f.write("Total Amount of Data collected:")
f.write(repr(twitter_plus_data[0]))
f.write("\n")
f.write("Amount of geo-tagged data:")
f.write(repr(twitter_plus_data[1]))
f.write("\n")
f.write("Amount of geo-tagged data from Glasgow:")
f.write(repr(twitter_plus_data[2]))
f.write("\n")
f.write("Amount of Redundant Data:")
f.write((twitter_plus_data[3]))
f.write("\n")
f.write("Amount of Retweets:")
f.write(repr(twitter_plus_data[4]))
f.write("\n")
f.write("Amount of Quotes:")
f.write(repr(twitter_plus_data[5]))
f.write("\n")
f.write('---------End of Twitter Data Analytics------------')
f.close()
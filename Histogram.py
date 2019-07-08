import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
database = 'mongodb://localhost/webscience'
client = MongoClient(database)
db = client.webscience
data = db.twitter_search.find()
#Graph to show Amount data collected at an interval of 10 mins start
count1=np.zeros(6)
count_total=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}).count()
print(count_total)
count1[0]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:07:00 +0000 2018'}}).count()
count1[1]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 06:07:00 +0000 2018','$lte':'Mon Nov 19 06:17:00 +0000 2018'}}).count()
count1[2]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 06:17:00 +0000 2018','$lte':'Mon Nov 19 06:27:00 +0000 2018'}}).count()
count1[3]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 06:27:00 +0000 2018','$lte':'Mon Nov 19 06:37:00 +0000 2018'}}).count()
count1[4]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 06:37:00 +0000 2018','$lte':'Mon Nov 19 06:47:00 +0000 2018'}}).count()
count1[5]=db.twitter_search.find({'created_at':{'$gte':'Mon Nov 19 06:47:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}).count()
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlabel("Time Interval of Tweets")  # x-axis label
ax.set_ylabel("Counts of Tweets")        # y-axis label
ax.set_title("Graph to show Time Vs Count of Tweets")
ax.bar(range(len(count1)),count1)
plt.show()
#Graph to show Amount of redundant data collected at an interval of 10 mins start

#Graph to show Amount of rtwedundant data collected at an interval of 10 mins end

#Graph to show Amount of geo-tagged data collected at an interval of 10 mins start
count_geotagged=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 18 06:57:00 +0000 2018'}}]}).count()
print(count_geotagged)
#Graph to show Amount of geo-tagged data collected at an interval of 10 mins stop
count2=np.zeros(6)
count2[0]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:07:00 +0000 2018'}}]}).count()
count2[1]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 06:07:00 +0000 2018','$lte':'Mon Nov 19 06:17:00 +0000 2018'}}]}).count()
count2[2]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 06:17:00 +0000 2018','$lte':'Mon Nov 19 06:27:00 +0000 2018'}}]}).count()
count2[3]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 06:27:00 +0000 2018','$lte':'Mon Nov 19 06:37:00 +0000 2018'}}]}).count()
count2[4]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 06:37:00 +0000 2018','$lte':'Mon Nov 19 06:47:00 +0000 2018'}}]}).count()
count2[5]=db.twitter_search.find({"$and":[{"user.geo_enabled": True},{"place.id": "791e00bcadc4615f"},{'created_at':{'$gte':'Mon Nov 19 06:47:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}]}).count()
fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)
ax1.set_xlabel("Time Interval of Tweets")  # x-axis label)
ax1.set_ylabel("Counts of geo-tagged Tweets in Glasgow")# y-axis label
ax1.set_title("Graph to show Time Vs Count of geo-tagged Tweets in Glasgow")
ax1.bar(range(len(count2)),count2)
plt.show()

#Graph to show Amount of retweets collected at an interval of 10 mins start
count_retweet=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}]}).count()
print(count_retweet)
count3=np.zeros(6)
count3[0]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:07:00 +0000 2018'}}]}).count()
count3[1]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 06:07:00 +0000 2018','$lte':'Mon Nov 19 06:17:00 +0000 2018'}}]}).count()
count3[2]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 06:17:00 +0000 2018','$lte':'Mon Nov 19 06:27:00 +0000 2018'}}]}).count()
count3[3]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 06:27:00 +0000 2018','$lte':'Mon Nov 19 06:37:00 +0000 2018'}}]}).count()
count3[4]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 06:37:00 +0000 2018','$lte':'Mon Nov 19 06:47:00 +0000 2018'}}]}).count()
count3[5]=db.twitter_search.find({"$and":[{"retweeted_status":{"$exists": True}},{'created_at':{'$gte':'Mon Nov 19 06:47:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}]}).count()
fig3=plt.figure()
ax3=fig3.add_subplot(1,1,1)
ax3.set_xlabel("Time Interval of Tweets")  # x-axis label)
ax3.set_ylabel("Counts of retweets")# y-axis label
ax3.set_title("Graph to show Time Vs Count of Tweets of Retweets")
ax3.bar(range(len(count3)),count3)
plt.show()
#Graph to show Amount of redundant data collected at an interval of 10 mins start
##############################################################
#Graph to show Amount of redundant data collected at an interval of 10 mins stop
#Graph to show Amount of quotes collected at an interval of 10 mins start
count_quotes=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}]}).count()
print(count_quotes)
count4=np.zeros(6)
count4[0]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 05:57:00 +0000 2018','$lte':'Mon Nov 19 06:07:00 +0000 2018'}}]}).count()
count4[1]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 06:07:00 +0000 2018','$lte':'Mon Nov 19 06:17:00 +0000 2018'}}]}).count()
count4[2]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 06:17:00 +0000 2018','$lte':'Mon Nov 19 06:27:00 +0000 2018'}}]}).count()
count4[3]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 06:27:00 +0000 2018','$lte':'Mon Nov 19 06:37:00 +0000 2018'}}]}).count()
count4[4]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 06:37:00 +0000 2018','$lte':'Mon Nov 19 06:47:00 +0000 2018'}}]}).count()
count4[5]=db.twitter_search.find({"$and":[{"is_quote_status":True},{'created_at':{'$gte':'Mon Nov 19 06:47:00 +0000 2018','$lte':'Mon Nov 19 06:57:00 +0000 2018'}}]}).count()
fig4=plt.figure()
ax4=fig4.add_subplot(1,1,1)
ax4.set_xlabel("Time Interval of Tweets")  # x-axis label)
ax4.set_ylabel("Counts of quotes")# y-axis label
ax4.set_title("Graph to show Time Vs Count of Tweets of Quotes")
ax4.bar(range(len(count4)),count4)
plt.show()
#Graph to show Amount of quotes collected at an interval of 10 mins stop


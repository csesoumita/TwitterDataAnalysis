# TwitterDataAnalysis
Developed a software for performing web crawling from Twitter and
Google Plus and then produced data analysis on the acquired data.
-Crawled Twitter data using Streaming REST API via tweepy library.
-Also fetched geo-tagged data. Performed keyword based
-Calculated and visualized the amount of geo-tagged data from
Glasgow location , amount of redundant tweets, amount retweets
and quotes.
-Files Description:
1) StreamingAPI.py-Program for Crawling Twitter Data using Streaming API start(based of certain users and keywords)
2) StreamingAPI_sample_method.py-Program for Crawling Twitter Data using Streaming API start for 1% data (via sample method)
3) REST_API_Twitter.py-Program for Twitter Data Crawling via REST API using tweepy
4) Geo_Tagged_Data.py- Program for Geo-tagged data for Glasgow via Streaming API and REST API
5) DataAnalytics_Twitter.py - Program to gather the data statistics from Mongo DB.
6) Twitter_DataAnalytics.txt- Text file having Data statistics from Mongo DB.
7)Histogram.py - Program to show the visualizations of things like total tweel count, total redundant data collected, total retweets etc.
8) DataAnalytics_GUI.py - A GUI application buit on tkinter to generate the analysis and visualizations.

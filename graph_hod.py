import matplotlib.pyplot as plt 
import pandas as pd
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

tweets['ts'] = pd.to_datetime(tweets['timestamp'])

tweets['hod'] = [t.hour for t in tweets.ts]
tweets.hod.value_counts().plot(kind="bar")
plt.show()

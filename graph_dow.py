import matplotlib.pyplot as plt 
import pandas as pd
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

tweets['ts'] = pd.to_datetime(tweets['timestamp'])
def get_dayofweek(dow):
    if dow == 0:
        return 'Mo'
    elif dow == 1:
        return "Di"
    elif dow == 2:
        return "Mi"
    elif dow == 3:
        return "Do"
    elif dow == 4:
        return "Fr"
    elif dow == 5:
        return "Sa"
    elif dow == 6:
        return "So"

tweets['dow'] = [get_dayofweek(t.dayofweek) for t in tweets.ts]
tweets.dow.value_counts().plot(kind="bar")
plt.show()

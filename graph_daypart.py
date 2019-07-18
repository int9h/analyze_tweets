import pandas as pd
import matplotlib.pyplot as plt
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

tweets['ts'] = pd.to_datetime(tweets['timestamp'])
def get_daypart(hour):
    morning = range(6,12)
    day = range(13,19)
    evening = range(20,23)
    night = range(0,5)

    if hour in morning:
        return "Morning"
    elif hour in day:
        return "Day"
    elif hour in evening:
        return "Evening"
    elif hour in night:
        return "Night"

tweets['daypart'] = [get_daypart(t.hour) for t in tweets.ts]
tweets.daypart.value_counts().plot(kind="bar") 
plt.show()

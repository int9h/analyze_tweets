import matplotlib.pyplot as plt 
import pandas as pd
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

def tweet_length(text):
    if len(text) < 100:
        return "short"
    elif 100 <= len(text) <= 135:
        return "medium"
    else:
        return "long"

tweets['length'] = tweets["text"].apply(tweet_length)

tweets.length.value_counts().plot(kind="bar")
plt.show()

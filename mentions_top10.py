import pandas as pd
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

mention_dict = {}

for i in tweets.index:
    tweet = tweets.iloc[i]['text']
    if isinstance(tweet, str):
        tweet = tweet.split()
        for word in tweet:
            if(word[0:1] == "@" and len(word)>1):
                if word in mention_dict:
                    mention_dict[word] += 1
                else:
                    mention_dict[word] = 1

sorted_mentions = sorted(mention_dict.items(), key=lambda x: x[1])[::-1]
print("Top 10 Mentions")
for mention in sorted_mentions:
    print(mention[1], ': ', str(mention[0]))

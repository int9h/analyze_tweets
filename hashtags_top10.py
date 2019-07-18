import pandas as pd
from lib.LoadTweets import LoadTweets

tweets = LoadTweets.load('tweets.csv')

tag_dict = {}

for i in tweets.index:
    tweet = tweets.ix[i]['text']
    if isinstance(tweet, str):
        tweet = tweet.split()
        for word in tweet:
            if(word[0:1] == "#" and len(word)>1):
                if word in tag_dict:
                    tag_dict[word] += 1
                else:
                    tag_dict[word] = 1

sorted_tags = sorted(tag_dict.items(), key=lambda x: x[1])[::-1]
print("Top 10 Hashtags")

for ht in sorted_tags[:10]:
    print(ht[1], ': ', str(ht[0]))

#!/usr/bin/env python3
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_vader(sentence):
    # calculate the negative, positive, neutral and compound scores, plus verbal evaluation
    # adapted from https://towardsdatascience.com/the-most-favorable-pre-trained-sentiment-classifiers-in-python-9107c06442c6

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = sentiment_dict['neg']
    neutral = sentiment_dict['neu']
    positive = sentiment_dict['pos']
    compound = sentiment_dict['compound']
    if sentiment_dict['compound'] >= 0.05:
        overall_sentiment = "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"
    return negative, neutral, positive, compound, overall_sentiment


feeds = {'nytimes_world': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
         'bbc_world': 'http://feeds.bbci.co.uk/news/world/rss.xml'
         }

positive = []
negative = []
for feed_url in feeds.values():
    print(feed_url)
    for entry in feedparser.parse(feed_url).entries:
        _, _, _, score, sentiment = sentiment_vader(entry.summary)-
        if sentiment == 'Positive' and score > 0.5:
            positive.append(entry.title)
        if sentiment == 'Negative' and score < -0.5:
            negative.append(entry.title)

print("\nPositive:\n")
for title in positive:
    print(f"- {title}")

print("\nNegative:\n")
for title in negative:
    print(f"- {title}")

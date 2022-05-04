#!/usr/bin/env python3
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_vader(sentence):
    #calculate the negative, positive, neutral and compound scores, plus verbal evaluation
    # from https://towardsdatascience.com/the-most-favorable-pre-trained-sentiment-classifiers-in-python-9107c06442c6

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


feeds = {'google': 'https://news.google.com/rss'}
positive = []
negative = []
for feed_url in feeds.values():
    print(feed_url)
    for entry in feedparser.parse(feed_url).entries:
        _, _, _, _, sentiment = sentiment_vader(entry.title)
        if sentiment == 'Positive':
            positive.append(entry.title)
        if sentiment == 'Negative':
            negative.append(entry.title)

print("Positive:\n")
for title in positive:
    print(f"- {title}")

print("Negative:\n")
for title in negative:
    print(f"- {title}")
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re

nltk.download('vader_lexicon', quiet=True)
_sia = SentimentIntensityAnalyzer()

def _clean_headline(text):
    text = re.sub(r'\([A-Z]{1,6}\)', '', text)
    return text.strip()

def analyze_sentiment(df, headline_col='headline', threshold=0.05):
    df = df.copy()
    df[headline_col] = df[headline_col].astype(str).apply(_clean_headline)
    scores = df[headline_col].apply(lambda x: _sia.polarity_scores(x))
    df['neg'] = scores.apply(lambda s: s['neg'])
    df['neu'] = scores.apply(lambda s: s['neu'])
    df['pos'] = scores.apply(lambda s: s['pos'])
    df['compound'] = scores.apply(lambda s: s['compound'])
    def label(c):
        if c > threshold:
            return 'positive'
        elif c < -threshold:
            return 'negative'
        else:
            return 'neutral'
    df['sentiment'] = df['compound'].apply(label)
    return df
import pandas as pd
from src.sentiment import analyze_sentiment
def test_sentiment_basic():
    df = pd.DataFrame({"headline": ["Stocks rally as earnings beat expectations", "Company files for bankruptcy amid turmoil"]})
    out = analyze_sentiment(df)
    assert set(out['sentiment']).issubset({'positive','negative','neutral'})
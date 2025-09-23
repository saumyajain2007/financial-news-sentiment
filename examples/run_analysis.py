from src.scraper import fetch_news_headlines
from src.sentiment import analyze_sentiment
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", default="AAPL")
    args = parser.parse_args()
    df = fetch_news_headlines(args.ticker, limit_per_source=5)
    df2 = analyze_sentiment(df)
    print(df2[['source','headline','compound','sentiment']].to_string(index=False))

if __name__ == "__main__":
    main()
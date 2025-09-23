import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_news_yahoo(ticker, limit=10):
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []
    for a in soup.select("h3 a")[:limit]:
        text = a.get_text().strip()
        items.append({"source": "yahoo", "headline": text, "link": a.get('href')})
    return pd.DataFrame(items)

def fetch_news_google(ticker, limit=10):
    q = f"{ticker} stock"
    url = f"https://news.google.com/rss/search?q={requests.utils.quote(q)}"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(resp.content, "xml")
    items = []
    for item in soup.find_all("item")[:limit]:
        title = item.title.get_text()
        link = item.link.get_text()
        items.append({"source": "google", "headline": title, "link": link})
    return pd.DataFrame(items)

def fetch_news_marketwatch(ticker, limit=10):
    url = f"https://www.marketwatch.com/search?q={requests.utils.quote(ticker)}&m=Search&sd=All"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []
    for el in soup.select(".searchresult__title a")[:limit]:
        title = el.get_text().strip()
        link = el.get('href')
        items.append({"source": "marketwatch", "headline": title, "link": link})
    return pd.DataFrame(items)

def fetch_news_headlines(ticker, limit_per_source=10, sources=None):
    if sources is None:
        sources = ["yahoo", "google", "marketwatch"]
    frames = []
    if "yahoo" in sources:
        try:
            frames.append(fetch_news_yahoo(ticker, limit_per_source))
        except Exception:
            pass
    if "google" in sources:
        try:
            frames.append(fetch_news_google(ticker, limit_per_source))
        except Exception:
            pass
    if "marketwatch" in sources:
        try:
            frames.append(fetch_news_marketwatch(ticker, limit_per_source))
        except Exception:
            pass
    if not frames:
        return pd.DataFrame(columns=["source","headline","link"])
    df = pd.concat(frames, ignore_index=True)
    df['headline'] = df['headline'].str.replace(r'\\s+', ' ', regex=True).str.strip()
    df = df.drop_duplicates(subset=['headline'])
    return df.reset_index(drop=True)
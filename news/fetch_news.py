import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_top_news(max_articles=5):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=india&language=en&sortBy=publishedAt&pageSize={max_articles}&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"❌ Error: {data.get('message')}")
        return []

    return data.get("articles", [])

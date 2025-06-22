import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    print("❌ NEWS_API_KEY not found in .env")
    exit()

url = f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print(f"❌ API request failed: {data.get('message')}")
    exit()

articles = data.get("articles", [])
if not articles:
    print("⚠️ No articles found. Check filters, rate limit, or API key.")
else:
    print("✅ Sample article:")
    print(articles[0]['title'])

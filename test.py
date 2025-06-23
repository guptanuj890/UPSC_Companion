from newsapi import NewsApiClient
import os 
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("api_key")
newsapi = NewsApiClient(api_key=api_key)
top_headlines = newsapi.get_top_headlines(language='en', category='general', page_size=10)

print("Top 10  News Headlines:")
if top_headlines and top_headlines['articles']:
    for article in top_headlines['articles']:
        print(f"- {article['title']}: {article['url']} :{article['content']}")
else:
    print("Could not retrieve top headlines for politics.")
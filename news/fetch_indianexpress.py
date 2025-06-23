import feedparser
from newspaper import Article

def get_indianexpress_articles(max_articles=10):
    rss_url = "https://indianexpress.com/section/india/feed/"
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries[:max_articles]:
        try:
            article = Article(entry.link)
            article.download()
            article.parse()
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "content": article.text
            })
        except Exception as e:
            print(f"❌ Failed to extract article from {entry.link}: {e}")
    return articles


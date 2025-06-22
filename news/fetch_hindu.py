import feedparser
from newspaper import Article

def get_hindu_articles(max_articles=5):
    rss_url = "https://www.thehindu.com/news/national/feeder/default.rss"
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


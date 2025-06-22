import streamlit as st
from news.fetch_news import get_top_news
from chains.summarizer_chain import summarize_article
from chains.question_chain import generate_questions

st.set_page_config(page_title="UPSC News Companion", layout="wide")
st.title("📰 UPSC News Companion")
st.markdown("Get summaries and questions from the latest news, optimized for UPSC preparation.")

# Fetch top 5 news articles
with st.spinner("Fetching latest news..."):
    articles = get_top_news()

if not articles:
    st.warning("⚠️ No articles found. Please check your NewsAPI key or try again later.")
else:
    for idx, article in enumerate(articles, 1):
        title = article.get("title", "Untitled")
        content = (
            article.get("content") or
            article.get("description") or
            article.get("summary") or
            ""
        )

        with st.expander(f"🔹 {idx}. {title}", expanded=False):
            st.markdown(f"**🔗 Source:** [Read more]({article.get('url', '#')})")

            with st.spinner("Generating summary..."):
                try:
                    summary = summarize_article(content)
                    st.subheader("📝 Summary")
                    st.markdown(summary.strip())
                except Exception as e:
                    st.error(f"Error generating summary: {e}")
                    continue

            with st.spinner("Generating UPSC-style questions..."):
                try:
                    questions = generate_questions(summary)
                    st.subheader("❓ Questions")
                    st.markdown(questions.strip())
                except Exception as e:
                    st.error(f"Error generating questions: {e}")

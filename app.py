import streamlit as st
from news.fetch_hindu import get_hindu_articles
from chains.summarizer_chain import summarize_article
from chains.question_chain import generate_questions
from chains.classifier_chain import classify_topic

st.set_page_config(page_title="UPSC News Companion", layout="wide")
st.title("📚 UPSC News Companion")
st.markdown("Get categorized summaries and MCQs from the latest news for UPSC preparation.")

# Fetch articles
with st.spinner("Fetching and analyzing top news from The Hindu..."):
    articles = get_hindu_articles()

if not articles:
    st.warning("⚠️ No articles found.")
else:
    category_map = {
        "Indian Polity": [],
        "Indian Economy": [],
        "International Relations": [],
        "Social Issues": [],
        "Other": []
    }
    questions_list=[]
    summary_list=[]
    category_list=[]
    for article in articles:
        title = article["title"]
        link = article["link"]
        content = article["content"]

        try:
            summary = summarize_article(content)
            questions = generate_questions(summary)
            category = classify_topic(content)

            summary_list.append(summary)
            questions_list.append(questions)
            category_list.append(category)

        except Exception as e:
            st.error(f"⚠️ Error processing article: {title}\n{e}")
            continue

        category = category if category in category_map else "Other"
        category_map[category].append({
            "title": title,
            "summary": summary,
            "link": link
        })

    # Display categorized output
    for cat, items in category_map.items():
        if items:
            with st.expander(f"📘 {cat} ({len(items)} articles)", expanded=False):
                for idx, item in enumerate(items, 1):
                    st.markdown(f"### {idx}. {item['title']}")
                    st.markdown(f"🔗 [Read Full Article]({item['link']})")
                    st.markdown(f"**📝 Summary:**\n{item['summary'].strip()}")
                    st.markdown("---")
    for questions in questions_list:
        st.markdown(questions)
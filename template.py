import os

# Define folder structure directly in current directory
folders = [
    "data",
    "news",
    "chains",
    "utils",
    "components",
    "assets"
]

# Define files with boilerplate content (relative to root)
files = {
    "app.py": """import streamlit as st

st.title("UPSC News Digest App")

st.write("This is the main entry point for the Streamlit app.")
""",

    "config.py": '''# Add your API keys here
NEWS_API_KEY = "your_news_api_key"
GEMINI_API_KEY = "your_gemini_api_key"
''',

    "requirements.txt": """streamlit
langchain
google-generativeai
requests
python-dotenv
""",

    "README.md": """# UPSC News Digest App

A tool for UPSC aspirants that fetches daily news, summarizes it using Gemini, and generates questions using LangChain.

## Features
- Daily news summarization
- UPSC-style question generation
- Simple UI with Streamlit
""",

    "data/summaries.json": "[]",
    "data/questions.json": "[]",

    "news/fetch_news.py": '''import requests
from config import NEWS_API_KEY

def get_top_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])
''',

    "chains/summarizer_chain.py": '''from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

summarize_prompt = PromptTemplate(
    input_variables=["article"],
    template="Summarize this news article for UPSC preparation: {article}"
)

summarizer_chain = LLMChain(llm=llm, prompt=summarize_prompt)

def summarize_article(article):
    return summarizer_chain.run(article=article)
''',

    "chains/question_chain.py": '''from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

question_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Generate 2 UPSC-level MCQs based on this summary: {summary}"
)

question_chain = LLMChain(llm=llm, prompt=question_prompt)

def generate_questions(summary):
    return question_chain.run(summary=summary)
''',

    "utils/text_cleaner.py": '''def clean_text(text):
    return text.replace("\\n", " ").strip()
''',

    "utils/topic_classifier.py": '''def classify_topic(summary):
    if "parliament" in summary.lower():
        return "Polity"
    elif "economy" in summary.lower():
        return "Economy"
    else:
        return "General Studies"
''',

    "components/news_card.py": '''import streamlit as st

def display_news_card(title, summary, questions):
    st.subheader(title)
    st.write(summary)
    st.markdown("**Questions:**")
    st.write(questions)
''',

    "assets/logo.png": None  # placeholder; won't write binary content
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        if content:
            f.write(content)

print("✅ Project structure created directly in the current folder.")

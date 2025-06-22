from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load Gemini API key from .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ✅ Explicitly pass the Gemini API key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)

classifier_prompt = PromptTemplate(
    input_variables=["article"],
    template="""
You are an expert UPSC news classifier.

Given this article, classify it into one of the following categories:
- Indian Polity
- Indian Economy
- International Relations
- Social Issues
- Other

Only respond with one category name.

Article:
{article}
"""
)

classifier_chain = LLMChain(llm=llm, prompt=classifier_prompt)

def classify_topic(article_text):
    return classifier_chain.run(article=article_text).strip()

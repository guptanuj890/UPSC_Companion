import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load Gemini API key from .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ✅ Explicitly pass the Gemini API key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)

# Prompt and summarizer chain
summarize_prompt = PromptTemplate(
    input_variables=["article"],
    template="Summarize this news article for UPSC preparation in 3 bullet points:\n\n{article}"
)

summarizer_chain = LLMChain(llm=llm, prompt=summarize_prompt)

def summarize_article(article):
    return summarizer_chain.run(article=article)


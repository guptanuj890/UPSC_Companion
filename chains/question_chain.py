from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)

question_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
You are a UPSC exam expert. Based on the following news summary, create **2 UPSC-level multiple-choice questions (MCQs)**.
Each should include 4 options and clearly mark the correct one.

If information is partial, extrapolate from context with care.

Summary:
{summary}
"""
)

question_chain = LLMChain(llm=llm, prompt=question_prompt)

def generate_questions(summary):
    return question_chain.run(summary=summary)

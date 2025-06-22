import streamlit as st

def display_news_card(title, summary, questions):
    st.subheader(title)
    st.write(summary)
    st.markdown("**Questions:**")
    st.write(questions)

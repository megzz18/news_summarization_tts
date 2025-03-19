import streamlit as st
import requests
from utils import scrape_news


st.title("News Summarization & TTS")

company = st.text_input("Enter Company Name")

if st.button("Fetch News"):
    response = requests.get(f"http://127.0.0.1:8000/scrape?company={company}")
    data = response.json()

    for article in data["articles"]:
        st.subheader(article["title"])
        st.write("Sentiment:", article["sentiment"])

if st.button("Generate Hindi Audio"):
    response = requests.get(f"http://127.0.0.1:8000/tts?text={company} latest news summary")
    st.audio(response.json()["audio_file"])
articles = scrape_news("Tesla")
print(articles)  # This will print the scraped news in the terminal

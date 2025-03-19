from fastapi import FastAPI
from utils import scrape_news, analyze_sentiment, comparative_analysis, text_to_speech

app = FastAPI()

@app.get("/scrape")
def get_news(company: str):
    articles = scrape_news(company)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])  
    return {"articles": articles}

@app.post("/analyze")
def analyze(articles: list):
    sentiment_summary = comparative_analysis(articles)
    return {"sentiment_summary": sentiment_summary}

@app.get("/tts")
def get_tts(text: str):
    filename = text_to_speech(text)
    return {"audio_file": filename}

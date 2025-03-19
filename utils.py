import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from gtts import gTTS

nltk.download("vader_lexicon")

def scrape_news(company):
    search_url = f"https://news.google.com/search?q={company}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("h3")[:10]:  
        title = item.text
        if item.a and "href" in item.a.attrs:
            link = "https://news.google.com" + item.a["href"][1:]
        else:
            link = None  # or continue to skip this item
        
        articles.append({"title": title, "link": link})  # Moved outside the if-else block

    return articles

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)

    if sentiment_score["compound"] >= 0.05:
        return "Positive"
    elif sentiment_score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def comparative_analysis(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in articles:
        sentiment = analyze_sentiment(article["title"])  # Ensure sentiment analysis is applied
        sentiment_counts[sentiment] += 1

    return sentiment_counts

def text_to_speech(text, filename="static/output.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename

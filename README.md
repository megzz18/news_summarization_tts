HEAD
# news_summarization_tts

# News Summarization & Text-to-Speech (TTS) App

##  Project Overview
This is a web-based application that extracts news articles related to a given company, analyzes the sentiment, performs comparative analysis, and converts the summarized content into **Hindi speech**.  

### Features:
- **News Extraction**: Scrapes top 10 news articles using `BeautifulSoup`.
- **Sentiment Analysis**: Categorizes each article as **Positive, Negative, or Neutral**.
- **Comparative Analysis**: Highlights sentiment trends and differences.
- **Text-to-Speech (TTS)**: Converts summarized content into Hindi using an open-source TTS model.
- **User Interface**: Built with `Streamlit`/`Gradio` for easy interaction.
- **Deployment**: Hosted on Hugging Face Spaces.

---

## Tech Stack
- **Backend**: Python (Flask/FastAPI for API)
- **Frontend**: Streamlit/Gradio
- **Web Scraping**: BeautifulSoup
- **Sentiment Analysis**: VADER/ TextBlob
- **TTS (Text-to-Speech)**: gTTS / Coqui TTS
- **Deployment**: Hugging Face Spaces

---

## Installation & Setup

### Prerequisites
- Install Python (>=3.8)
- Install dependencies

###  Clone the repository:
```sh
git clone https://github.com/YOUR-USERNAME/news_summarization_tts.git
cd news_summarization_tts
>>>>>>> a378fce (Initial commit - News Summarization and TTS App)

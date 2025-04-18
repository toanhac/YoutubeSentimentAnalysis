
# 🎬 YouTube Sentiment Analyzer with Custom Fine-tuned Model

An AI-powered web app that analyzes viewer sentiment from YouTube video comments using a fine-tuned BERT model. Supports multilingual input with automatic translation and provides insightful visualizations and summaries.

## 🚀 Features

- 🔗 Input any YouTube video URL
- 💬 Crawl and process all comments
- 🌍 Translate non-English comments using Google Translate API
- 🤖 Fine-tuned BERT model for sentiment classification (Negative, Neutral, Positive)
- 📊 Visualize results in real-time using pie charts
- 🧠 Generate smart summaries with optional LLM integration
- 🌐 Built with Streamlit for fast, interactive deployment

## 🧠 Model

- **Base model**: [`bert-base-uncased`](https://huggingface.co/bert-base-uncased)
- **Fine-tuned on**: [GoEmotions dataset](https://github.com/google-research/google-research/tree/master/goemotions) (mapped to 3 sentiment classes)
- **Framework**: Hugging Face Transformers + PyTorch

## 📦 Tech Stack

- `Python`, `PyTorch`, `Transformers`, `Googletrans`
- `Streamlit` for UI
- `Matplotlib` for visualizations
- `YouTube API` for comment crawling

## 🖥️ Demo

> Not Ready :v

## 📁 Folder Structure


```
YoutubeSentimentAnalysis/
├── .venv/                        # Virtual environment (not pushed to Git)
├── my_sentiment_model/          # Folder containing the fine-tuned BERT model
├── services/                    # Core logic modules
│   ├── __init__.py
│   ├── llm_summarizer.py        # Optional LLM-based summary generator
│   ├── sentiment_analyzer.py    # Interface for analyzing sentiment
│   ├── transformer_sentiment.py # Loads and runs the custom BERT model
│   ├── translator.py            # Google Translate API wrapper
│   └── youtube_crawler.py       # Crawls YouTube comments
├── utils/                       # Utility functions
│   ├── __init__.py
│   └── helpers.py
├── .gitignore
├── app.py                       # Streamlit app entrypoint
├── config.py                    # Configuration (API keys, settings, etc.)
├── requirements.txt             # Required Python packages
└── train.py                     # Script to fine-tune the sentiment model
```

## ⚙️ Setup

1. **Clone this repo**  
   ```bash
   https://github.com/toanhac/YoutubeSentimentAnalysis.git
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```bash
   streamlit run app.py
   ```

4. **(Optional)**: Fine-tune model from scratch  
   ```bash
   python train.py
   ```

## 📝 Example Usage

Paste a YouTube link into the app, and you'll get:
- Language-detected comments (translated if needed)
- Sentiment classification results
- Pie chart visualization
- Overall summary/comment insights

## 🧪 Future Improvements

- Deploy online (Streamlit Cloud / Hugging Face Spaces)
- Add emotion-level classification (e.g., joy, anger)
- Allow user-defined label mapping
- Improve LLM summarization


---

Made with ❤️ by ToanHac

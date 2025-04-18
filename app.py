import streamlit as st
from services.youtube_crawler import get_comments
from services.sentiment_analyzer import analyze_sentiment
from services.llm_summarizer import summarize_comments_with_sentiment
from services.transformer_sentiment import analyze_sentiments_with_finetuned_model
from services.translator import translate_comments_to_english
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="YouTube Sentiment Analysis", layout="centered")
st.title("YouTube Video Sentiment Analysis")

youtube_url = st.text_input("Enter a YouTube video URL:")

if st.button("OK"):
    if "watch?v=" not in youtube_url:
        st.error("Invalid YouTube URL. Please enter a full URL like: https://www.youtube.com/watch?v=VIDEO_ID")
    else:
        video_id = youtube_url.split("watch?v=")[-1].split("&")[0]

        with st.spinner("Fetching comments from YouTube..."):
            comments = get_comments(video_id, max_results=100)
            translated_comments = translate_comments_to_english(comments)
        if not comments:
            st.warning("No comments found on this video.")
        else:
            st.success(f"Successfully retrieved {len(translated_comments)} comments.")
            st.subheader("Sentiment Analysis")

            sentiment_result = analyze_sentiment(translated_comments)
            # sentiment_result = analyze_sentiments_with_finetuned_model(translated_comments)
            st.json(sentiment_result)

            # Plot pie chart
            st.subheader("Sentiment Distribution")
            labels = ["Positive", "Neutral", "Negative"]
            values = [sentiment_result["Positive"], sentiment_result["Neutral"], sentiment_result["Negative"]]
            colors = ["#8BC34A", "#2196F3", "#F44336"]

            values = [v if v is not None and not np.isnan(v) else 0 for v in values]

            if sum(values) == 0:
                st.warning("No sentiment data to display.")
            else:
                fig, ax = plt.subplots()
                colors = ["#FF6B6B", "#FFD93D", "#6BCB77"]
                ax.pie(values, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
                ax.axis("equal")
                st.pyplot(fig)

            # fig, ax = plt.subplots()
            # ax.pie(values, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
            # ax.axis("equal")
            # st.pyplot(fig)

            # Use LLM to summarize
            st.subheader("AI Summary of Viewer Sentiment")
            summary = summarize_comments_with_sentiment(translated_comments, sentiment_result)
            st.markdown(summary)

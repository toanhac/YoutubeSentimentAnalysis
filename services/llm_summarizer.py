import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def summarize_comments_with_sentiment(comments, sentiment_stats, max_comments=50):
    total = sentiment_stats["Total Comments"]
    positive = sentiment_stats["Positive"]
    neutral = sentiment_stats["Neutral"]
    negative = sentiment_stats["Negative"]

    sample_comments = "\n".join("- " + c for c in comments[:max_comments])

    prompt = f"""
Here is the sentiment analysis result from viewers of a YouTube video:

- Total comments: {total}
- Positive: {positive} ({(positive / total) * 100:.1f}%)
- Neutral: {neutral} ({(neutral / total) * 100:.1f}%)
- Negative: {negative} ({(negative / total) * 100:.1f}%)

Sample viewer comments:
{sample_comments}

Please summarize the overall sentiment and viewer impressions in a professional and concise paragraph.
"""

    response = model.generate_content(prompt)
    return response.text

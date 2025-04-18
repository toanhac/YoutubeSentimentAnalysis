from transformers import pipeline, BertForSequenceClassification, BertTokenizer

model_path = "my_sentiment_model"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiments_with_finetuned_model(comments):
    results = pipe(comments, truncation=True)
    summary = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for res in results:
        label = res['label'].lower()
        if "positive" in label:
            summary["Positive"] += 1
        elif "neutral" in label:
            summary["Neutral"] += 1
        elif "negative" in label:
            summary["Negative"] += 1
    summary["Total Comments"] = len(results)
    return summary

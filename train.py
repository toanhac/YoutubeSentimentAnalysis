from datasets import load_dataset
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch

print("Loading GoEmotions dataset...")
dataset = load_dataset("go_emotions")
train_data = dataset["train"]

positive = [1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 16, 20, 21, 22, 23]
negative = [8, 11, 12, 14, 15, 17, 18, 19, 24, 25, 26]
neutral = [0]

def convert_to_3_class(row):
    labels = row["labels"]
    if any(lab in positive for lab in labels):
        return 2  # positive
    elif any(lab in negative for lab in labels):
        return 0  # negative
    else:
        return 1  # neutral

train_data = train_data.filter(lambda row: len(row["labels"]) > 0)
train_data = train_data.map(lambda row: {"label_id": convert_to_3_class(row)})

print("Tokenizing...")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize_fn(example):
    tokens = tokenizer(example["text"], padding="max_length", truncation=True, max_length=128)
    tokens["labels"] = example["label_id"]
    return tokens

tokenized_data = train_data.map(tokenize_fn, batched=False)
tokenized_data.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

print("Initializing model...")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

training_args = TrainingArguments(
    output_dir="./my_sentiment_model",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    save_strategy="epoch",
    logging_steps=100,
    logging_dir="./logs",
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data,
)

print("Training...")
trainer.train()

print("Saving model...")
model.save_pretrained("./my_sentiment_model")
tokenizer.save_pretrained("./my_sentiment_model")

print("Done! Model saved to ./my_sentiment_model")

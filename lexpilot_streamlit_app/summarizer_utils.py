from transformers import pipeline

def load_summarizer_model():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        device=-1
    )

def summarize_text(model, text, max_length=150):
    if len(text.strip()) == 0:
        return ""
    return model(text, max_length=max_length)[0]['summary_text']

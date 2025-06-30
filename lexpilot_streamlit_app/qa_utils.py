from transformers import pipeline

def load_qa_model():
    return pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad",
        device=-1  # Use CPU (safe for Spaces)
    )

def get_answer(model, question, context):
    return model(question=question, context=context[:100000])

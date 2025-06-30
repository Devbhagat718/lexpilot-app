import os
import streamlit as st
import time
import torch
from tempfile import gettempdir
from pathlib import Path
import psutil

from qa_utils import load_qa_model, get_answer
from summarizer_utils import load_summarizer_model, summarize_text
from file_utils import extract_text_from_file

# Setup Streamlit
st.set_page_config(page_title="LexPilot Pro", layout="wide")

# Sidebar Info
with st.sidebar:
    st.title("LexPilot™")
    st.write("Smart document analyzer for contracts and legal docs.")
    st.markdown("---")
    st.text(f"Memory: {psutil.virtual_memory().percent}% used")
    st.text(f"CPU: {psutil.cpu_percent()}% used")
    st.text(f"Device: {'GPU ✅' if torch.cuda.is_available() else 'CPU ⚠️'}")

# Model Cache Setup
@st.cache_resource(ttl=3600)
def load_models():
    return {
        "qa": load_qa_model(),
        "summarizer": load_summarizer_model()
    }

models = load_models()

# Upload UI
st.title("📄 LexPilot Pro")

with st.expander("📤 Upload Document", expanded=True):
    uploaded_file = st.file_uploader("Choose PDF or DOCX", type=["pdf", "docx"])
    manual_text = st.text_area("Or paste your text here:", height=150)
    context = extract_text_from_file(uploaded_file) if uploaded_file else manual_text

# Tabs
tab1, tab2 = st.tabs(["🔍 Question Answering", "📝 Summarization"])

with tab1:
    question = st.text_input("Enter your question:")
    if question and context:
        with st.spinner("Answering..."):
            result = get_answer(models["qa"], question, context)
            st.success(f"Answer: {result['answer']}")
            st.progress(result['score'])
            st.caption(f"Confidence: {result['score']:.2%}")

with tab2:
    with st.form("summarization_form"):
        length = st.slider("Summary Length", 50, 300, 150)
        if st.form_submit_button("Summarize"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(models["summarizer"], context, max_length=length)
                st.success("Done!")
                st.markdown(summary)

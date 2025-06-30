---
title: LexPilot
emoji: 🛩️
colorFrom: red
colorTo: red
sdk: streamlit
sdk_version: 1.25.0
app_file: streamlit_app.py
pinned: false
---

# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).


# LexPilot Pro (Streamlit App)

Analyze legal documents with QA and summarization features using pre-trained Hugging Face models.

## Features

- Upload PDF or Word documents
- Ask natural language questions about content
- Generate concise summaries

## Run Locally

```bash
git clone https://huggingface.co/spaces/your-username/lexpilot-streamlit
cd lexpilot-streamlit
pip install -r requirements.txt
streamlit run streamlit_app.py
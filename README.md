# LexPilot Streamlit App 🛩️

## Overview

The **LexPilot Streamlit App** is an intelligent document analyzer designed for legal and contract documents. It provides **question answering** and **summarization** capabilities using state-of-the-art pre-trained models from Hugging Face. This application enables users to ask natural language questions about their uploaded documents and generate concise summaries for better understanding and decision-making.

---

## Features

- 📄 **Upload PDF or Word Documents**  
  Users can upload legal documents in `.pdf` or `.docx` format.

- 🔍 **Question Answering**  
  Allows users to ask natural language questions and receive precise answers based on the document content.

- 📝 **Summarization**  
  Generates concise and informative summaries from lengthy documents.

- 💻 **System Monitoring**  
  Displays memory, CPU usage, and device information (GPU/CPU status) in the sidebar.

---

## Architecture

### 1. **Frontend**  
Built using **Streamlit**, providing an interactive interface for file uploads, questions, and summaries.

### 2. **Backend**  
- **Question Answering:** Powered by `distilbert-base-cased-distilled-squad`.  
- **Summarization:** Utilizes `sshleifer/distilbart-cnn-12-6`.  
- **File Parsing:** Processes `.pdf` files using `PyPDF2` and `.docx` files using `python-docx`.

### 3. **Deployment**  
Deployed on Hugging Face Spaces using Docker for scalable and efficient hosting.

---

## File Structure

```plaintext
lexpilot_streamlit_app/
├── .env                    # Environment variables
├── Dockerfile              # Docker configuration for deployment
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── streamlit_app.py        # Main application logic
├── file_utils.py           # File handling utilities
├── qa_utils.py             # Question answering utilities
├── summarizer_utils.py     # Summarization utilities
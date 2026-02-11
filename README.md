# RAG-Based Question Answering System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system that answers user queries using information extracted from a PDF document. Instead of relying only on a language model’s pre-trained knowledge, the system retrieves relevant content from a document and generates responses based on that context. This approach improves accuracy and reduces hallucinated answers.

The project includes:
- PDF text extraction
- Text chunking
- Embedding generation using Sentence Transformers
- FAISS vector database for similarity search
- Context-based answer generation using a lightweight language model
- Streamlit web interface for user interaction

---

## Problem Statement
Large Language Models often generate generic or incorrect responses when asked domain-specific questions. The objective of this project is to:
- Accept user queries
- Retrieve relevant information from a document
- Generate answers grounded in the document content
- Improve reliability using Retrieval-Augmented Generation

---

## Dataset / Knowledge Source
Type: PDF document  
Source: Public educational material  

The dataset size exceeds GitHub’s 25 MB file limit.

Download the dataset from Google Drive:
(https://drive.google.com/file/d/1jhEth_cpT_EpGrSPTcS2tLB-_x9ug0Bw/view?usp=drive_link)

After downloading:
1. Rename the file as `ml_intro.pdf` (if necessary)
2. Place it in the project folder before running the application

---

## RAG Architecture
User Query  
→ Convert query to embedding  
→ FAISS similarity search  
→ Retrieve top relevant text chunks  
→ Combine context with query  
→ Pass to language model  
→ Generate final answer  

This ensures responses are based on the document rather than general model knowledge.

---

## Text Chunking Strategy
Chunk size: 500 characters  
Chunk overlap: 50 characters  

Reason:
- Maintains context continuity between chunks  
- Prevents information loss at chunk boundaries  
- Improves retrieval accuracy  
- Balances performance and memory usage  

---

## Embedding Model
Model used: sentence-transformers/all-MiniLM-L6-v2  

Reason:
- Lightweight and fast  
- Good semantic understanding  
- Works efficiently on CPU  
- Open-source and widely used for retrieval tasks  

---

## Vector Database
Vector store used: FAISS  

Advantages:
- Fast nearest-neighbor search  
- Efficient for large embedding collections  
- Works locally without external services  
- Easy integration with Python  

---

## Language Model
Model used: google/flan-t5-small  

Reason:
- Lightweight and efficient  
- Suitable for instruction-based tasks  
- Runs locally without GPU  
- Generates context-aware responses  

---

## Streamlit Interface
A Streamlit web application is included to provide an interactive user interface.

Features:
- Simple question input
- Context-based answer generation
- Fast local execution
- No external APIs required

To run the Streamlit app:

1. Install dependencies:
pip install streamlit sentence-transformers faiss-cpu pypdf transformers

2. Ensure `ml_intro.pdf` is in the project folder

3. Run:
streamlit run app.py

4. Open in browser:
http://localhost:8501

Note: The application is intended to run locally. Web hosting from Google Colab may not work reliably due to networking limitations.

---

## Notebook Implementation
The notebook includes step-by-step implementation:
1. Library installation  
2. PDF loading and text extraction  
3. Text chunking  
4. Embedding generation  
5. FAISS index creation  
6. Retrieval function  
7. RAG pipeline  
8. Minimum three test queries with outputs  

All steps include markdown explanations.

---

## Future Improvements
- Dynamic or semantic chunking  
- Hybrid search (keyword + semantic)  
- Reranking models for improved retrieval  
- Metadata filtering for multiple documents  
- Persistent vector database storage  
- Support for multiple file formats  
- Chat-style interface  
- Cloud deployment  

---

## Project Structure
RAG_Project/
- RAG_Notebook.ipynb
- app.py
- README.md
- ml_intro.pdf (download separately from Drive)

---

## Tools & Libraries Used
Python  
Streamlit  
Sentence Transformers  
FAISS  
HuggingFace Transformers  
PyPDF  
NumPy  
Google Colab / VS Code  

---

## How to Run the Project
1. Clone the repository  
2. Download the dataset from the Google Drive link  
3. Place the PDF in the project folder  
4. Install dependencies  
5. Run the notebook or launch the Streamlit app  

---

## Author
Name: Xiao  
Program: B.Tech  
Project: Retrieval-Augmented Generation (RAG) Assignment
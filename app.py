import streamlit as st
from pypdf import PdfReader
import os

# Page setup
st.set_page_config(page_title="RAG QA System")
st.title("RAG-Based Question Answering System")

# Local PDF path
file_path = "ml_intro.pdf"

# Load PDF text (lightweight)
@st.cache_resource
def load_documents(path):
    if not os.path.exists(path):
        return []

    reader = PdfReader(path)
    docs = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            docs.append(text)
    return docs

documents = load_documents(file_path)

if len(documents) == 0:
    st.error("PDF not found. Keep ml_intro.pdf in the same folder.")
    st.stop()

st.success(f"Loaded {len(documents)} pages from PDF")

# Simple retrieval (keyword-based for demo)
def simple_retrieve(query):
    for doc in documents:
        if query.lower() in doc.lower():
            return doc[:500]
    return documents[0][:500]

# UI
st.subheader("Ask a question")

query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query:
        with st.spinner("Generating answer..."):
            context = simple_retrieve(query)
            st.subheader("Answer")
            st.write(context)
    else:
        st.warning("Please enter a question.")
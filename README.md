# AI Lab Projects: Text Chunking Methods and BLIP Image Captioning

This repository contains two AI lab projects focused on document processing for Large Language Models (LLMs) and vision-language modeling using transformer architectures.

---

## Project 1: Multi-Level Text Chunking for LLM Applications

### Overview
This project explores and compares multiple text chunking strategies used to process large unstructured documents for LLM-based systems. The aim is to divide text into meaningful segments while preserving semantic and structural context, enabling efficient downstream tasks such as retrieval and question answering.

---

### Objective
To design and evaluate different chunking techniques that improve document handling within LLM token limits while maintaining contextual coherence.

---

### Chunking Methods Implemented

| Level | Method | Description |
|------|--------|-------------|
| 1 | Character Chunking | Fixed-size splitting based on character count |
| 2 | Recursive Chunking | Hierarchical splitting using paragraphs, lines, and words |
| 3 | Document-Specific Chunking | Structure-aware splitting for markdown and source code |
| 4 | Semantic Chunking | Embedding-based grouping using semantic similarity |
| 5 | Agentic Chunking | LLM-driven chunking based on contextual reasoning |

---

### Technologies Used
- Python  
- LangChain  
- Embedding Models  
- Vector Similarity (Cosine Similarity)  
- Unstructured Library (for PDF parsing)

---

### Key Features
- Efficient handling of long documents  
- Preservation of semantic meaning across chunks  
- Support for text, markdown, code, and PDFs  
- Improved retrieval performance in RAG systems  

---

### Applications
- Enterprise document search  
- AI research assistants  
- Knowledge-based chat systems  
- Document intelligence platforms  

---

### Conclusion
Advanced chunking strategies significantly enhance LLM-based systems by preserving document structure and semantic integrity, leading to improved information retrieval and model performance.

---

## Project 2: Fine-Tuning BLIP for Football Image Captioning

### Overview
This project fine-tunes a pre-trained BLIP (Bootstrapped Language-Image Pretraining) model to generate captions for football-related images. The model learns to produce meaningful textual descriptions by jointly understanding visual and linguistic information.

---

### Objective
To improve image captioning performance in the sports domain by fine-tuning a multimodal transformer model on a domain-specific dataset.

---

### Methodology

**Dataset**  
A football image-caption dataset sourced from Hugging Face.

**Data Preprocessing**
- Images converted into pixel embeddings  
- Captions tokenized using AutoProcessor  
- Custom PyTorch dataset used for efficient batching  

**Model**
BLIP Image Captioning Base model consisting of:
- Vision Encoder  
- Text Decoder  

**Training**
- Optimizer: AdamW  
- Loss Function: Cross-Entropy  
- Backpropagation using caption tokens as labels  

---

### Working
1. Input image is passed through the vision encoder to extract visual features.  
2. These visual embeddings are provided to the text decoder.  
3. During training, the decoder learns to map visual features to the correct caption tokens.  
4. During inference, the trained model generates captions token-by-token based solely on the image.  
5. Generated token IDs are decoded into natural language sentences.

---

### Technologies Used
- Python  
- PyTorch  
- Hugging Face Transformers  
- BLIP Model  
- AutoProcessor  

---

### Outcomes
- Generation of relevant football-specific captions  
- Improved domain-specific captioning accuracy  
- Demonstration of multimodal transformer effectiveness  
- Model suitable for deployment and reuse

---

### Future Scope
- Medical image captioning  
- Wildlife monitoring  
- Surveillance and security systems  

---

## Overall Learning Outcome
These projects demonstrate the effective use of multimodal AI systems for both text and image processing, combining language models, vision encoders, and intelligent preprocessing techniques to build practical AI applications.

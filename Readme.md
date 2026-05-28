# 📚 RAG Chatbot using LangChain, FAISS & Gemini

This project is a simple Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FAISS, Hugging Face embeddings, Gemini API, and Streamlit.

The chatbot can read PDF documents, store them in a vector database, and answer questions based only on the uploaded document content.

I built this project to learn how modern AI chatbots work with custom data and how vector databases are used in real-world LLM applications.

---

## 🚀 Features

* Chat with your own PDF documents
* Semantic search using FAISS
* Hugging Face sentence embeddings
* Gemini API integration
* Streamlit web interface
* Context-aware answers
* Fast document retrieval

---

## 🛠️ Technologies Used

* Python
* LangChain
* FAISS
* Hugging Face Embeddings
* Gemini API
* Streamlit

---

## 📂 Project Structure

```bash
gpt_rag_chat_bot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── data/
│   └── documents.pdf
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
└── indexing/
    └── ingest.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
cd gpt_rag_chat_bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Gemini API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get API key from:

[Google AI Studio](https://aistudio.google.com/app/apikey?utm_source=chatgpt.com)

---

## 📄 Add Your PDF

Place your PDF file inside the `data` folder.

Example:

```bash
data/documents.pdf
```

---

## 🧠 Create Vector Database

Run:

```bash
python indexing/ingest.py
```

This will:

* Load the PDF
* Split text into chunks
* Generate embeddings
* Create FAISS vector database

---

## ▶️ Run the Chatbot

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

## 💬 Example Questions

* What is this document about?
* Give me a summary
* What are the key points?
* Explain chapter 1

---

## 📸 Screenshots

You can add screenshots of your chatbot here later.

---

## 🌐 Deployment

This project can be deployed for free using:

* [Streamlit Community Cloud](https://share.streamlit.io?utm_source=chatgpt.com)
* [Hugging Face Spaces](https://huggingface.co/spaces?utm_source=chatgpt.com)

---

## 📌 Future Improvements

* Multiple PDF upload support
* Chat history
* Better UI design
* Source citations
* Support for DOCX and TXT files
* Conversational memory

---

## 🙌 Acknowledgement

This project was built for learning purposes to understand how Retrieval-Augmented Generation (RAG) systems work using modern LLM tools and vector databases.

---

## 📧 Contact

Feel free to connect with me on LinkedIn or GitHub.

import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

st.set_page_config(page_title="RAG Chatbot")

st.title("📚 RAG Chatbot")

# Load Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS
db = FAISS.load_local(
    "vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)

# Load Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

st.success("✅ Chatbot Ready")

# User Question
query = st.text_input("Ask a question about your document")

if query:

    with st.spinner("Searching..."):

        docs = db.similarity_search(query, k=3)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)

        with st.expander("Retrieved Chunks"):
            st.write(context)
📚 Conversational RAG - Intelligent PDF Chat

📖 Overview

This project is a Conversational Retrieval-Augmented Generation (RAG) application. It allows users to upload PDF documents and chat with them using natural language. Unlike standard RAG applications, this tool is state-aware, meaning it remembers the chat history and context, allowing for follow-up questions and a more natural conversation flow.

It leverages Groq's LPU inference engine for lightning-fast responses using the llama-3.1-8b-instant model and uses HuggingFace embeddings for vector search.

✨ Features

📄 Multi-PDF Support: Upload multiple PDF files at once to create a comprehensive knowledge base.

🧠 Context-Aware Chat: Rephrases user queries based on chat history to ensure the model understands follow-up questions.

⚡ High-Speed Inference: Uses Groq API for near-instant text generation.

🔍 Vector Search: Utilizes Chroma vector store and HuggingFace embeddings (all-MiniLM-L6-v2) for accurate document retrieval.

💾 Session Management: Maintains chat history within the active session.

🛠️ Tech Stack

Frontend: Streamlit

Orchestration: LangChain

LLM: Groq (Llama-3.1-8b-instant)

Embeddings: HuggingFace (all-MiniLM-L6-v2)

Vector DB: ChromaDB

🚀 Getting Started

Prerequisites

Python 3.9 or higher.

A Groq API Key (Get it here).

A HuggingFace Access Token (Get it here).

Installation

Clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


Create a virtual environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install dependencies:

pip install streamlit langchain langchain-groq langchain-openai langchain-community langchain-huggingface chromadb pypdf python-dotenv


Configuration

Create a .env file in the root directory.

Add your HuggingFace token to the file (Note: The code specifically looks for the variable name HF_TOKKEN):

HF_TOKKEN=your_huggingface_access_token_here


🏃‍♂️ Usage

Run the Streamlit application:

streamlit run app.py


Interact with the App:

Enter your Groq API Key in the sidebar input field.

Enter a Session ID (or use the default).

Upload one or more PDF files.

Start chatting! Ask questions about the content of your PDFs.

🧠 How It Works

Document Loading: The app loads PDFs using PyPDFLoader.

Splitting & Embedding: Text is split into chunks of 500 characters (with 200 overlap) and converted into vectors using HuggingFace embeddings.

Retrieval: These vectors are stored in ChromaDB. When you ask a question, the system finds the most relevant chunks.

History Awareness: A specialized chain (create_history_aware_retriever) reformulates your latest question based on previous messages to ensure the context is preserved (e.g., if you ask "What is his name?" after talking about a specific person).

Generation: The context and the reformulated question are sent to the Groq LLM to generate a concise answer.

🤝 Contributing

Contributions are welcome! Please follow these steps:

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📝 License

Distributed under the MIT License. See LICENSE for more information.

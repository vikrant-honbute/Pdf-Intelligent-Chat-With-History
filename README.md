📄 Conversational RAG — Intelligent PDF Chat

Conversational RAG is a State-Aware RAG (Retrieval-Augmented Generation) app built using ChromaDB, LangChain, HuggingFace Embeddings, and Groq LLM.

It allows you to upload multiple PDF documents and maintain a continuous conversation with them — the app remembers your chat history to provide context-aware answers.

🚀 Features

PDF Ingestion using PyPDFLoader

Text Chunking via RecursiveCharacterTextSplitter

Embeddings using HuggingFace (all-MiniLM-L6-v2)

Vector Search with ChromaDB

Intelligent Chat utilizing Groq (llama-3.1-8b-instant)

Context Awareness via RunnableWithMessageHistory

Session Management for maintaining chat state

📦 Installation

1. Clone the project

git clone [https://github.com/your-username/conversational-rag.git](https://github.com/your-username/conversational-rag.git)
cd conversational-rag


2. Create a virtual environment

python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate


3. Install dependencies

pip install streamlit langchain langchain-groq langchain-community langchain-huggingface chromadb pypdf python-dotenv


🔑 Environment Variables

Create a .env file in the root directory and add your HuggingFace token.

(Note: The code specifically looks for HF_TOKKEN as the variable name).

HF_TOKKEN=your_huggingface_access_token


Get your HF Access Token here: HuggingFace Settings

📘 How to Use

Run the app:

streamlit run app.py


Enter Groq API Key: In the input field provided on the screen, enter your Groq API Key (Get it here).

Set Session ID: Enter a generic Session ID (e.g., user1) to track your conversation history.

Upload PDFs: Use the file uploader to add your PDF documents.

Start Chatting: Ask questions! The system will reformulate your queries based on history and retrieve answers from the PDFs.

🧱 Tech Stack

Python

Streamlit

LangChain

ChromaDB

HuggingFace Embeddings

Groq LLM (Llama 3)

PyPDF

📁 Project Structure

Conversational-RAG/
│
├── app.py                 # Main application script
├── .env                   # Environment variables (HF Token)
├── requirements.txt       # Project dependencies
└── README.md              # Documentation


💡 Future Improvements

Add sidebar for better UI navigation

Support for different file formats (TXT, DOCX)

Option to select different Llama models

Clear chat history button

📝 License

MIT License — free to use and modify.

🙌 Credits

Built using LangChain, ChromaDB, HuggingFace, and Groq.

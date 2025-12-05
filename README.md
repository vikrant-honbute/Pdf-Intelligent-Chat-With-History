📄 Conversational RAG — PDF Intelligent Chat with History

Conversational RAG is a State-Aware RAG (Retrieval-Augmented Generation) app built using ChromaDB, LangChain, HuggingFace Embeddings, and Groq LLM.
It allows you to upload PDF documents and chat with them while maintaining the context of the conversation history.

🚀 Features

PDF ingestion via Streamlit File Uploader

Text chunking via RecursiveCharacterTextSplitter

Embeddings using HuggingFace (all-MiniLM-L6-v2)

Persistent Vector Search with ChromaDB

Answer generation using Groq (llama-3.1-8b-instant)

Chat History Awareness: Rephrases queries based on previous context

Session Management: Maintains distinct chat sessions via Session ID

📦 Installation

1. Clone the project

git clone [https://github.com/yourusername/Conversational-RAG.git](https://github.com/yourusername/Conversational-RAG.git)
cd Conversational-RAG


2. Create a virtual environment

python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


(Note: Ensure you have streamlit, langchain, langchain-groq, langchain-community, langchain-huggingface, chromadb, pypdf, and python-dotenv installed)

🔑 Environment Variables

Create a .env file in the root directory for your HuggingFace token:

HF_TOKKEN=your_huggingface_access_token


Get your HF Access Token here: https://huggingface.co/settings/tokens

(Note: The Groq API Key is entered directly in the App UI)

📘 How to Use

Run the app:

streamlit run app.py


Enter your Groq API Key in the input field. (Get it here: https://console.groq.com/keys)

Enter a Session ID (default is provided) to manage chat history.

Upload your PDF files using the file uploader.

Ask questions! The app will contextualize your query based on history and answer from the PDF.

🧱 Tech Stack

Python

Streamlit

LangChain (Core, Community, Groq, HuggingFace)

ChromaDB (Vector Store)

HuggingFace Embeddings (all-MiniLM-L6-v2)

Groq LLM (llama-3.1-8b-instant)

PyPDFLoader

📁 Project Structure

Conversational-RAG/
│
├── app.py                 # Main application script
├── .env                   # Environment variables (HF_TOKKEN)
├── requirements.txt       # Dependencies
└── README.md              # Documentation


💡 Future Improvements

Add "Clear History" button

Support for uploading multiple file types (txt, docx)

Sidebar for better session management

Export chat history

📝 License

MIT License — free to use and modify.

🙌 Credits

Built using LangChain, ChromaDB, HuggingFace, and Groq.

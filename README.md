Pdf-Intelligent-Chat-With-History

An intelligent conversational RAG (Retrieval-Augmented Generation) chatbot that lets you:

Upload one or more PDF files

Ask questions in natural language

Get context-aware answers grounded in the PDFs

Maintain chat history per session

Use Groq’s LLaMA 3.1 (8B Instant) for fast responses

Built with Streamlit, LangChain, ChromaDB, and Groq.

🚀 Features
📄 PDF Question Answering

Upload single or multiple PDFs

Load text using PyPDFLoader

Split documents into chunks using RecursiveCharacterTextSplitter

Create embeddings with HuggingFaceEmbeddings (all-MiniLM-L6-v2)

Store and search chunks using Chroma vector store

💬 Conversational RAG

Uses a history-aware retriever to rewrite the user query using chat history

Retrieves the most relevant chunks from your PDFs

Answers using the retrieved context

Keeps answers short and concise (≈3 sentences, as per system prompt)

⚡ Powered by Groq

Uses ChatGroq with model: llama-3.1-8b-instant

Very low latency → good interactive experience in Streamlit

🧠 Chat History per Session

Session-based chat memory using:

ChatMessageHistory

RunnableWithMessageHistory

Different session_id values → separate conversations

🖥 Streamlit UI

Input for Groq API key

File uploader for PDFs

Input for session ID

Text box for questions

Display of assistant answers and raw chat history

📂 Project Structure
project-root/
│── app.py                 # Main Streamlit application
│── requirements.txt       # Python dependencies
│── .env                   # API keys & secrets (not committed)
│── .gitignore             # Git ignore rules
│── README.md              # Project documentation
└── temp.pdf               # Temporary file created when processing uploads

🔐 Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here
HF_TOKKEN=your_huggingface_token_here   # optional, matches your code variable name


Note: your code uses HF_TOKKEN (with double “K”), so the .env key must match exactly.

🛠 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/vikrant-honbute/Pdf-Intelligent-Chat-With-History.git
cd Pdf-Intelligent-Chat-With-History

2️⃣ Create a Virtual Environment
python -m venv venv


Activate it (Windows):

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py


Then open the local URL shown in the terminal (usually http://localhost:8501).

🧩 How It Works (High Level)

User enters Groq API key in the UI.

User uploads one or more PDF files.

PDFs are:

Loaded with PyPDFLoader

Split into overlapping chunks by RecursiveCharacterTextSplitter

Converted into embeddings using HuggingFaceEmbeddings

Stored in a Chroma vector store.

User asks a question.

A history-aware retriever:

Reads past messages (chat_history)

Reformulates the question into a standalone query if needed.

Relevant chunks are retrieved from Chroma.

ChatGroq (LLaMA 3.1 8B Instant) generates an answer using:

System prompt

Retrieved context

Chat history.

The answer and messages are stored in ChatMessageHistory for that session.

💡 Tech Stack
Component	Technology
UI	Streamlit
LLM	Groq – LLaMA 3.1 8B Instant
Orchestration	LangChain (classic, core, community)
Vector Store	Chroma
Embeddings	HuggingFace MiniLM (all-MiniLM-L6-v2)
PDF Loader	PyPDFLoader
Memory	ChatMessageHistory + RunnableWithMessageHistory
🤝 Contributing

Issues, feature requests, and pull requests are welcome.

📜 License

This project is licensed under the MIT License.

⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.

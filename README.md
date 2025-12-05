# Pdf-Intelligent-Chat-With-History

An intelligent, conversational **RAG (Retrieval-Augmented Generation)** chatbot that lets you:

- Upload one or more **PDF files**
- Ask **questions in natural language**
- Get **accurate, context-aware answers**
- Maintain **chat history per session**
- Use **Groq’s LLaMA 3.1** model for fast responses

Built with **Streamlit**, **LangChain**, **ChromaDB**, and **Groq**.

---

## 🚀 Features

### 📄 PDF Question Answering
- Upload multiple PDF files
- Extract text using `PyPDFLoader`
- Split documents into chunks using `RecursiveCharacterTextSplitter`
- Generate embeddings with `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`)
- Store and search document chunks using **Chroma** vector store

### 💬 Conversational RAG
- Uses **history-aware retriever** to reformulate questions based on chat history
- Retrieves relevant chunks from PDF content
- Answers based on retrieved context
- Keeps responses short and concise (3 sentences max, as per system prompt)

### ⚡ Powered by Groq
- Uses `ChatGroq` with model: `llama-3.1-8b-instant`
- Fast and efficient inference for interactive Q&A

### 🧠 Chat History per Session
- Session-based chat memory using:
  - `ChatMessageHistory`
  - `RunnableWithMessageHistory`
- Different `session_id` values create separate chat histories

### 🖥 Streamlit UI
- Enter **Groq API key**
- Upload one or multiple PDFs
- Enter **session ID**
- Ask questions and view answers
- Inspect stored chat history

---

## 📂 Project Structure

Example structure:

```bash
project-root/
│── app.py                 # Main Streamlit app (your code)
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (not committed)
│── .gitignore             # Git ignore rules
│── README.md              # Project documentation
└── temp.pdf               # Temporary file for uploaded PDFs
🔐 Environment Variables
Create a .env file in the project root:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
HF_TOKKEN=your_huggingface_token_here   # if you use HuggingFace private models
Note: In your code you used HF_TOKKEN (double K). Make sure the same name is used in .env and os.environ.

🛠 Installation & Setup
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/vikrant-honbute/Pdf-Intelligent-Chat-With-History.git
cd Pdf-Intelligent-Chat-With-History
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
On Windows:

bash
Copy code
venv\Scripts\activate
(On macOS/Linux, use source venv/bin/activate)

3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create .env file
bash
Copy code
# in the project root
GROQ_API_KEY=your_groq_api_key
HF_TOKKEN=your_huggingface_token   # optional
5️⃣ Run the Streamlit app
bash
Copy code
streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501).

🧩 How It Works (High-Level Flow)
User enters Groq API key in the UI

User uploads one or more PDF files

PDFs are:

Loaded with PyPDFLoader

Split into chunks using RecursiveCharacterTextSplitter

Embedded using HuggingFaceEmbeddings

Stored in a Chroma vector store

User asks a question

A history-aware retriever:

Looks at previous chat messages

Reformulates the question (if needed) into a standalone query

Relevant document chunks are retrieved from Chroma

ChatGroq (LLaMA 3.1 8B Instant) generates an answer using:

System prompt

Retrieved context

Chat history

Answer and messages are stored in ChatMessageHistory for that session

💡 Tech Stack
Layer	Technology
UI	Streamlit
LLM	Groq – llama-3.1-8b-instant
Orchestration	LangChain (chains, prompts, memory)
Vector Store	Chroma
Embeddings	HuggingFace MiniLM (all-MiniLM-L6-v2)
PDF Loader	LangChain PyPDFLoader
Memory	ChatMessageHistory, RunnableWithMessageHistory

🧪 Possible Improvements
Add support for:

More file types (DOCX, TXT, etc.)

Persistent vector storage (Chroma on disk)

Add authentication for API key

Add option to clear chat history per session

Add token usage display or cost estimation

🤝 Contributing
Contributions, issues, and feature requests are welcome.
Feel free to fork the repo and open a pull request.

📜 License
This project is licensed under the MIT License.

⭐ Support
If you find this project helpful, please consider giving it a ⭐ on GitHub.

sql
Copy code

If you tell me **the exact final name** you want to show (for example:  
`PDF Intelligent Chat with History` vs `Pdf-Intelligent-Chat-With-History`), I can tweak the heading and desc

# Pdf-Intelligent-Chat-With-History

An intelligent conversational RAG (Retrieval-Augmented Generation) chatbot that allows users to upload PDF files and ask questions based on their content. The system uses Groq’s LLaMA 3.1 model, LangChain retrievers, Chroma vector storage, and Streamlit UI to provide accurate, context-aware answers with chat history support.

---

## 🚀 Features

### 📄 PDF Question Answering
- Upload single or multiple PDF files  
- Extract text using `PyPDFLoader`  
- Split documents into chunks with `RecursiveCharacterTextSplitter`  
- Generate embeddings using `HuggingFaceEmbeddings` (MiniLM-L6-v2)  
- Store and retrieve chunks via **ChromaDB**

### 💬 Conversational RAG
- Maintains session-based chat history  
- Reformulates user queries based on chat context  
- Retrieves the most relevant content chunks  
- Generates concise answers (max 3 sentences)

### ⚡ Powered by Groq
Fast and efficient inference with:
ChatGroq(model_name="llama-3.1-8b-instant")

markdown
Copy code

### 🧠 Chat History Memory
Uses:
- `ChatMessageHistory`
- `RunnableWithMessageHistory`

Each session uses a unique `session_id`.

### 🖥 Streamlit User Interface
- Enter Groq API key  
- Upload PDFs  
- Provide session ID  
- Ask questions  
- View responses and stored chat history  

---

## 📂 Project Structure

project-root/
│── app.py # Main application file
│── requirements.txt # Dependencies
│── .env # Environment variables (ignored by Git)
│── .gitignore # Ignore rules
│── README.md # Project documentation
└── temp.pdf # Temporary file used internally

yaml
Copy code

---

## 🔐 Environment Variables

Create a `.env` file in your project folder with:

GROQ_API_KEY=your_groq_api_key
HF_TOKKEN=your_huggingface_token # optional, matches your code variable name

yaml
Copy code

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vikrant-honbute/Pdf-Intelligent-Chat-With-History.git
cd Pdf-Intelligent-Chat-With-History
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
streamlit run app.py
Then open the local URL shown in the terminal.

🧩 How It Works
User uploads PDFs

Text is loaded and split into overlapping chunks

Embeddings are generated and stored in Chroma

User enters a query

A history-aware retriever reformulates the question

Relevant chunks are retrieved

Groq LLM generates the answer

Chat history is stored per session

💡 Tech Stack
Component	Technology
UI	Streamlit
LLM	Groq – LLaMA 3.1 (8B Instant)
Framework	LangChain
Vector Store	Chroma
Embeddings	HuggingFace MiniLM L6-v2
PDF Loader	PyPDFLoader
Memory	ChatMessageHistory

🤝 Contributing
Contributions and suggestions are welcome!

📜 License
This project is licensed under the MIT License.

⭐ Support
If you like this project, please ⭐ star the repository!

yaml
Copy code

---

If you want a **more stylish version with badges, emojis, centered title, or screenshots**, tell me — I can generate

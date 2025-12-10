# 🤖 Conversational RAG — PDF Chat With Memory  
A smart **Retrieval-Augmented Generation (RAG)** application that allows users to **upload PDFs and chat with them**, powered by **Groq LLM**, **LangChain Classic**, **ChromaDB**, and **Streamlit**.  
Supports **conversation history**, **question reformulation**, and **context-aware answers**.

---

## 🚀 Features

- 📂 Upload and process **multiple PDF files**
- 🔍 Automatic text splitting (500 chars, 200 overlap)
- 🧠 **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)
- 🗃️ **ChromaDB** vector database for fast retrieval
- 🧵 **Session-based chat memory** using `ChatMessageHistory`
- 🧩 **History-aware retriever** (question rewriting)
- ⚡ Ultra-fast inference via **Groq LLM (llama-3.1-8b-instant)**
- 🧠 RAG pipeline using LangChain Classic chains
- 🎛️ Clean, simple **Streamlit UI**

---

## 🖼️ Demo / Screenshots  

## 📸 Screenshot

<p align="center">
  <img src="<img width="1919" height="915" alt="UI" src="https://github.com/user-attachments/assets/e12ad591-0670-441b-a7a4-0fc9cca4ac63" />
" width="600" />
</p>





```
[ Conversational RAG — UI Screenshot Placeholder ]
```

---

## 🧱 Tech Stack

| Component | Technology |
|----------|------------|
| UI | Streamlit |
| LLM | Groq (llama-3.1-8b-instant) |
| Framework | LangChain Classic |
| Embeddings | HuggingFace MiniLM |
| Vector Store | ChromaDB |
| Document Loader | PyPDFLoader |
| Memory | ChatMessageHistory |

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/conversational-rag-pdf-chat.git
cd conversational-rag-pdf-chat
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

Suggested `requirements.txt`:

```
streamlit
python-dotenv
langchain-classic
langchain-core
langchain-community
langchain-chroma
langchain-groq
langchain-text-splitters
langchain-huggingface
pypdf
```

---

## 🔑 Environment Variables

Create `.env`:

```bash
HF_TOKKEN=your_huggingface_token_here
```

⚠️ Use exact name `HF_TOKKEN` — your code uses this spelling.

Groq API key is entered inside the UI.

---

## 📘 How to Use

### Start the app
```bash
streamlit run app.py
```

### Steps
1. Enter your **Groq API key**.  
2. Enter **session ID** (default: `default_session`).  
3. Upload one or more **PDF files**.  
4. Ask questions related to the documents.  
5. The system uses:
   - Chat history  
   - Reformulated queries  
   - Retrieved chunks  
   - Groq LLM for final answers  

---

## 🧩 Core Architecture (Key Snippets)

### Embeddings
```python
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

### Groq LLM
```python
llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant")
```

### History-Aware Retriever
```python
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)
```

### Conversational RAG Chain
```python
conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)
```

---

## 🗂️ Project Structure

```bash
conversational-rag-pdf-chat/
│
├── app.py
├── requirements.txt
├──

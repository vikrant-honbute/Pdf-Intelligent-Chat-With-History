import streamlit as st
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
import os

from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKKEN'] = os.getenv('HF_TOKKEN')
embeddings= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")



##set up Streamlit

st.title("Conversational RAG - PDF INTELLIGENT CHAT WITH HISTORY")
st.write("UPLOAD YOUR PDF & CHAT WITH IT ")

## Input the Groq API key
api_key= st.text_input("Enter your Groq API key:", type="password")

### Check if API key provided 
if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant")

    #CHAT INTERFACE
    session_id = st.text_input("session ID:", value="default_session")
    
    #STATEFULL MANAGE CHAT HISTORY

    if 'store' not in st.session_state:
        st.session_state.store={}

    uploaded_files = st.file_uploader("Upload PDF File you want to Chat with: ", type="pdf", accept_multiple_files=True)
    
    #MANAGE THE UPLOADED FILE
    if uploaded_files:
        documents=[]
        for uploaded_file in uploaded_files:
            temppdf= f"./temp.pdf"
            with open(temppdf,"wb") as file:     # opening the file
                file.write(uploaded_file.getvalue())   ## reading all values
                file_name= uploaded_file.name  ## storing file name too
            
            loader=PyPDFLoader(temppdf)
            docs=loader.load()
            documents.extend(docs)
        
    #split and create embeddings for the documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
        splits = text_splitter.split_documents(documents)
        vectorstore =  Chroma.from_documents(documents=splits, embedding=embeddings)
        retriever =vectorstore.as_retriever() 
    
        ##system prompt

        contextualize_q_system_prompts = (
            "Given a chat history and the latest user question"
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood"
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )

        ## prompt
        contextualize_q_prompt = ChatPromptTemplate(
            [
                ("system", contextualize_q_system_prompts),
                MessagesPlaceholder("chat_history"),
                ("human","{input}"),
            ]
        )

        history_aware_retriever = create_history_aware_retriever(llm,retriever,contextualize_q_prompt)

        ##ANSWER QUESTION 
        system_prompt = (
            "You are an assistant for question-answering tasks."
            "use the following pieces of retrived contect to answer"
            "the question. If you don't know the answer, say that you"
            "dont know. Use three Sentence maximun and keep the"
            "answer concise"
            "\n\n"
            "{context}"
        )

        qa_prompt = ChatPromptTemplate(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}")
            ]
        )

        question_answer_chain = create_stuff_documents_chain(llm,qa_prompt)
        rag_chain= create_retrieval_chain(history_aware_retriever,question_answer_chain)

        def get_session_history(session:str)-> BaseChatMessageHistory:
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]
        


        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"

        )

        user_input = st.text_input("Your question:")
        if user_input:
            session_history = get_session_history(session_id)
            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "some-id"}}
,
            )
            st.write(st.session_state.store)
            st.write("Assistant:", response['answer'])
            st.write("Chat history", session_history.messages)
else:
    st.warning("Please Enter Your GROQ API KEY")
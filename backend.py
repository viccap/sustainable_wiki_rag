from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_wiki_app_backend():
    load_dotenv()
    # Initialize the embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    loaded_wiki_vectorstore = FAISS.load_local("full_wiki_embedding_faiss_index", embeddings=embedding_model, allow_dangerous_deserialization=True)
    retriever = loaded_wiki_vectorstore.as_retriever()

    # Set up the LLM
    llm = ChatOpenAI(
        openai_api_key=os.getenv("API_KEY"),
        openai_api_base="https://chat-ai.academiccloud.de/v1",
        model_name="meta-llama-3.1-8b-instruct",
        temperature=0.7
    )

    # Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def answer_question(question, qa_chain=None):
    if qa_chain is None:
        qa_chain = load_wiki_app_backend()
    result = qa_chain.invoke({"query": question})
    return result["result"]
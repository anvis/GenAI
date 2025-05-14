from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import chromadb
from langchain.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

def Read(file_path):    
    print("Loading PDF document...")
    print(f"File path: {file_path}")
    pdf_loader = PyPDFLoader(file_path)
    documents = pdf_loader.load()
    return documents

def Read_SplitText(file_path):
    documents = Read(file_path)
    if isinstance(documents, list) and isinstance(documents[0], str):
        print("List of strings detected.")
        documents = [Document(page_content=text) for text in documents]
    
    # Check if documents are valid
    if not documents or not all(hasattr(doc, "page_content") for doc in documents):
        print("Invalid document structure. Ensure documents are a list of Document objects with page_content.")
    else:
        # Split the documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        split_docs = text_splitter.split_documents(documents)

    if len(split_docs) == 0:
        print("No documents to process.")
    else:
        print(f"Split into {len(split_docs)} chunks.")
    
    return split_docs

def Read_GenAI(model,EmbeddingModel,file_path):
   split_docs = Read_SplitText(file_path)
   # Initialize  the persistent storage ChromaDB
   chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Persistent storage
   
   # Convert text into vector embeddings and store
   embedding = GoogleGenerativeAIEmbeddings(model=EmbeddingModel)

   # Store document embeddings
   vectorstore = Chroma.from_documents(split_docs, embedding, persist_directory="./chroma_db")

   # Save the embeddings to disk
   # vectorstore.persist() // Automatic in newer versions of Chroma

   qa_chain = RetrievalQA.from_chain_type(model, chain_type="stuff", retriever=vectorstore.as_retriever())

   return qa_chain


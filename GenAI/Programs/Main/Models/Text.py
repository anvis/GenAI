from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from langchain.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

def TextRead_SplitDocument(documents : list[Document], chunk_size=500, chunk_overlap=100 ):
    #documents = Read(file_path)
    if isinstance(documents, list) and isinstance(documents[0], str):
        print("List of strings detected.")
        documents = [Document(page_content=text) for text in documents]
    
    # Check if documents are valid
    if not documents or not all(hasattr(doc, "page_content") for doc in documents):
        print("Invalid document structure. Ensure documents are a list of Document objects with page_content.")
    else:
        # Split the documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        split_docs = text_splitter.split_documents(documents)

    if len(split_docs) == 0:
        print("No documents to process.")
    else:
        print(f"Split into {len(split_docs)} chunks.")
    
    return split_docs

def Convert_To_Embedding_Gemini(split_docs : list[Document], EmbeddingModel="models/embedding-001"):
   # Initialize  the persistent storage ChromaDB
   chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Persistent storage

    # Convert text into vector embeddings and store
   embedding = GoogleGenerativeAIEmbeddings(model=EmbeddingModel)

   # Store document embeddings
   vectorstore = Chroma.from_documents(split_docs, embedding, persist_directory="./chroma_db")

   # Save the embeddings to disk
   # vectorstore.persist() // Automatic in newer versions of Chroma
   print("Vectorstore created successfully.")

   return vectorstore
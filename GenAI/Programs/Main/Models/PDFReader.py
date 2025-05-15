from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from Models.Text import TextRead_SplitDocument, Convert_To_Embedding_Gemini

def Read(file_path):    
    print("Loading PDF document...")
    print(f"File path: {file_path}")
    pdf_loader = PyPDFLoader(file_path)
    documents = pdf_loader.load()
    return documents

def Read_SplitText(file_path):
    documents = Read(file_path)
    split_docs = TextRead_SplitDocument(documents)     
    return split_docs

def Read_GenAI(model,EmbeddingModel,file_path):
   split_docs = Read_SplitText(file_path)   

   # Store document embeddings
   vectorstore = Convert_To_Embedding_Gemini(split_docs, EmbeddingModel)  

   qa_chain = RetrievalQA.from_chain_type(model, chain_type="stuff", retriever=vectorstore.as_retriever())

   return qa_chain


from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

def Read(model, url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    summarize_chain = load_summarize_chain(model, chain_type="stuff")
    return summarize_chain.invoke(docs)
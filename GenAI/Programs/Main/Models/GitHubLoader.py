from langchain_community.document_loaders.github import GithubFileLoader
from Models.Text import TextRead_SplitDocument, Convert_To_Embedding_Gemini

def Read(GitHubURL, branch="main"):
    # github_loader = GithubFileLoader(GitHubURL, branch, file_filter=None)
    github_loader = GithubFileLoader(
    repo= GitHubURL,  # the repo name
    branch=branch,  # the branch name    
    access_token="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",  # your personal access token
    github_api_url="https://api.github.com/",
    file_filter=lambda file_path: file_path.endswith(
        ".md"
    ),  # load all markdowns files.
)
    documents = github_loader.load()
    return documents


def Read_SplitText(GitHubURL, branch="main"):
    documents = Read(GitHubURL, branch)
    print(f"Number of documents loaded: {len(documents)}")
    split_docs = TextRead_SplitDocument(documents)  
    print(f"Number of documents after splitting: {len(split_docs)}")
    return split_docs

def GetVectorStore(EmbeddingModel, GitHubURL, branch="main"):
    split_docs = Read_SplitText(GitHubURL, branch)   

    # Store document embeddings
    vectorstore = Convert_To_Embedding_Gemini(split_docs, EmbeddingModel)
    return vectorstore

def Read_GenAI(model, EmbeddingModel, GitHubURL, branch="main"):
    split_docs = Read_SplitText(GitHubURL, branch)   

    # Store document embeddings
    vectorstore = Convert_To_Embedding_Gemini(split_docs, EmbeddingModel)  
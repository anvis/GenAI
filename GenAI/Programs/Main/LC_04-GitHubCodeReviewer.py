
from Models.llm import llm
from Models.GitHubLoader import GetVectorStore


# repo_url = "anvis/GraphQLDemo"  # Replace with the actual repo URL

repo_url = "anvis/ReactLearning"

geminiModel = llm.get_Gemini_model() 

vector_store = GetVectorStore("models/embedding-001", repo_url, branch="master")

query = "Summarize the repository structure and key functionalities."


retrieved_docs = vector_store.similarity_search(query, k=5)
context = "\n".join([doc.page_content for doc in retrieved_docs])
response = geminiModel.invoke(context)

print("Repository Summary:")
print(response)

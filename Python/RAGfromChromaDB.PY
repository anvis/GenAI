from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai

# 1. Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
chroma_collection = chroma_client.get_collection("articles_embeddings")

# 2. Load embedding model (for queries)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Configure Gemini with your API key
genai.configure(api_key="AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20")

# 4. Define RAG query function
def rag_query(user_query):
    # Step A: Embed the query
    query_embedding = embedder.encode([user_query])

    # Step B: Retrieve relevant chunks from ChromaDB
    results = chroma_collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    print("hola hola")
    ##print("Documents:", results["documents"])


    retrieved_docs = results["documents"]

    # Flatten nested lists/tuples
    flat_docs = []
    for item in retrieved_docs:
        if isinstance(item, (list, tuple)):
            flat_docs.extend(item)
        else:
            flat_docs.append(item)


    if not flat_docs:
        return "No data found at our end."


    context = "\n\n".join(flat_docs)


    # Step C: Send to Gemini with context
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    You are a helpful tutor. Use the following context to answer the question.

    Context:
    {context}

    Question:
    {user_query}
    """

    response = model.generate_content(prompt)
    return response.text

# Example usage
answer = rag_query("Explain ipl with an analogy")
print("Answer:", answer)
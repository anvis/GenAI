import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="./chroma_storage")

chroma_collection = chroma_client.get_collection("articles_embeddings")

# 2. Load embedding model (for queries)
embedder = SentenceTransformer("all-MiniLM-L6-v2")


# 5. Verification Step
print("\n--- Verification ---")
# Count records
count = len(chroma_collection.get()["ids"])
print("Total records stored in ChromaDB:", count)

# Test a semantic query
query = "Explain eigenvectors with an analogy"
query_embedding = embedder.encode([query])
results = chroma_collection.query(query_embeddings=query_embedding, n_results=2)

print("\nQuery Results:")
for doc, meta in zip(results["documents"], results["metadatas"]):
    print("Document:", doc)
    print("Metadata:", meta)
    print("---")
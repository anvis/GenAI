from pymongo import MongoClient
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["Articles"]

# 2. Connect to ChromaDB
## chroma_client = chromadb.Client() # this will create in memory
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
chroma_collection = chroma_client.get_or_create_collection("articles_embeddings")

# 3. Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 4. Loop through all collections in MongoDB
for collection_name in db.list_collection_names():
    collection = db[collection_name]
    print(f"Processing collection: {collection_name}")

    for doc in collection.find():
        # Combine meaningful fields for embedding
        text_to_embed = f"Title: {doc.get('title','')}\nContent: {doc.get('content','')}\nTags: {','.join(doc.get('tags', []))}"

        # Generate embedding
        embedding = embedder.encode([text_to_embed])[0]

        # Store in ChromaDB
        chroma_collection.add(
            documents=[text_to_embed],
            embeddings=[embedding],
            ids=[str(doc["_id"])],
            metadatas={
                "collection": str(collection_name),
            "slug": str(doc.get("slug", "")),
            "tags": ",".join(doc.get("tags", [])),   # convert list → string
            "created_at": str(doc.get("created_at", "")),  # convert datetime → string
            "source": str(doc.get("source", "")),
            "folder_path": str(doc.get("folder_path", ""))

            }
        )

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
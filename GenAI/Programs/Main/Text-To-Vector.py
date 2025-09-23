# app.py
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_store")

# Create or get collection
collection = chroma_client.get_or_create_collection(name="vector_store")

# Streamlit UI
st.title("🔢 Number to Vector Converter")
user_input = st.text_input("Enter a number or text:", "")

if st.button("Convert and Store"):
    if user_input.strip():
        # Convert to vector
        embedding = model.encode(user_input).tolist()

        # Store in ChromaDB
        collection.add(
            documents=[user_input],
            embeddings=[embedding],
            ids=[f"id_{user_input}"]
        )

        # Show result
        st.success("Vector stored successfully!")
        st.write("🔍 Converted Vector:")
        st.json(embedding)
    else:
        st.warning("Please enter a valid input.")

if st.button("Show Stored Entries"):
    results = collection.get()
    for doc, vec in zip(results["documents"], results["embeddings"]):
        st.write(f"📄 Text: {doc}")
        st.json(vec)

if st.button("Show Stored Entries in vectors"):
    results = collection.get()
    st.json(results)
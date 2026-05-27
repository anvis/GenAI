
**RAG Pipeline**

- Document Ingestion (Raw data, Remove Noise, Chunk documents)
- Embed with transformer embeddings
- Store in vector DB
- Retrieve top-k chunks
- Pass to LLM for generation

---

Why Chunking? 

Chunking makes retrieval precise and efficient. If you embed the entire document as one vector, retrieval will return the whole thing even if only a small section is relevant. That dilutes precision.Most embedding models have a token limit

Fixed-size or Semantic chunking
Fixed Chunking Splits text into chunks of a predetermined size (e.g., 500 tokens, 1,000 characters).

Semantic chunking Splits text based on meaning, structure, or natural boundaries (e.g., paragraphs, sections, headings).

Hybrid Approach: Semantic boundaries + Token Limit (Range)

---


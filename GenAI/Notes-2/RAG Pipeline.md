
**RAG Pipeline**

- Document Ingestion (Raw data, Remove Noise, Chunk documents)
- Embed with transformer embeddings
- Store in vector DB
- Retrieve top-k chunks
- Pass to LLM for generation

---

Why Chunking? 

Chunking makes retrieval precise and efficient. 
If you embed the entire document as one vector, retrieval will return the whole thing even if only a small section is relevant. 
That dilutes precision.Most embedding models have a token limit

Fixed-size or Semantic chunking
Fixed Chunking Splits text into chunks of a predetermined size (e.g., 500 tokens, 1,000 characters).

Semantic chunking Splits text based on meaning, structure, or natural boundaries (e.g., paragraphs, sections, headings).

Hybrid Approach: Semantic boundaries + Token Limit (Range)

---

Embedding vs Encoding:

Tokenization → Breaks raw text into manageable pieces.
Encoding → General process of turning tokens into numbers.
Vectorization (basic encoding) → Basic numeric representation.
One-hot encoding: "powerful" → [0,0,0,1,0,...].

Embeddings (Advance encoding) → Improves vectorization by learning dense, continuous representations. Advanced, learned encodings that capture meaning and context.	"powerful" → [0.23, -0.11, 0.89,...].

---

**Embedding**

Convert chunks into dense vector representations using embedding models.
Embedding can be done in many ways we have used Sentence Transformers. 

What are Sentence Transformers? 
Sentence Transformers are a Python framework that makes it easy to generate high-quality embeddings for sentences, paragraphs, or entire documents, enabling tasks like semantic search, clustering, and similarity comparison. 
Sentence Transformers built on transformer architectures (e.g., BERT, RoBERTa)

<img width="832" height="227" alt="image" src="https://github.com/user-attachments/assets/e5de1195-198a-4d7c-98ea-0bd316823b70" />

Query: “bank” 
Word2Vec/GloVe: Same vector for “river bank” and “bank account.” 
Sentence Transformers: Different embeddings because the surrounding sentence changes meaning. 

 ---

 Dense Vectors vs Sparse Vectors

 Sparse Vectors: 
 High-dimensional vectors where most entries are **zero**.
 Each dimension corresponds to a word in the vocabulary. 
 Cannot capture semantic similarity (e.g., “car” vs “automobile” are treated as unrelated).
 Example: TF-IDF, BM25.

Dense Vectors:
Low-dimensional vectors where **most entries are non-zero**. 
Each dimension encodes semantic features, not individual words. 
Captures meaning, context, and synonyms.Example: Word2Vec, Sentence Transformers.

How Sparse Vector Works?
Let's say we have 3 documents, 
- Doc1: “The fox ran quickly.”
- Doc2: “The moon shone at night.”
	- Doc3: “The tree stood tall.”
we term all provided data as corpus.
You count all unique words across the corpus →
['the', 'fox', 'ran', 'quickly', 'moon', 'shone', 'at', 'night', 'tree', 'stood', 'tall’]
Vector Representation:	- Doc1 → [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
	- Doc2 → [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
	- Doc3 → [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]


Dense Vector:
For the same sentence “The fox ran quickly,” the model might output something like:  
[0.23, 0.88, 0.65, 0.12, 0.44, 0.91, 0.33, 0.77]
Each number represents a learned feature — not a word position.

Dense vectors are **compact (e.g., 300 dimensions)** and **semantic**:  
- “fox” and “wolf” will have similar vectors.  
- “quickly” and “fast” will be close in vector space.

---

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/d5d43ade-4497-4050-a1ce-fe5191851460" />

---

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/e82ac80c-04a6-47d0-b7d4-90e95165b5c4" />

---

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/03c0ffde-a528-4f81-986e-98d612d7e928" />

---


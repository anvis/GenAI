
Tokenization breaks text into smaller units (tokens), vectorization converts those tokens into numerical vectors, and embeddings are dense, learned vector representations that capture semantic meaning.

---

How They Work Together
- Tokenization → Breaks raw text into manageable pieces.
- Example: "ChatGPT is powerful" → ["ChatGPT", "is", "powerful"].
- Vectorization → Converts each token into a numerical format.
- One-hot encoding: "powerful" → [0,0,0,1,0,...].
- Bag-of-words: counts frequency of tokens in a document.
- Embeddings → Improves vectorization by learning dense, continuous representations.
- "powerful" → [0.23, -0.11, 0.89,...].
- Similar words (like "strong") will have vectors close to "powerful".

---

- Tokenization is simple but language-dependent (e.g., Chinese requires character segmentation).
- Vectorization (like one-hot) is easy but results in sparse, high-dimensional vectors that don’t capture meaning.
- Embeddings are powerful because they encode semantic relationships (e.g., "king" - "man" + "woman" ≈ "queen"), but they require training or pre-trained models.

---

Risks & Limitations
- Tokenization errors can break meaning (e.g., splitting "New York" into "New" and "York").
- Vectorization without embeddings leads to poor search relevance.
- Embeddings require careful handling of bias and domain adaptation—pre-trained embeddings may not align with your school’s specialized content.

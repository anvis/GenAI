## RAG vs CAG

CAG exists not to replace RAG, but to solve a different class of problems, especially ones where RAG has real trade-offs.
CAG flips the script. Instead of retrieving context per query, it preloads everything the model might need into memory — before a user even asks a question.

Cache-Augmented Generation (CAG) is an alternative to Retrieval-Augmented Generation (RAG) that eliminates real-time retrieval by preloading relevant documents into a model’s extended context and caching its runtime parameters. This approach allows the model to generate responses directly without needing to fetch external data

CAG is particularly useful for tasks where the knowledge base is limited and manageable, making it a streamlined alternative to traditional RAG-based systems

---

## How CAG Works

1. You load all your domain knowledge, say, a full product manual, company policies, or a set of meeting transcripts, into a long prompt.
2. The model processes this once, storing it in the KV cache.
3. When a user submits a query, the model appends that query after the knowledge, and instantly generates an answer using the cached memory, without re-reading everything.

If your LLM can read it once and reuse it, CAG gives you speed, coherence, and simplicity.

But if your knowledge base is huge, dynamic, or requires traceability—RAG is still the better fit. Retrieval works well when you need to handle massive corpora, serve many users, or provide citations.

CAG is also benefiting from recent innovations like:

Re-ranking: Curating what goes into the context (e.g., top-K high-relevance passages).
Segmented summarization: Condensing long documents into structured memory chunks.
Hybrid models: Using RAG to filter and CAG to reason — retrieve a few dozen passages and cache them for rich follow-ups.

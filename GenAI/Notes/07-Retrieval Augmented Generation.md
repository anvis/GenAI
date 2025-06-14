# RAG

- [What is RAG](#What-is-RAG)
- [How RAG Works](#How-RAG-Works)
- [Limitations of LLM](#Limitations-of-LLM)
- [RAG vs CAG](#RAG-vs-CAG)
- [How CAG Works](#How-CAG-Works)

## What is RAG?
**Concept of RAG**: Improving LLM responses by retrieving data from external knowledge sources (e.g., using vector databases).
*   **Implementation**: Using vector databases and embeddings to retrieve relevant context for LLM queries.

RAG helps LLMs stay up-to-date by retrieving relevant information from an external knowledge source, typically a vector database.

**Retrieval-Augmented Generation (RAG)**  is a powerful approach for keeping Generative AI models informed with the most recent data, particularly when dealing with domain-specific questions. It cleverly combines the comprehensive understanding capacity of a large language model (LLM) with the most up-to-date information pulled from a database of relevant text snippets. The beauty of this system is in its ability to ensure that responses remain accurate and reflective of the latest developments.

---

## How RAG Works?

Here’s how it works:

When a query is made, the system first retrieves relevant documents or snippets from a knowledge base.

These retrieved pieces of information are then used as context for the generative model to produce more informed and accurate responses.

1) A user asks a question.
2) The system turns the query into an embedding and retrieves relevant document chunks.
3) Those chunks are added to the prompt.
4) The LLM uses both the user’s question and the retrieved context to generate an answer.

RAG works in three stages:

1. Retrieval: When a request reaches LLM and the system looks for relevant information that informs the final response.  It searches through an external dataset or document collection to find most relevant pieces of information. This dataset could be a curated knowledge base, or any extensive collection of text, images, videos, and audio or even your local database. 

2. Augmentation: In this step the query is enhanced with the information retrieved in the previous step.

3. Generation: The final augmented response or output is generated. Your LLM uses the additional context provided by the augmented input to produce an answer that is not only relevant to the original query but enriched with information from external sources.

---

## Limitations of LLM

1. Hallucination: LLM's try to present false information when it does not have the answer or even there is no answer.
2. Outdated Info: Presenting out-of-date or generic information when the user wants a specific, accurate response.
3. Tech Confusion: Generating inaccurate responses due to terminology confusion, wherein different training sources use the similar terminology about different things.
4. Unauthorized: Creating a response from non-authoritative sources.

## RAG vs CAG

CAG exists not to replace RAG, but to solve a different class of problems, especially ones where RAG has real trade-offs.
CAG flips the script. Instead of retrieving context per query, it preloads everything the model might need into memory — before a user even asks a question.

Cache-Augmented Generation (CAG) is an alternative to Retrieval-Augmented Generation (RAG) that eliminates real-time retrieval by preloading relevant documents into a model’s extended context and caching its runtime parameters. This approach allows the model to generate responses directly without needing to fetch external data

CAG is particularly useful for tasks where the knowledge base is limited and manageable, making it a streamlined alternative to traditional RAG-based systems


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


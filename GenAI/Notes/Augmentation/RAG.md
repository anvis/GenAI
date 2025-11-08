
# RAG

- [What is RAG](#What-is-RAG)
- [How RAG Works](#How-RAG-Works)
- [Limitations of LLM](#Limitations-of-LLM)
- [Why Should We Use RAG?](#Why-Should-We-Use-RAG?)
- [Types of RAG](#Types-of-RAG)
- [RAG vs CAG](#RAG-vs-CAG)
- [How CAG Works](#How-CAG-Works)

## What is RAG?

Retrieval-augmented generation (RAG) is a powerful AI technique that combines information retrieval with text generation. Instead of relying solely on pre-trained knowledge, RAG pulls real-time data from external sources, ensuring more accurate and up-to-date responses. This makes AI models more reliable, especially for applications that require fresh and factual information.

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

---

## Why Should We Use RAG?
-Improved Accuracy: AI can access the latest information rather than relying on outdated training data.
-Better Context Understanding: RAG enhances the AI’s ability to generate meaningful responses by retrieving relevant documents.
-Reduced Hallucination: Since the model pulls from real sources, the risk of generating false information is minimized.
-Scalability: RAG can integrate with various databases and APIs, making it useful for diverse applications.
-Enhanced Customization: It allows businesses to tailor AI responses based on industry-specific knowledge.

---

## Types of RAG

**Standard RAG** is a basic system where documents are broken into pieces, and the most relevant sections are retrieved to answer queries using a language model. It follows a simple three-step process: indexing, retrieval, and generation, and uses basic measures for finding matching text. This approach works for Q&A systems and chatbots that answer common questions. For example, a university FAQ chatbot can pull relevant info from academic guidelines to assist students.

**Advanced RAG** improves on Standard RAG by adding steps before and after retrieving information, like rewriting queries and re-ranking documents. This method ensures better quality and accuracy, making it suitable for areas like healthcare and legal applications. A healthcare chatbot exemplifies this use case, refining queries and pulling the latest guidelines to provide trustworthy answers.

**Modular RAG** separates the retrieval and generation processes into independent modules, allowing more flexibility and customization. This is ideal for large enterprises that need different solutions for various departments, like customer support platforms using specific modules for technical and billing inquiries.

**Corrective RAG** includes feedback mechanisms to cross-check answers against trusted sources, enhancing accuracy and reducing misinformation. It's useful in high-stakes fields such as legal research, where verification is critical. A legal research assistant checking its summaries against databases illustrates this approach.

**Speculative RAG** addresses uncertainty by offering educated guesses when data is incomplete, signaling to users that these answers are not confirmed facts. It serves exploratory research and brainstorming sessions, as seen in a market research tool proposing emerging industry trends.

**Fusion RAG** combines multiple data sources to provide comprehensive answers and reduce biases. This is useful for complex decision-making, such as a financial advisory tool that merges market data with expert insights for investment advice.

**Agentic RAG** allows the model to autonomously decide what additional information is needed, improving the answer through iterative queries. This is beneficial for interactive assistants, like a virtual research assistant refining its responses to complex questions.

**Self RAG** incorporates self-assessment, where the model evaluates and adjusts its responses against retrieved data. This method is suitable for educational platforms, resembling an AI math tutor that reviews its solutions against verified methods.

**Graph RAG** utilizes knowledge graphs to understand the relationships between information, enhancing context in retrieval. It's valuable in legal and scientific research, exemplified by a legal assistant that shows interrelations among case documents for richer responses.

**Radio RAG** focuses on real-time data retrieval in specialized fields, crucial for time-sensitive situations. For example, a radiology support tool pulls the latest research to assist in decision-making regarding diagnoses.

---


## Table of Contents
- [Transformer Embeddings](#Transformer-Embeddings)
- [The Issue with Static Embeddings](#The-Issue-with-Static-Embeddings)
- [Difference between Static and Learned Embeddings](#Difference-between-Static-and-Learned-Embeddings)
- [Training transformer embeddings](#Training-transformer-embeddings)
- [Understand Self Attention Mechanism](#Understand-Self-Attention-Mechanism)



## Understand Self Attention Mechanism

Self-attention modifies the vector representation of words to capture the context of their usage in an input sequence. 
The “self” in self-attention refers to the fact that the mechanism uses the surrounding words within a single sequence to provide context. As such, self-attention requires all words to be processed in parallel. 

This is actually one of the main benefits of transformers (especially compared to RNNs) since the models can leverage parallel processing for a significant performance boost. 

Another form of attention used in transformers is cross-attention. Unlike self-attention, which operates within a single sequence, cross-attention compares each word in an output sequence to each word in an input sequence, crossing between the two embedding matrices.

---

We understood that the goal of self-attention is to move the embedding for each token to a region of vector space that better represents the context of its use in the input sequence. Let's Explore how it is done?

The self-attention mechanism is a crucial part of transformers, allowing them to process sequences in parallel while weighing the importance of different words in a sentence dynamically. Here’s a breakdown of how it works:

- Calculate the Similarity Between Words using the Dot Product
- Scale the Similarity Scores. (Normalizing the Similarity Score)
- Calculate the Attention Weights using the Softmax Function
- Calculate the Transformer Embedding

---

Key Concepts in Self-Attention

- Query, Key, and Value Vectors: Each word in the input sequence is transformed into three vectors—Query (Q), Key (K), and Value (V). These vectors capture different aspects of the word’s significance.
  
- Similarity Calculation: The Query vector of a word is compared with Key vectors of all words to determine relevance. This is done using a dot product, followed by a scaling operation.
  
- Softmax Normalization: The relevance scores are passed through a softmax function to assign attention weights, ensuring they sum to 1.
  
- Weighted Summation: Each word's final representation is computed by taking a weighted sum of all Value vectors using the attention weights.
  
- Multi-Head Attention: Instead of using one set of Q, K, and V vectors, transformers use multiple attention heads, each capturing different aspects of relationships between words.

---
  
Why is Self-Attention Powerful?
- Captures Context: Words can relate to others dynamically, unlike fixed embeddings.
- Handles Long Sequences Efficiently: Unlike recurrent networks, self-attention enables parallel computation, making it scalable.
- Adapts to Different Input Structures: Works well across sentences, paragraphs, and even code snippets!


https://medium.com/p/d7a9f0f4d94e



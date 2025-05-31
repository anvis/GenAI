

# Word Embeddings

## Table of Contents
- [What is WordEmbedding](#What-is-WordEmbedding)
- [One-Hot Encoded Vector](#One-Hot-Encoded-Vector)
- [Word Embedding](#Word-Embedding)
- [One-Hot Encoded Vector vs Word Embedding](#One-Hot-Encoded-Vector-vs-Word-Embedding)
- [Denotational vs Distributional Semantics](#Denotational-vs-Distributional-Semantics)

## What is WordEmbedding

Word Embedding is the process of taking a word and creating a vector representation in N-dimensional space. 

As a simple example, you could imagine each word having a three-dimensional representation, and then plotting the words in 3D space using these numbers as coordinates. 
The goal here is to come up an algorithm to produce the coordinates for each word (called embeddings), such that similar words are geographically near in vector space, and dissimilar words are distant in vector space. 

Word embeddings bridge the barrier between natural language and machine language, and so the need for high quality vector representations is difficult to understate.

Natural Language Processing (NLP) deals with textual data, which in its raw form cannot be understood by computers.

In recent times, NLP tasks have been largely handled by neural networks, such as Recurrent Neural Networks (RNNs) and transformer-based models (including many Large Language Models, LLMs). 
These both require vector inputs to enable linear algebra operations, and so text must first be converted into arrays of numbers. 

Sentences can first be split into words (or subword units) called tokens using tokenization.
These tokens are then assigned an integer value called a token ID, which can be converted into a one-hot encoded vector.


## One-Hot Encoded Vector

**1. One-Hot Encoded Vector**

- Represents each word as a unique binary vector.
- The size of the vector equals the total vocabulary size.
- Only one position in the vector is set to **1**, while all others are **0**.

#### **Example:**
If we have a vocabulary of 4 words: `["cat", "dog", "fish", "bird"]`, their one-hot vectors would be:
```
cat   → [1, 0, 0, 0]
dog   → [0, 1, 0, 0]
fish  → [0, 0, 1, 0]
bird  → [0, 0, 0, 1]
```

#### **Pros:**
✅ Simple and easy to implement  
✅ Preserves uniqueness of words  

#### **Cons:**
❌ Inefficient for large vocabularies (high-dimensional sparse vectors)  
❌ Doesn't capture word relationships (e.g., "cat" and "dog" are equally distant from "fish")  


## Word Embedding

**2. Word Embedding (Distributed Representation)**
- Maps each word to a dense **fixed-length vector**.
- Word embeddings are **learned** to represent semantic relationships.
- Examples: **Word2Vec, GloVe, FastText, BERT embeddings**.

#### **Example:**
If word embeddings have 3 dimensions:
```
cat   → [0.85, 0.12, -0.42]
dog   → [0.88, 0.14, -0.39]
fish  → [0.30, 0.60, -0.10]
```
Notice that "cat" and "dog" have similar values because they are semantically related.

#### **Pros:**
✅ Captures semantic meaning (words like "king" and "queen" are closer)  
✅ Lower dimensionality and computational efficiency  
✅ Helps in downstream NLP tasks like text classification and sentiment analysis  

#### **Cons:**
❌ Requires training or pre-trained embeddings  
❌ May struggle with rare or unseen words (though newer models handle this better)  


## One-Hot Encoded Vector vs Word Embedding

### **Key Differences**
| Feature           | One-Hot Encoding | Word Embedding |
|------------------|----------------|---------------|
| Representation  | Sparse binary vector | Dense numerical vector |
| Size            | Vocabulary-dependent | Fixed-length |
| Semantic Meaning | ❌ No | ✅ Yes |
| Storage        | High memory usage | Efficient |



## Denotational vs Distributional Semantics

Denotational semantics is crucial for formal verification and correctness in programming, while distributional semantics helps in tasks like word similarity, machine translation, and sentiment analysis.

Before embedding words as vectors, it is important to consider what meaning is trying to be encoded. Most linguists think about meaning as being the representation of an idea by a word or group of words. This is called denotational semantics, and is just one way to define the meaning of words. 

For NLP, it is often more helpful to think of the meaning of a word as being determined by the words that frequently co-occur (i.e. words that often appear before or after the word). This is a concept called distributional semantics




https://medium.com/p/eb9326c6ab7c

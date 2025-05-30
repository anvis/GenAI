

Word Embedding is the process of taking a word and creating a vector representation in N-dimensional space. 

As a simple example, you could imagine each word having a three-dimensional representation, and then plotting the words in 3D space using these numbers as coordinates. 
The goal here is to come up an algorithm to produce the coordinates for each word (called embeddings), such that similar words are geographically near in vector space, and dissimilar words are distant in vector space. 

Word embeddings bridge the barrier between natural language and machine language, and so the need for high quality vector representations is difficult to understate.

Natural Language Processing (NLP) deals with textual data, which in its raw form cannot be understood by computers.

In recent times, NLP tasks have been largely handled by neural networks, such as Recurrent Neural Networks (RNNs) and transformer-based models (including many Large Language Models, LLMs). 
These both require vector inputs to enable linear algebra operations, and so text must first be converted into arrays of numbers. 

Sentences can first be split into words (or subword units) called tokens using tokenization.
These tokens are then assigned an integer value called a token ID, which can be converted into a one-hot encoded vector.


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



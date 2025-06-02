

word2vec is a family of algorithms that produce distributed word embeddings for use in NLP tasks. 

These vectors are far denser than those created using the one-hot encoding method (i.e. very few, if any, of the elements are 0), and so they can be much smaller in size. 

The idea is to create an N-dimensional vector space, in which similar words are geographically close to each other.

Word2Vec is a neural network-based model that transforms words into numerical vectors, capturing semantic relationships by mapping similar words closer in the vector space.

It's widely used in NLP for tasks like word similarity, document clustering, sentiment analysis, and improving contextual understanding in AI applications, enabling models to process language more intuitively.


How Word2Vec Works:
- Training on Context – The model learns word relationships from a large corpus by predicting words in context.
- Two Architectures:
- Continuous Bag of Words (CBOW) – Predicts a target word given its surrounding words (context window).
- Skip-Gram – Predicts surrounding words given a target word, better for capturing rare word meanings.
- Vector Space Representation – Words are mapped into high-dimensional space where similar words appear closer together.
- Dot Product & Cosine Similarity – Helps determine word similarity by measuring angles and distances between vectors.
- Optimization with Backpropagation – The network refines embeddings through gradient descent and loss minimization.
- Practical Applications – Used in NLP tasks like text classification, sentiment analysis, and chatbot training.
Word2Vec enables deep learning models to grasp nuances of natural language, forming the foundation for more advanced techniques like Transformers and BERT.






Typically, these embeddings have around 300 dimensions. Once these embeddings are created, they can be written to a file and loaded into memory when needed to essentially form a lookup table at run time. 
When a language model is given some input text, the text is first converted into tokens. 
These are then converted into vectors by finding the appropriate row in the word2vec embeddings matrix. 
For this reason, the embeddings produced by word2vec are called static. 
These static embeddings form the basis for the so-called dynamic or contextual embeddings that are used in LLMs, which are made by adding context from the surrounding sentences or paragraphs to each word.


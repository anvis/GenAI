

word2vec is a family of algorithms that produce distributed word embeddings for use in NLP tasks. 

These vectors are far denser than those created using the one-hot encoding method (i.e. very few, if any, of the elements are 0), and so they can be much smaller in size. 

The idea is to create an N-dimensional vector space, in which similar words are geographically close to each other.

Typically, these embeddings have around 300 dimensions. Once these embeddings are created, they can be written to a file and loaded into memory when needed to essentially form a lookup table at run time. 
When a language model is given some input text, the text is first converted into tokens. 
These are then converted into vectors by finding the appropriate row in the word2vec embeddings matrix. 
For this reason, the embeddings produced by word2vec are called static. 
These static embeddings form the basis for the so-called dynamic or contextual embeddings that are used in LLMs, which are made by adding context from the surrounding sentences or paragraphs to each word.


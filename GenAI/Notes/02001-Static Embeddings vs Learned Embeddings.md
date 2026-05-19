## The Issue with Static Embeddings

We explored static embeddings for language models using word2vec as an example. 
This embedding method predates transformers and suffers from one major drawback: the lack of **contextual information**.

Words with multiple meanings (called polysemous words) are encoded with somewhat ambiguous representations since they lack the context needed for precise meaning. 

A classic example of a polysemous word is bank. Using a static embedding model, the word bank would be represented in vector space with some degree of similarity to words such as money and deposit and some degree of similarity to words such as river and nature. 
This is because the word will occur in many different contexts within the training data. This is the core problem with static embeddings: they do not change based on context — hence the term “static”.

Transformers overcome the limitations of static embeddings by producing their own context-aware transformer embeddings. 
In this approach, fixed word embeddings are augmented with positional information (where the words occur in the input text) and contextual information (how the words are used). 
These two steps take place in distinct components in transformers, namely the positional encoder and the self-attention blocks, respectively.

By incorporating this additional information, transformers can produce much more powerful vector representations of words based on their usage in the input sequence. 
Extending the vector representations beyond static embeddings is what enables Transformer-based models to handle polysemous words and gain a deeper understanding of language compared to previous models.

## Difference between Static and Learned Embeddings 

A key difference between static and learned embeddings is the way in which they are trained. S
tatic embeddings are trained in a separate neural network (using the Skip-Gram or Continuous Bag of Words architectures) using a word prediction task within a given window size. 
Once trained, the embeddings are then extracted and used with a range of different language models.

Learned embeddings, however, are integral to the transformer you are using and are stored as weights in the first linear layer of the model. 
These weights, and consequently the learned embedding for each token in the vocabulary, are trained in the same backpropagation steps as the rest of the model parameters. 

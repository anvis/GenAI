
## Table of Contents
- [Transformer Embeddings](#Transformer-Embeddings)
- [The Issue with Static Embeddings](#The-Issue-with-Static-Embeddings)
- [Difference between Static and Learned Embeddings](#Difference-between-Static-and-Learned-Embeddings)
- [Training transformer embeddings](#Training-transformer-embeddings)
- [Understand Self Attention Mechanism](#Understand-Self-Attention-Mechanism)

## Transformer Embeddings

The Transformer is a deep neural network architecture that is the foundation for almost all LLMs today. 
Derivative models are often called Transformer-based models or transformers for short, and so these terms will be used interchangeably here.

Like all machine learning models, transformers work with numbers and linear algebra rather than processing human language directly.
Because of this, they must convert textual inputs from users into numerical representations through several steps. 
Perhaps the most important of these steps is applying the self-attention mechanism, which is the focus of this article. 

The process of representing text with vectors is called embedding (or encoding), hence the numerical representations of the input text are known as transformer embeddings.

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


## Training transformer embeddings

Training transformer embeddings involves learning contextual word representations using self-attention and deep neural networks. Here’s the process:

1. **Tokenization** – Breaks input text into tokens and converts them into numerical IDs.

	- Input text is split into tokens (subwords or words) using algorithms like **Byte Pair Encoding (BPE)** or **WordPiece**.  
    - Each token is assigned a unique ID from a predefined vocabulary.
   
2. **Embedding Layer** – Transforms token IDs into dense vectors capturing semantic properties.

   - Token IDs are transformed into dense vectors in a high-dimensional space.  
   - These **learned embeddings** help capture semantic relationships between words.
   
3. **Positional Encoding** – Adds positional information to embeddings since transformers lack inherent sequence awareness.

   - Since transformers process tokens in parallel (unlike RNNs), they lack inherent order awareness.  
   - Positional encoding adds information about each token’s position in the sequence.
   - Positional Encoding is then used to add positional information to the word embeddings. Whereas Recurrent Neural Networks (RNNs) process text sequentially (one word at a time), transformers process all words in parallel. This removes any implicit information about the position of each word in the sentence. For example, the sentences the cat ate the mouse and the mouse ate the cat use the same words but have very different meanings. To preserve the word order, positional encoding vectors are generated and added to the learned embedding for each word.
   
4. **Self-Attention Mechanism** – Computes attention scores to focus on relevant words dynamically.

   - Each token attends to all others in the sequence using **scaled dot-product attention**.  
   - This allows models to weigh words differently depending on their relevance to the context.  
   - **Multi-head attention** enables capturing multiple contextual relationships simultaneously.

5. **Feed-Forward Layers** – Further refines embeddings through multiple layers of transformation.

   - A series of dense layers refine embeddings further by learning complex transformations.  
   - Normalization layers ensure stability during training.
   
6. **Backpropagation & Optimization** – Adjusts embeddings using loss functions and gradient descent.

   - Loss is computed using functions like **cross-entropy** for classification tasks.  
   - Gradients are propagated using **Adam optimizer** or variants to adjust embeddings efficiently.
   
7. **Pretraining & Fine-Tuning** – Models are pretrained on large corpora and later fine-tuned for specific tasks.

   - Transformers are **pretrained** on large corpora using objectives like **Masked Language Modeling (MLM)** (as in BERT) or **Next Word Prediction** (as in GPT).  
   - Later, models are **fine-tuned** on downstream tasks such as **text classification, translation, and question answering**.
   
 

This process enables deep contextual understanding, making embeddings highly effective in NLP tasks like machine translation, question answering, and text generation.


## Understand Self Attention Mechanism

Self-attention modifies the vector representation of words to capture the context of their usage in an input sequence. 
The “self” in self-attention refers to the fact that the mechanism uses the surrounding words within a single sequence to provide context. As such, self-attention requires all words to be processed in parallel. 

This is actually one of the main benefits of transformers (especially compared to RNNs) since the models can leverage parallel processing for a significant performance boost. 


The self-attention mechanism is a crucial part of transformers, allowing them to process sequences in parallel while weighing the importance of different words in a sentence dynamically. Here’s a breakdown of how it works:

Key Concepts in Self-Attention
- Query, Key, and Value Vectors: Each word in the input sequence is transformed into three vectors—Query (Q), Key (K), and Value (V). These vectors capture different aspects of the word’s significance.
- Similarity Calculation: The Query vector of a word is compared with Key vectors of all words to determine relevance. This is done using a dot product, followed by a scaling operation.
- Softmax Normalization: The relevance scores are passed through a softmax function to assign attention weights, ensuring they sum to 1.
- Weighted Summation: Each word's final representation is computed by taking a weighted sum of all Value vectors using the attention weights.
- Multi-Head Attention: Instead of using one set of Q, K, and V vectors, transformers use multiple attention heads, each capturing different aspects of relationships between words.

  
Why is Self-Attention Powerful?
- Captures Context: Words can relate to others dynamically, unlike fixed embeddings.
- Handles Long Sequences Efficiently: Unlike recurrent networks, self-attention enables parallel computation, making it scalable.
- Adapts to Different Input Structures: Works well across sentences, paragraphs, and even code snippets!


https://medium.com/p/d7a9f0f4d94e



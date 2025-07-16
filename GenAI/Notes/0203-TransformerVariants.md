
Transformer (Architecture)

- The Transformer is the fundamental neural network architecture introduced by Vaswani et al. in the 2017 paper "Attention is All You Need."
- It uses self-attention and feed-forward layers, allowing for parallel processing rather than sequential processing like RNNs.
- This model forms the backbone of modern NLP models, including GPT and BERT.


Modern LLMs are built using variations of the Transformer architecture. Depending on their use case and training objective, they fall into one of three categories:

---

**Encoder-Only Models**

- Use only the encoder part of the transformer.
- Good at understanding tasks (e.g., classification, sentiment analysis).
- Use bidirectional attention: they consider both left and right context.
- Example Models: BERT, RoBERTa

**Decoder-Only Models**

- Use only the decoder part of the transformer.
- Designed for generating text, predicting one token at a time from left to right.
- Use causal (unidirectional) attention to avoid looking at future tokens.
- Example Models: GPT-2, GPT-3, LLaMA, Falcon

**Encoder-Decoder Models (Seq2Seq)**

- Use the encoder to process input and the decoder to generate output.
- Great for translation, summarization, and question answering.
- Encoder builds a representation; decoder generates output based on that.
- Example Models: T5, BART, mT5

---

**Autoregressive Language Models** (e.g., GPT): 

Goal: Predict the next word in a sequence, one word (or token) at a time, using only previous context.

These models are trained left to right, meaning they can only “see” what comes before the word they’re trying to predict.

Autoregressive models primarily use the **decoder part of the Transformer architecture**, making them well-suited for natural language generation (NLG) tasks like text summarization, generation, etc. 

- These models generate text by predicting the next word in a sequence given the previous words. 
- They are trained to maximize the likelihood of each word in the training dataset, given its context. 
- The most well-known example of an autoregressive language model is OpenAI’s GPT (Generative Pre-trained Transformer) series, with GPT-4 being the latest and most powerful iteration.

Autoregressive models based on decoder networks primarily leverage layers related to self-attention, cross-attention mechanisms, and feed-forward networks as part of their neural network architecture. 

---

**Autoencoding Language Models** (e.g., BERT): 

Goal: Predict missing words within a sentence, where certain words are intentionally “masked” during training.

These models learn using bidirectional context, meaning they can look at both the left and the right side of a word to understand its meaning.

Autoencoding models, on the other hand, mainly use the encoder part of the Transformer.It’s designed for tasks like classification, question answering, etc. 

- These models learn to generate a fixed-size vector representation (also called embeddings) of input text by reconstructing the original input from a masked or corrupted version of it. 
- They are trained to predict missing or masked words in the input text by leveraging the surrounding context.

Autoencoding models based on encoder networks primarily leverage layers related to self-attention mechanisms and feed-forward networks as part of their neural network architecture. 

---

The third one is the combination of autoencoding and autoregressive such as the T5 (Text-to-Text Transfer Transformer) model. Developed by Google in 2020, T5 LLM can perform natural language understanding (NLU) and natural language generation (NLG). T5 LLM can be understood as a pure transformer using both encoder and decoder networks.

---

**GPT (Generative Pretrained Transformer)**

- Developed by OpenAI, GPT is a generative model designed for text completion, conversation, and content creation.
- It is autoregressive, meaning it predicts text word by word based on previous tokens.
- Uses causal attention (only looks at previous words) to ensure coherent generation.
- Example: Chatbots, AI-assisted writing, creative text generation.

**BERT (Bidirectional Encoder Representations from Transformers)**

BERT (Bidirectional Encoder Representations from Transformers), developed by Google, is one of the most famous autoencoding language models. It can be fine-tuned for a variety of NLP tasks, such as sentiment analysis, named entity recognition and question answering. 

- Developed by Google, BERT is optimized for understanding context rather than generating text.
- It is bidirectional, meaning it considers both previous and next words to derive deeper meaning.
- Great for tasks like question answering, sentiment analysis, and search engine optimization.
- Example: Google Search improvements, document classification.

---

![image](https://github.com/user-attachments/assets/9cee3a84-5240-44e8-995b-136b10a189e4)


<img width="1063" height="247" alt="image" src="https://github.com/user-attachments/assets/3bdf1e82-3225-4878-9330-20a47074e20a" />


https://medium.com/data-science/a-complete-guide-to-bert-with-code-9f87602e4a11

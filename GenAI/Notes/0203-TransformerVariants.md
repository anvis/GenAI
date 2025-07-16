
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

**GPT (Generative Pretrained Transformer)**

- Developed by OpenAI, GPT is a generative model designed for text completion, conversation, and content creation.
- It is autoregressive, meaning it predicts text word by word based on previous tokens.
- Uses causal attention (only looks at previous words) to ensure coherent generation.
- Example: Chatbots, AI-assisted writing, creative text generation.

**BERT (Bidirectional Encoder Representations from Transformers)**

- Developed by Google, BERT is optimized for understanding context rather than generating text.
- It is bidirectional, meaning it considers both previous and next words to derive deeper meaning.
- Great for tasks like question answering, sentiment analysis, and search engine optimization.
- Example: Google Search improvements, document classification.

---

![image](https://github.com/user-attachments/assets/9cee3a84-5240-44e8-995b-136b10a189e4)


<img width="1063" height="247" alt="image" src="https://github.com/user-attachments/assets/3bdf1e82-3225-4878-9330-20a47074e20a" />


https://medium.com/data-science/a-complete-guide-to-bert-with-code-9f87602e4a11

**Why Outputs Differ**:

- Training Data Differences:  
Each LLM is trained on different datasets, timeframes, and filtering strategies. 
That means their "knowledge base" and learned patterns vary.

- Model Architecture & Parameters:  
Even if two models are trained on similar data, differences in architecture (e.g., transformer size, attention mechanisms, fine-tuning methods)
affect how they interpret prompts.

- Sampling & Randomness:  
Most LLMs use probabilistic sampling (temperature, top-k, nucleus sampling). 
This introduces randomness, so the same prompt can produce multiple valid continuations.

- Prompt Interpretation:  
Models don’t “understand” prompts the way humans do; they predict the next token based on probability. 
Slight differences in tokenization or context handling can shift the output.

- Context Window & Memory:  
How much text the model can “see” at once (its context window) influences the response. 
Larger windows allow more nuanced answers, smaller ones force truncation or simplification.

- Fine-Tuning & Alignment:  
Some models are tuned for creativity, others for factual accuracy or safety. 
That tuning changes the “style” of the output even with identical prompts.

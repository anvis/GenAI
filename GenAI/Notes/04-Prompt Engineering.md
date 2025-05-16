# Prompt Engineering

## Table of Contents
- [Prompt Engineering](#Prompt-Engineering)
- [Types of Prompts](#Types-of-Prompts)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prompt Engineering
This project does XYZ...

https://developers.google.com/machine-learning/resources/prompt-eng

https://medium.com/the-generator/the-perfect-prompt-prompt-engineering-cheat-sheet-d0b9c62a2bba



## Types of Prompts
 Zero-shot, few-shot prompting.

**Zero Shot Prompting:**

Zero-shot prompting is an AI technique where model perform tasks without examples. 
This approach falls under Zero-Shot Learning (ZSL), allowing models to tackle new tasks by leveraging their pre-trained knowledge, without needing any task-specific data. 

Flow: 
1) User asks Query
2) AI model processes the query and infers the task from its extensive training data.
3) With its pre-trained knowledge, the model analyzes the query. It uses the context and patterns it has learned during its training to understand how to address the task at hand.
4) Finally, the model generates a response based on its understanding of the task.

**Few Shot Prompting** :

Few Short Prompting is a technique in artificial intelligence (AI) where model learn to perform tasks with very few examples reducing the need for large datasets. It falls under Few Shot Learning (FSL) which enables models to adapt quickly to new tasks with minimal data making it particularly useful in situations with limited data.

Flow: 
1) User asks Query.
2) A collection of examples, previously stored in a vector store, is used to match and find the most relevant information.
3) A collection of examples, previously stored in a vector store, is used to match and find the most relevant information.
4) After fetching the relevant examples, the system combines them with the user query to create a clear prompt.
5) Model processes this constructed prompt, utilizing its pre-existing knowledge and the provided examples, then it generates an output by applying the knowledge learned from those examples to the query.

   example of few shot prompting
   https://www.youtube.com/watch?v=R9BjOa4Pkdc
   


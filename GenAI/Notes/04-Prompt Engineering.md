# Prompt Engineering

## Table of Contents
- [Prompt Engineering](#Prompt-Engineering)
- [Types of Prompts](#Types-of-Prompts)
- [Prompt Tuning](#Prompt-Tuning)
- [Contributing](#contributing)
- [License](#license)

## Prompt Engineering

**Your prompts define the LLM’s behavior**

It’s how we turn raw model capabilities into real-world functionality. A small change in phrasing can significantly alter the output — making prompt design both powerful and delicate.


In production environments, poor prompts result in:

- Hallucinated or vague answers
- Inconsistent formats
- Missed tasks and user frustration
- Higher token usage and latency
  
Effective prompts result in:

- Clear, structured, accurate outputs
- Predictable, robust behavior
- Lower costs and better user experience



https://developers.google.com/machine-learning/resources/prompt-eng

https://medium.com/the-generator/the-perfect-prompt-prompt-engineering-cheat-sheet-d0b9c62a2bba

---


## Types of Prompts

### **Instruction-Based Prompts**

Use when: You want the model to perform a clear task (summarize, translate, analyze, etc.)

Summarize the following meeting transcript into 3 concise bullet points.

```
Yesterday's meeting included updates on the marketing campaign...
```

### **Role-Based Prompts**

Use when: You want the model to adopt a tone, domain knowledge, or point of view.

```
You are a senior software engineer. Explain the concept of async/await in Python to a beginner developer.
```

 ### **Few-Shot Prompting**

Use when: You want to guide behavior with examples.
 
Providing a few examples within the prompt helps the model learn the desired format or style of response. This technique can improve the model's accuracy by showing it patterns to follow.

Few Short Prompting is a technique in artificial intelligence (AI) where model learn to perform tasks with very few examples reducing the need for large datasets. 

It falls under Few Shot Learning (FSL) which enables models to adapt quickly to new tasks with minimal data making it particularly useful in situations with limited data.

```
Convert the following product reviews into sentiment labels (Positive, Negative, Neutral):

Review: "The battery life is great!"  
Sentiment: Positive
Review: "It stopped working after a week."  
Sentiment:
```

Flow: 
1) User asks Query.
2) A collection of examples, previously stored in a vector store, is used to match and find the most relevant information.
3) A collection of examples, previously stored in a vector store, is used to match and find the most relevant information.
4) After fetching the relevant examples, the system combines them with the user query to create a clear prompt.
5) Model processes this constructed prompt, utilizing its pre-existing knowledge and the provided examples, then it generates an output by applying the knowledge learned from those examples to the query.

   example of few shot prompting
   https://www.youtube.com/watch?v=R9BjOa4Pkdc
    
### **Zero-Shot Prompting**
This approach allows the model to handle tasks without any specific examples in the prompt. It relies on the model's general understanding and knowledge to generate responses.

Zero-shot prompting is an AI technique where model perform tasks without examples. 
This approach falls under Zero-Shot Learning (ZSL), allowing models to tackle new tasks by leveraging their pre-trained knowledge, without needing any task-specific data. 

Flow: 
1) User asks Query
2) AI model processes the query and infers the task from its extensive training data.
3) With its pre-trained knowledge, the model analyzes the query. It uses the context and patterns it has learned during its training to understand how to address the task at hand.
4) Finally, the model generates a response based on its understanding of the task.
    
### **One-Shot Prompting**
This technique involves giving the model a single example of the desired input-output relationship before asking it to generate a response. For instance, if you want the model to solve a math problem, you would first provide one example of a similar problem and its solution.

###  **Chain of Thought Prompting**
This technique encourages the model to break down complex tasks into smaller, logical steps.
By guiding the model to think through the problem, it can arrive at more accurate solutions.

```
Q: Jane has 5 red balloons and gives away 2. How many does she have left?  
A: Let's think step by step.
```

- Use cues like: Let’s think step by step, Show your reasoning, Break it down
- Chain-of-thought improves performance on reasoning, problem-solving, and planning tasks

###  **Structured Output Prompts**

Use when: You need the output in a machine-readable format (JSON, YAML, tables).

```
Extract the following information in JSON format:  
1. Event name  
2. Date  
3. Location

"""
Join us for AI Summit 2025 on June 2nd in Berlin at the City Conference Center.
"""

Output:

{
 "event_name": "AI Summit 2025",
 "date": "June 2nd, 2025",
 "location": "City Conference Center, Berlin"
 }

```
    
###  **In-Context Learning**
This method involves providing instructions or examples directly in the prompt, allowing the model to learn from the context provided.

---

## Prompt Tuning

Prompt tuning involves modifying the input prompts given to a foundation model to elicit better responses for a particular task. This technique focuses on optimizing the prompts rather than retraining the entire model.

Prompt tuning is a technique in generative AI which allows models to target specific tasks effectively. By crafting prompts, whether through a hands-on approach with hard prompts or through an automated process with soft prompts, we enhance the model's predictive capabilities.

Prompt tuning is a technique for optimizing AI model responses by adjusting prompts rather than modifying the model itself. Unlike fine-tuning, which updates model weights, prompt tuning refines how prompts interact with the model to improve accuracy and relevance.

### **How Prompt Tuning Works**

- Soft Prompt Initialization – Learnable prompts are introduced to guide the model.
- Forward Pass & Loss Assessment – The model processes input with soft prompts and compares output to expected results.
- Backpropagation & Refinement – Only the soft prompts are updated, not the entire model, ensuring efficient adaptation.

### **Types of Prompt Tuning Techniques**

- Chain-of-Thought Prompting (CoT) – Encourages step-by-step reasoning for complex tasks.
- Self-Consistency Decoding – Generates multiple responses and selects the most frequent one.
- Tree-of-Thought Prompting (ToT) – Explores multiple reasoning paths for diverse solutions.

### **Why Prompt Tuning Matters**

- Efficiency – Reduces computational cost compared to full model fine-tuning.
- Adaptability – Allows models to specialize in tasks without retraining.
- Improved Accuracy – Enhances response quality for specific applications

---


   


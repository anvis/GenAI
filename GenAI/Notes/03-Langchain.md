
LangChain

## Table of Contents
- [Introduction to Langchain](#Introduction-to-Langchain)
- [Integration with OpenAI and Other Models](#Integration-with-OpenAI-and-Other-Models)
- [Prompt Templating](#Prompt-Templating)
- [Chains](#Chains)
- [Agents](#Agents)
- [Memory](#Memory)
- [Document Loaders](#Document-Loaders)
- [Retrieval QA](#Retrieval-QA)

## Introduction to Langchain
LangChain is a framework for developing applications powered by large language models (LLMs). 
It simplifies the process of building, deploying, and managing AI-driven applications by providing tools for context-aware reasoning, orchestration, and integration with various AI models.

LangChain is a wrapper around the LLM (Open AI), instead of directly working with Open AI we can use LangChain.

LangChain can simultaneously call multiple LLM's for different tasks and integrate the response for desired output. 

LangChain is a framework designed to orchestrate and integrate large language models (LLMs) into applications. It provides tools for prompt engineering, memory management, and agent-based workflows, making it easier to build AI-powered applications.

LangChain is particularly useful when working with AI agents, orchestration, and memory in LLM-based applications. 





## Integration with OpenAI and Other Models
Steps to install:
1. Clone the repo
2. Run `npm install`
3. Start the server with `npm start`

## Prompt Templating

LangChain provides prompt templates to structure inputs for language models, ensuring consistency and adaptability. These templates help format user input into structured prompts, making interactions with LLMs more effective.

Types of Prompt Templates in LangChain:

- String PromptTemplates – Used for simple text formatting.

       'from langchain_core.prompts import PromptTemplate
       prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
       print(prompt_template.invoke({"topic": "cats"}))'



- ChatPromptTemplates – Used for multi-message interactions.from langchain_core.prompts 

            'import ChatPromptTemplate
       prompt_template = ChatPromptTemplate([("system", "You are a helpful assistant"),
                                            ("user", "Tell me a joke about {topic}")])
      print(prompt_template.invoke({"topic": "cats"}))'

- MessagesPlaceholder – Allows dynamic insertion of multiple messages.

            'from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
       from langchain_core.messages import HumanMessage
       prompt_template = ChatPromptTemplate([("system", "You are a helpful assistant"),
                                            MessagesPlaceholder("msgs")])
       print(prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]}))'



## Chains
Combining multiple components for complex tasks.
        -  **Simple Sequential Chains**: Combining chains in a sequence.
        -  **Sequential Chains**: More advanced sequencing with input/output keys.
        
chains are sequences of operations that process inputs and generate outputs by linking together various components like LLMs, retrievers, memory, and tools.
Chains link multiple functions and pass output from one function as input to other function.

LangChain provides various chain types that allow developers to build and customize workflows for natural language processing tasks. These chain types help streamline the integration of language models and other tools into applications. So basically a chain type is nothing more than tying together a series of tasks where we are chaining together different task and we are passing the input from the first one over to the next one. The pipe operator is used to act like a chain for each sub sequent tasks.



Types of Chains in LangChain:

**LLMChain** – The simplest chain, where a prompt is passed to an LLM and the response is returned.
   ```python
   from langchain_core.prompts import PromptTemplate
   from langchain_core.llms import OpenAI
   from langchain.chains import LLMChain

   prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
   llm = OpenAI(model="gpt-4")
   chain = LLMChain(llm=llm, prompt=prompt)
   print(chain.invoke({"topic": "cats"}))
   ```
**SequentialChain** – Executes multiple chains in sequence, passing outputs from one to the next.
   ```python
   from langchain.chains import SequentialChain

   chain1 = LLMChain(llm=llm, prompt=PromptTemplate.from_template("Describe {topic}"))
   chain2 = LLMChain(llm=llm, prompt=PromptTemplate.from_template("Summarize the description"))
   sequential_chain = SequentialChain(chains=[chain1, chain2])
   print(sequential_chain.invoke({"topic": "quantum computing"}))
   ```
**RouterChain** – Routes inputs to different chains based on conditions.
**RetrievalQAChain** – Uses a retriever to fetch relevant documents before querying an LLM.
**ConversationalRetrievalChain** – Maintains memory for context-aware responses.

LangChain’s **chains** allow for modular, reusable workflows, making AI applications more structured and scalable.



## Agents
Autonomous entities using tools (e.g., Google Search API via Surp API).

## Memory
Retaining conversation history.
        *   **Conversation Buffer Memory**: Simple storage of conversation history.
        *   **Conversation Buffer Window Memory**: Limiting the retained history.

## Document Loaders
Reading various document types (PDF, CSV, TXT, etc.).

## Retrieval QA
Question answering over an index.

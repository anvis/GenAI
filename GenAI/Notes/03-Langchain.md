
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

A prompt template in LangChain is a structured way to create prompts with dynamic inputs for language models. It consists of a text string, often referred to as “the template,” which can incorporate parameters provided by users to generate a specific prompt

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

- System Message Template: This is like instructions for an AI before it starts talking to you. It sets the rules for how the AI should behave, what it can do, and how it should respond.
- 
- Human Message Template: This is more like a guide for people when they talk to an AI. It helps users ask questions in a way that gets the best response.

Think of it like this: The system message is like telling a chef how to cook, and the human message is like ordering food from the menu. The chef (AI) follows the instructions, while the customer (you) chooses what to ask.


## Chains
Combining multiple components for complex tasks.
        -  **Simple Sequential Chains**: Combining chains in a sequence.
        -  **Sequential Chains**: More advanced sequencing with input/output keys.
        
chains are sequences of operations that process inputs and generate outputs by linking together various components like LLMs, retrievers, memory, and tools.
Chains link multiple functions and pass output from one function as input to other function.

LangChain provides various chain types that allow developers to build and customize workflows for natural language processing tasks. These chain types help streamline the integration of language models and other tools into applications. So basically a chain type is nothing more than tying together a series of tasks where we are chaining together different task and we are passing the input from the first one over to the next one. The pipe operator is used to act like a chain for each sub sequent tasks.

 A “chain” refers to a sequence of actions or tasks that are linked together to achieve a specific goal. You can create a chain that takes user input, processes it with a language model, and then generates a response.


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

An Agent is a component that plays a vital role in determining the next steps or actions to be taken within a chain of calls to language models (LLMs) or other tools. 
An Agent has access to a suite of tools and toolkits which it uses to make decisions on the next action in the sequence.

**Agent Types**:

ZERO_SHOT_REACT_DESCRIPTION: This is a zero-shot agent that performs a reasoning step before acting. It's suitable for scenarios where an immediate response is required without prior training.

ZERO_SHOT_REACT_DESCRIPTION is a type of agent that performs a reasoning step before taking action. It does not rely on any chat history, meaning it makes decisions based solely on the current input. This makes it suitable for scenarios where an immediate response is required without the need for context from previous interactions.

REACT_DOCSTORE: This is also a zero-shot agent that performs a reasoning step before acting. However, this agent has access to a document store that allows it to look up relevant information to answer the question. It's suitable for scenarios where the answer can be found in a document store.

SELF_ASK_WITH_SEARCH: This agent breaks down a complex question into a series of simpler questions and uses a search tool to look up answers to the simpler questions in order to answer the original complex question. It's suitable for scenarios where the question is complex and needs to be broken down.

CONVERSATIONAL_REACT_DESCRIPTION: This agent is designed to hold a conversation in addition to using tools. It has methods for creating prompts, validating tools, and constructing an agent from a language model and tools.

CHAT_ZERO_SHOT_REACT_DESCRIPTION: This is a zero-shot agent that performs a reasoning step before acting and is designed to be used in conjunction. 

CHAT_ZERO_SHOT_REACT_DESCRIPTION also performs a reasoning step before acting, but unlike `ZERO_SHOT_REACT_DESCRIPTION`, it uses a chat history variable in the prompt. This means that the final prompt will include the chat history, allowing the agent to remember the context of the chat and the history of the conversation. This agent type is designed for multi-turn tasks that require maintaining the context of a conversation.

CHAT_CONVERSATIONAL_REACT_DESCRIPTION: The context does not provide information about this agent type.

STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION: This is a zero-shot react agent optimized for chat models. This agent is capable of invoking tools that have multiple inputs. It's suitable for chat scenarios where multiple inputs are required.

OPENAI_FUNCTIONS: This is an agent optimized for using open AI functions. It's suitable for scenarios where open AI functions are required.

OPENAI_MULTI_FUNCTIONS: 

## Memory
Retaining conversation history.
        *   **Conversation Buffer Memory**: Simple storage of conversation history.
        *   **Conversation Buffer Window Memory**: Limiting the retained history.

## Document Loaders
Reading various document types (PDF, CSV, TXT, etc.).

## Retrieval QA
Question answering over an index.

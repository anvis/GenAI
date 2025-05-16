from Models.llm import llm

geminiModel = llm.get_Gemini_model() 


# - Set Up Conversation Memory:

from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history")

# - Define Tools for the Agent

from langchain.agents import Tool

def simple_tool(query):
    return f"You asked about: {query}"

tools = [Tool(name="SimpleTool", func=simple_tool, description="A basic tool for answering queries.")]

# Create the ZeroShot Agent

from langchain.agents import initialize_agent
from langchain.agents import AgentType

agent = initialize_agent(
    tools=tools,
    llm=geminiModel,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# - Run the Agent:

response = agent.run("Tell me about LangChain.")
print(response)
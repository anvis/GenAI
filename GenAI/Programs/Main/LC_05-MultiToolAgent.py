from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from Models.llm import llm

# Define tools
def calculator(expression):
    print("Entering calculator tool")
    return eval(expression)

calc_tool = Tool(name="Calculator", func=calculator, description="Performs basic calculations.")

def search_tool(query):
    print("Entering search tool")
    return f"Searching for: {query}"  # Replace with actual search API

search_tool = Tool(name="SearchTool", func=search_tool, description="Searches the web for information.")

# Initialize LLM
geminiModel = llm.get_Gemini_model() 

# Create agent
agent = initialize_agent(
    tools=[calc_tool, search_tool],
    llm=geminiModel,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
response = agent.run("What is 25 * 4?")
print(response)
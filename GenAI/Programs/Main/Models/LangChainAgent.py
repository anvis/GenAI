from langchain.agents import initialize_agent

"""
    Returns:
        An initialized LangChain agent.
"""

def getAgent(model, tools, AgentType, verbose=True):  
    # Initialize the agent
    agent = initialize_agent(
        tools=tools,
        llm=model,
        agent=AgentType,
        verbose=verbose
    )
    
    return agent
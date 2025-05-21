from langchain.agents import AgentType
from Models.llm import llm
from Models.LangChainAgent import getAgent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

geminiModel = llm.get_Gemini_model()

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper, search_type="search", search_results=1)
tools = [wiki_tool]
ZeroShotAgentType = AgentType.ZERO_SHOT_REACT_DESCRIPTION

agent = getAgent(geminiModel, tools, ZeroShotAgentType, True)

response = agent.run("Who was the first person to walk on the moon?")
print(response)



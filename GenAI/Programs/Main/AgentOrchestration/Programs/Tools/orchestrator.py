from langchain.agents import initialize_agent


#### LLM Import and Setup #####
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from getpass import getpass

# Define environment variables
os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyDHyo4-lEgmnpIJLQK5i58EYUTo50A9EXs")
os.environ["LANGCHAIN_API_KEY"] = getpass("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")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../../../../Resources/googleCreds.json")
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0"

GOOGLE_API_KEY = "AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20"



def get_Gemini_ChatModel(modelName="gemini-2.0-flash"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0,max_tokens=None)
    return llm

llm = get_Gemini_ChatModel("gemini-2.5-flash")

print("gemini models")
from google import generativeai
generativeai.configure(api_key=os.environ["GOOGLE_API_KEY"] )
print(generativeai.list_models()) 

#### LLM Import and Setup #####

def summarizer_tool(text: str) -> str:
    # Simulate summarization
    prompt = f"Summarize the following information in 5 concise sentences:\n\n{text}"
    return llm.invoke(prompt)

from langchain.agents import  Tool
from langchain.utilities import DuckDuckGoSearchAPIWrapper

search = DuckDuckGoSearchAPIWrapper()


def researcher_tool(query: str) -> str:
    # Simulate web search
    return search.run(query)

researcher = Tool(
    name="Researcher",
    func=researcher_tool,
    description="Fetches raw info from web"
)

summarizer = Tool(
    name="Summarizer",
    func=summarizer_tool,
    description="Summarizes raw info"
)


agent = initialize_agent(
    tools=[researcher, summarizer],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Run orchestration
result = agent.run("Tell me about agentic AI orchestration")
print(result)

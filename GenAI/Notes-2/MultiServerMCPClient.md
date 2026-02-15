

import asyncio
import tracemalloc
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from getpass import getpass

tracemalloc.start()

# It's a best practice to load secrets from environment variables.
# os.environ["OPENAI_API_KEY"] = "sk-..."


os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../googleCreds.json")

GOOGLE_API_KEY = "AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20"

def get_Gemini_ChatModel(modelName="gemini-2.5-flash"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0,max_tokens=None)
    return llm

gemini_llm = get_Gemini_ChatModel("gemini-2.5-flash")

model = gemini_llm

# --- 1. Initialize Non-Async Components ---
client = MultiServerMCPClient(
    {
        "MongoDB": {
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "mongodb-mcp-server",
                "mongodb://localhost:27017"
                #mongodb+srv://username:password@cluster.mongodb.net/database
                #"mongodb://username:password@localhost:27017/database"
                #"mongodb://localhost:27017/database"
                #mongodb://host:port
            ]
        }
    }
)


# --- 2. Define the Core Asynchronous Logic ---
async def setup_agent():
    print("🚀 Starting MongoDB MCP Client...")
    tools = await client.get_tools()
    print(f"✅ Tools loaded: {list(tools)}")
    return create_react_agent(model=model, tools=tools)

agent = asyncio.run(setup_agent())

async def chat_function(message: str, history: list = None):
    print(f"\n💬 User Message: {message}")
    response_dict = await agent.ainvoke(
        {"messages": [{"role": "user", "content": message}]}
    )
    print("🤖 Agent Response:", response_dict)
    return response_dict['messages'][-1].content


# --- 3. Wrapper Method for Queries ---
async def run_query(question: str, history: list = None, print_response: bool = True):
    print("Run a single query and return the response.")   
    response = await chat_function(question, history or [])
    if print_response:
        print(f"\nQuery: {question}")
        print("Response:", response)
    return response

# --- 4. Example Usage with Fixed Queries ---
async def main():
    print("Main function started.")
    queries = [
        "Tell me all mongo collections in Articles database"
        #,"List all databases",
        #"How many documents are in the 'users' collection?"
    ]
    history = []
    for q in queries:
        print(f"\n--- Running Query: {q} ---")
        resp = await run_query(q, history)
        print(f"Response for '{q}': {resp}")
        history.append((q, resp))

if __name__ == "__main__":
    asyncio.run(main())




MultiServerMCPClient

is a LangChain adapter that manages connections to one or more Model Context Protocol (MCP) servers. It's the glue between your LLM agent and external tools/services.

What it does in your code:

Initializes connections to MCP servers (in your case, the MongoDB server) via subprocess (stdio transport).
Launches the MongoDB MCP server by running:
npx -y mongodb-mcp-server

Exposes tools — via await client.get_tools(), it retrieves all available tools/capabilities from connected servers and converts them into LangChain-compatible tool objects.
Bridges communication between your agent and the external servers over stdin/stdout.
In your setup:

client = MultiServerMCPClient(
    {
        "MongoDB": {
            "transport": "stdio",           # communicate via stdin/stdout
            "command": "npx",               # run via npm
            "args": ["-y", "mongodb-mcp-server"]  # launch mongodb-mcp-server
        }
    }
)

Then in setup_agent():

tools = await client.get_tools()  # Get all MongoDB tools
return create_react_agent(model=model, tools=tools)  # Pass to ReAct agent

Result: Your Gemini LLM agent can now query MongoDB via natural language by calling the MongoDB MCP tools directly, without implementing database logic yourself.

Key benefit: The MCP server handles the actual MongoDB queries; your agent just orchestrates them based on user requests.



what this line is doing? agent = asyncio.run(setup_agent())

This line initializes the agent synchronously at module load time by running an async function.

Breaking it down:

setup_agent() — an async function that:

Connects to the MongoDB MCP server via client.get_tools()
Retrieves all available MongoDB tools
Creates a ReAct agent (Reasoning + Acting) with your Gemini LLM + MongoDB tools
Returns the configured agent
asyncio.run(...) — runs the async function to completion in a new event loop, blocking until done

agent = ... — stores the initialized agent in a module-level variable

Result: By the time your code reaches main(), the agent is already ready to use—it has all MongoDB capabilities loaded and can invoke them on demand.

Why this pattern?

The agent setup is expensive (spawning the MCP server, discovering tools), so you do it once at startup.
Later async functions (chat_function, run_query, main) can call await agent.ainvoke(...) without re-initializing.
Note: This creates a blocking operation at module import. If you wanted to delay initialization or avoid blocking, you could move this inside main() instead.



what is the use of await agent.ainvoke

sends a user query to the agent and waits for the result.

Breaking it down:

response_dict = await agent.ainvoke(
    {"messages": [{"role": "user", "content": message}]}
)

agent.ainvoke(...) — async method that invokes the ReAct agent

ainvoke = "async invoke" (the 'a' prefix means async)
Input format:

{"messages": [{"role": "user", "content": message}]}


Standard chat format: list of messages with role (user/assistant) and content
Sent to Gemini LLM + MongoDB tools
Agent workflow:

Takes your user message (e.g., "Tell me all mongo collections")
Reasons about what it means
Decides which MongoDB MCP tool to call (e.g., listCollections())
Executes the tool via the MCP server
Returns a structured response dict with the result
await — pauses execution until the agent finishes and returns the response

Result:

return response_dict['messages'][-1].content  # Extract the final answer

Extracts the last message's content (the agent's final answer)
Example flow:

User: "Tell me all mongo collections"
Agent reasons: "I need to call MongoDB tool to list collections"
Agent calls tool → MCP server queries MongoDB → returns collection names
Agent formats answer and returns it
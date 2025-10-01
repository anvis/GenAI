***Model Context Protocol***

- MCP (Model Context Protocol) is a standardized way for LLMs to interact with external tools, APIs, and files.
  
- MCP Server: A lightweight service that acts as a bridge between LLMs and external tools—files, APIs, databases, etc.
It standardizes how AI models interact with the outside world.
Usually exposed by companies that provide services, similar to API. Server Exposes multiple tools for services it provides.
The MCP Server acts like a tool registry and execution engine. It hosts tools and exposes them to LLMs via a structured protocol.


- MCP Client: The interface (often embedded in the agent or orchestration layer) that sends structured requests to the MCP server and receives responses.
  
- MCP Host: The Application we are building. We create Clients in our Application.

Before MCP,
- Each tool (Slack, GitHub, Google Maps) needed its own custom connector logic.
- LLMs couldn’t “see” or act on real-time data from external systems without complex plumbing.

MCP Solved these issues by, 
- Standardized protocol for tool access
- Secure, layered architecture (auth, ACLs, input/output sanitization)
- Fail-safe patterns (circuit breakers, caching, rate limiting)
- Composable connectors reusable across agents and models

Why MCP Server Is Useful
- LLMs are blind to external systems unless explicitly connected.
- MCP solves this by letting you define tools (e.g., file search, API calls, database queries) and expose them to the model in a consistent format.


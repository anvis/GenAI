from langchain.agents import Tool, AgentType, initialize_agent
from Models.llm import llm
from Models.LangChainAgent import getAgent
from Models.Prompts.Gemini import Prompt

geminiModel = llm.get_Gemini_model()

def execute_code(code):
    print("Executing code...")
    print(code)
    return code

def write_python_code(text: str):
    prompt =  Prompt("Write Python code for the following task:\n{input_text}\n\nCode:")
    chain = prompt | geminiModel
    response = chain.invoke({"input_text": text}, verbose=False)
    print(response)


#code_tool = Tool(name="Python Executor", func=execute_code, description="Executes Python code.")
code_tool = Tool(
    name="PythonCodeWriter",
    func=write_python_code,
    description="Generates Python code based on user instructions."
)
ZeroShotAgentType = AgentType.ZERO_SHOT_REACT_DESCRIPTION


code_agent = getAgent(geminiModel, code_tool, ZeroShotAgentType, True)

response = code_agent.run("Write a Python function that calculates the factorial of a number.")
print(response)





from Models.llm import llm
from Models.Prompts.Gemini import Prompt


geminiModel = llm.get_Gemini_model()

def write_python_code(text: str):
    prompt =  Prompt("Write Python code for the following task:\n{input_text}\n\nCode:")
    chain = prompt | geminiModel
    response = chain.invoke({"input_text": text}, verbose=False)
    print(response)

def write_cSharp_code(text: str):
    prompt =  Prompt("Write c# code for the following task:\n{input_text}\n\nCode:")    

    chain = prompt | geminiModel
    response = chain.invoke({"input_text": text}, verbose=False)
    print(response)

write_cSharp_code("factorial of a number.")






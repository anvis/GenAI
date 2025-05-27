from Models.Prompts.Gemini import Prompt_System_Human
from Models.llm import get_Gemini_model


llm = get_Gemini_model("gemini-2.0-flash")

prompt = Prompt_System_Human("You are an astronomer, knowledgeable about the solar system", "Question:{question}")


chain = prompt | llm
response = chain.invoke({"question": "How many moons does Jupiter have?"})
print(response)
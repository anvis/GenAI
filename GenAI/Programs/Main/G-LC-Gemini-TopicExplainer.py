
from Models.llm import get_Gemini_model
from Models.Prompts.Gemini import Prompt


llm = get_Gemini_model("gemini-2.0-flash")

template = Prompt(
    "Explain {topic} in detail for a age {age} year old would understand"
)

chain = template | llm
topic = input("Hugging Face")   
age = input("30")
response = chain.invoke({"topic": topic, "age": age})
print(response)

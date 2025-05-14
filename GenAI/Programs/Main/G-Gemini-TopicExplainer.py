
from Models.llm import get_Gemini_model
from langchain.prompts import PromptTemplate


llm = get_Gemini_model("gemini-2.0-flash")

template = PromptTemplate.from_template(
    "Explain {topic} in detail for a age {age} year old would understand"
)

chain = template | llm
topic = input("Hugging Face")   
age = input("30")
response = chain.invoke({"topic": topic, "age": age})
print(response)

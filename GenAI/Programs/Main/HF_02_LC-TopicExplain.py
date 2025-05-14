from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate

model_id = "meta-llama/Meta-Llama-3-8B"

#tokenizer = AutoTokenizer.from_pretrained(model_id)

model = pipeline("text-generation", model=model_id, device=0)

# Wrap it inside LangChain
llm = HuggingFacePipeline(pipeline=model)

# Create the prompt template for summarization
template = PromptTemplate.from_template(
    "Explain {topic} in detail for a age {age} year old would understand"
)

chain = template | llm

topic = input("Hugging Face")
age = input("10")

response = chain.invoke({"topic": topic, "age": age})
print(response)
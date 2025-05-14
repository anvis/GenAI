from Models.llm import get_Gemini_model, llm
#from langchain_google_genai import systempromptmessage, humanpromptmessage
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"


chat_prompt = llm.get_ChatPromptTemplate(template, human_template)

messages = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

gemini_model = llm.get_Gemini_model()

chain = chat_prompt | gemini_model # LLMChain(llm=llm, prompt=messages)

response = chain.invoke({"text": "I love programming.", "input_language": "English", "output_language": "French"})
print(response)



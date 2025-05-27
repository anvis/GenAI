from Models.llm import llm
from Models.Prompts.Gemini import Prompt_System_Human

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = Prompt_System_Human(template, human_template)

#messages = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

gemini_model = llm.get_Gemini_model()

chain = chat_prompt | gemini_model # LLMChain(llm=llm, prompt=messages)

response = chain.invoke({"text": "I love programming.", "input_language": "English", "output_language": "French, Hindi"})
print(response.content)

system_Text_GrammerCheck = "You are a grammar checker. Correct the grammar in the following text."
human_Text_GrammerCheck = "Correct the grammar in the following text: {text}"
chat_prompt_GrammerCheck = Prompt_System_Human(system_Text_GrammerCheck, human_Text_GrammerCheck)

GrammerChecker = chat_prompt_GrammerCheck | gemini_model 

response = GrammerChecker.invoke({"text": "Get out house my you"})
print(response.content)



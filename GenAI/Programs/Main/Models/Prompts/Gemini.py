from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate


def Prompt(text:str):
    template = PromptTemplate.from_template(text)
    return template


def Prompt_System_Human(systemText:str, HumanText:str):
    chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",systemText),
        ("human",HumanText)
    ]
    )
    return chat_prompt



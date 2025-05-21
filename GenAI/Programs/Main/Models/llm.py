from langchain_google_genai import ChatGoogleGenerativeAI
from Common import Config
from langchain.prompts.chat import ChatPromptTemplate

class llm:
    _systemText = "Default Name"
    _humanText = "Default Human Text"

    @property
    def systemText(self):
        return self._systemText

    @systemText.setter
    def systemText(self, new_systemText):
        if isinstance(new_systemText, str) and new_systemText.strip():
            llm._systemText = new_systemText  

    @property
    def humanText(self):
        return self._humanText

    @humanText.setter
    def humanText(self, new_humanText):
        if isinstance(new_humanText, str) and new_humanText.strip():
            llm._humanText = new_humanText  
    

    def get_Gemini_model(modelName="gemini-2.0-flash"):
    # Initialize Gemini model
        llm = ChatGoogleGenerativeAI(model=modelName, temperature=0,max_tokens=None)
        return llm

    
    def get_ChatPromptTemplate(systemText=None, humanText=None):
       
       # systemText = systemText if systemText else self.systemText
      #  humanText = humanText if humanText else self.humanText

        chat_prompt = ChatPromptTemplate.from_messages([
             ("system", systemText),
            ("human", humanText),
        ])
        return chat_prompt









## -------------------------------------------

def get_Gemini_model(modelName="gemini-1.5-pro"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0)
    return llm
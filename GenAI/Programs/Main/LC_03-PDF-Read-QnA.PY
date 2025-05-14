from Models.PDFReader import Read, Read_SplitText, Read_GenAI
import os
from Models.llm import llm

fileName = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Resources/Files/Trans.pdf"))

geminiModel = llm.get_Gemini_model() 

qa_chain = Read_GenAI(geminiModel, "models/embedding-001", fileName)

# Query documents
query = "What is the main topic of the document?"
answer = qa_chain.invoke(query)
print("Answer:", answer)


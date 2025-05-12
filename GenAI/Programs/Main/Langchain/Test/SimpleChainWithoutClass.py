#from langchain.schema import RunnableLambda, SequentialChain
from langchain_core.runnables import RunnableLambda
from langchain.chains import SequentialChain, SimpleSequentialChain

# Define steps as independent functions
extract_keywords = RunnableLambda(lambda text: [word.lower() for word in text.split() if len(word) > 3])
sort_keywords = RunnableLambda(lambda keywords: sorted(keywords))

# Chain the steps
chain = SimpleSequentialChain(
    chains=[extract_keywords, sort_keywords],
    verbose=True)

# Example usage
result = chain.invoke("LangChain enables dynamic workflows for data processing")
print(result)
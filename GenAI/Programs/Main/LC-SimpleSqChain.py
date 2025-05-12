from Models.llm import get_Gemini_model
import warnings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain


warnings.filterwarnings("ignore")

llm = get_Gemini_model("gemini-2.0-flash") #ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

template = '''You are a movie genre recommendor. Given the user's favorite genre: {genre}, suggest three related genres.
 
Suggests genres:'''
prompt_template = PromptTemplate(input_variables=["genre"], template=template)
chain_one = LLMChain(llm=llm, prompt=prompt_template)


template2 = '''You are a movie recommender. Given the user's favorite genres: {genres}, suggest some movies that fall under these genres.
 
Suggest movies:'''
prompt_template = PromptTemplate(input_variables=["genres"], template=template2)
chain_two = LLMChain(llm=llm, prompt=prompt_template)

# Link the two chains together in a sequential manner  
# The output of chain_one will be passed as input to chain_two  
overall_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=True)

# Run the overall chain with a sample input 
overall_chain.run('Romance')
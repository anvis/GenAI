from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from Models.llm import llm

# Step 1: Define the schema for the structured output
response_schemas = [
    ResponseSchema(name="name", description="The name of the person"),
    ResponseSchema(name="age", description="The age of the person in years"),
    ResponseSchema(name="hobbies", description="A list of hobbies the person enjoys"),
]

# Step 2: Create a StructuredOutputParser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Step 3: Define the format instructions for the output
format_instructions = output_parser.get_format_instructions()

# Step 4: Create a ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides structured information."),
    ("user", "Please provide the following details about a person: name, age, and hobbies."),
    ("assistant", f"Sure! I will provide the details in the following format:\n{format_instructions}"),
    ("user", "The person's name is Alex, they are 29 years old, and they enjoy hiking, painting, and reading."),
])

# Step 5: Initialize the chat model
#chat_model = ChatOpenAI(temperature=0)

geminiModel = llm.get_Gemini_model() 

# Step 6: Generate a response
response = geminiModel(prompt.to_messages())

# Step 7: Parse the response into structured data
parsed_response = output_parser.parse(response.content)

# Output the structured data
print(parsed_response)

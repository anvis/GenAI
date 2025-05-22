from Models.llm import llm
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional
import logging
from datetime import datetime
from langchain.output_parsers import StructuredOutputParser
from langchain_core.output_parsers import PydanticOutputParser




# --------------------------------------------------------------
# Set up logging configuration
# --------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# --------------------------------------------------------------
# Initialize Gemini Model
# --------------------------------------------------------------

geminiModel = llm.get_Gemini_model()

# --------------------------------------------------------------
# Step 1 :: Defining Classes
# --------------------------------------------------------------

class EventExtraction(BaseModel):
    description: str = Field(description="Raw description of the event")
    is_calendar_event: bool = Field(
        description="Whether this text describes a calendar event"
    )
    confidence_score: float = Field(description="Confidence score between 0 and 1")


class EventDetails(BaseModel):
    name: str = Field(description="Name of the event")
    date: str = Field(
        description="Date and time of the event. Use ISO 8601 to format this value."
    )
    duration_minutes: int = Field(description="Expected duration in minutes")
    participants: list[str] = Field(description="List of participants")
    
class EventConfirmation(BaseModel):
    confirmation_message: str = Field(
        description="Natural language confirmation message"
    )
    calendar_link: Optional[str] = Field(
        description="Generated calendar link if applicable"
    )   

# --------------------------------------------------------------
# Step 2: Define the functions
# --------------------------------------------------------------

def extract_event_info(user_input: str) -> EventExtraction:
    logger.info("Starting event extraction analysis")
    logger.debug(f"Input text: {user_input}")

    today = datetime.now()
    date_context = f"Today is {today.strftime('%A, %B %d, %Y')}."
    

    #output_parser = StructuredOutputParser.from_response_schemas(EventExtraction)
    #output_parser =  PydanticOutputParser(pydantic_object=EventExtraction)
    #format_instructions = output_parser.get_format_instructions()

    print("Format Instructions:")
    #print(format_instructions)


    prompt=ChatPromptTemplate.from_messages(
    [
        ("system",f"{date_context} Analyze if the text describes a calendar event."),
        ("user",f"{user_input}")
        #("assistant",f"Answer: {format_instructions}"),
        
    ]
    )
    print("Prompt Template:")
    print(prompt)
    chain=prompt|geminiModel
    result= chain.invoke({"user_input": user_input})
    print(result)


user_input = "Let's schedule a 1h team meeting next Tuesday at 2pm with Alice and Bob to discuss the project roadmap."
response = extract_event_info( user_input)
logger.info("Event extraction analysis completed")
print(response)



'''


'''
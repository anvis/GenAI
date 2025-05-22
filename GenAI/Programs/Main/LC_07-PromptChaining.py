from Models.llm import llm
from pydantic import BaseModel, Field
from typing import Optional
import logging
from datetime import datetime
from langchain.output_parsers import StructuredOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from Models.Prompts.Gemini import Prompt_System_Human


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

    geminiModel = llm.get_Gemini_model().with_structured_output(EventExtraction)

    today = datetime.now()
    date_context = f"Today is {today.strftime('%A, %B %d, %Y')}."

    prompt=Prompt_System_Human(
   f"{date_context} Analyze if the text describes a calendar event.", f"{user_input}")
    
    chain=prompt|geminiModel
    result= chain.invoke({"user_input": user_input})

    print("Printing Description:")
    print(result.description)

    print("Printing is_calendar_event:")
    print(result.is_calendar_event)

    print("Printing confidence_score:")
    print(result.confidence_score)

    return result

def parse_event_details(description: str) -> EventDetails:
     logger.info("Starting parse Event analysis")
     logger.debug(f"Input text: {description}")

     geminiModel = llm.get_Gemini_model().with_structured_output(EventDetails)

     today = datetime.now()
     date_context = f"Today is {today.strftime('%A, %B %d, %Y')}."

     prompt=Prompt_System_Human(f"{date_context} Extract detailed event information. When dates reference 'next Tuesday' or similar relative dates, use this current date as reference.",
        f"{description}")
      
     chain=prompt|geminiModel
     result= chain.invoke({"description": description})

     print("Printing name:")
     print(result.name)

     print("Printing date:")
     print(result.date)

     print("Printing duration_minutes:")
     print(result.duration_minutes)

     print("Printing participants:")
     print(result.participants)
     return result


def generate_confirmation(event_details: EventDetails) -> EventConfirmation:
     logger.info("Generating confirmation message")

     prompt=Prompt_System_Human("Generate a natural confirmation message for the event. Sign of with your name; susie",
         f"{event_details}")
     
     geminiModel = llm.get_Gemini_model().with_structured_output(EventConfirmation)
     eventDetails = str(event_details.model_dump())

     chain=prompt|geminiModel
     result= chain.invoke({"event_details": eventDetails})
     return result
# --------------------------------------------------------------



# Step 3: Main execution

user_input = "Let's schedule a 1h team meeting next Tuesday at 2pm with Alice and Bob to discuss the project roadmap."
user_input01 = "Can you send an email to Alice and Bob to discuss the project roadmap?"

initial_extraction = extract_event_info(user_input)
logger.info("Event extraction analysis completed")

if (not initial_extraction.is_calendar_event or initial_extraction.confidence_score < 0.7):
        logger.warning(f"Gate check failed - is_calendar_event: {initial_extraction.is_calendar_event}, confidence: {initial_extraction.confidence_score:.2f}")
        #return None
else:
    logger.info("Gate check passed, proceeding with event processing")

    # Second LLM call: Get detailed event information
    event_details = parse_event_details(initial_extraction.description)

    confirmation = generate_confirmation(event_details)

    if confirmation:
        print(f"Confirmation: {confirmation.confirmation_message}")
        if confirmation.calendar_link:
            print(f"Calendar Link: {confirmation.calendar_link}")
    else:
        print("This doesn't appear to be a calendar event request.")


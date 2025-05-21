#from langchain.chat_models import ChatGoogle
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
import requests
from Models.llm import llm

# Initialize Gemini Model
geminiModel = llm.get_Gemini_model() 

# Function to Fetch Weather Data
def get_weather(latitude, longitude):
    #api_key = "YOUR_WEATHER_API_KEY"
    url =  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"The weather in : {data['current']['condition']['text']}, {data['current']['temp_c']}°C"
    else:
        return f"Error fetching weather for coordinates ({latitude}, {longitude}): {response.status_code}"

# Define Weather Tool for LangChain Agent
weather_tool = Tool(
    name="WeatherAPI",
    func=get_weather,
    description="Fetches current weather details for a given city."
)

# Initialize LangChain Agent
agent = initialize_agent(
    tools=[weather_tool],
    llm=geminiModel,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example Query
response = agent.run("What is the weather in Hyderabad?")
print(response)



## ---------------------------------


from langchain.chat_models import ChatGoogle
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
import requests

# Initialize Gemini Model
llm = ChatGoogle(model="gemini-pro")

# Function to Generate Coordinates via Gemini
def get_coordinates(city):
    query = f"Provide latitude and longitude for {city}."
    response = llm.invoke([query])
    
    try:
        lat, lon = map(float, response.split(","))
        return lat, lon
    except:
        return "Error parsing coordinates"

# Function to Fetch Weather Data
def get_weather(city):
    lat, lon = get_coordinates(city)
    
    if isinstance(lat, str):  # Error case
        return lat
    
    api_key = "YOUR_WEATHER_API_KEY"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city}: {data['current']['condition']['text']}, {data['current']['temp_c']}°C"
    else:
        return f"Error fetching weather for {city}"

# Define Weather Tool for LangChain Agent
weather_tool = Tool(
    name="WeatherAPI",
    func=get_weather,
    description="Fetches current weather details based on city name."
)

# Initialize LangChain Agent
agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example Query
response = agent.run("What is the weather in Hyderabad?")
print(response)
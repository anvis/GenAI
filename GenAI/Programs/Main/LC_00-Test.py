#from langchain.chat_models import ChatGoogle
import requests
import json
from Models.llm import llm

# Initialize Gemini Model
geminiModel = llm.get_Gemini_model()

# Restructured Mapping Document
mapping_document = {
    "https://api1.example.com/user": ["user_name", "email"],
    "https://api2.example.com/balance": ["account_balance", "currency"],
    "https://api3.example.com/history": ["transaction_history", "last_transaction"]
}

# Function to Fetch Data in One Call per API
def fetch_data():
    results = {}
    for api, properties in mapping_document.items():
        print(f"Fetching data from {api} for properties: {properties}")
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            for prop in properties:
                results[prop] = data.get(prop, f"'{prop}' not found in response")
        else:
            for prop in properties:
                results[prop] = f"Error {response.status_code}: Unable to fetch {prop}"
    return results

# Ask Gemini for API Execution Logic
query = "Determine which properties need to be fetched based on provided API schema."
response = geminiModel.invoke([query])
print("Gemini Response:", response)

# Execute API Calls
final_results = fetch_data()
print(final_results)

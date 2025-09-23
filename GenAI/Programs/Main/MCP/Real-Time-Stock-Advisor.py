#################Import LLM #################

import os
import mcp

from getpass import getpass
from langchain_google_genai import ChatGoogleGenerativeAI


# Define environment variables
os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20")
os.environ["LANGCHAIN_API_KEY"] = getpass("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")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../../Resources/googleCreds.json")
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0"

GOOGLE_API_KEY = "AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20"



def get_Gemini_ChatModel(modelName="gemini-2.0-flash"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0,max_tokens=None)
    return llm



#gemini_llm = get_Gemini_ChatModel("gemini-2.0-flash")

#################Import LLM #################

##########Ticker Extraction############

# Sample lookup dictionary
TICKER_MAP = {
    "hdfc": "HDFCBANK",
    "reliance": "RELIANCE",
    "tcs": "TCS",
    "infosys": "INFY",
    "icici": "ICICIBANK",
    "sbi": "SBIN",
    "hdfc bank": "HDFCBANK",
    "state bank of india": "SBIN"
}

import re

def extract_ticker(query):
    query_lower = query.lower()
    for name, ticker in TICKER_MAP.items():
        if re.search(rf"\b{name}\b", query_lower):
            return ticker
    return None

def extract_ticker_with_gemini(query):
    prompt = f"""
    Extract the stock ticker symbol from this user query:
    "{query}"

    Respond with only the ticker symbol (e.g., HDFCBANK, INFY, TCS).
    """
    response = llm.invoke(prompt)
    return response.content.strip()


def get_ticker(query):
    ticker = extract_ticker(query)
    if ticker:
        return ticker
    return extract_ticker_with_gemini(query)

##########Ticker Extraction############


from mcp import ClientSession

# Define MCP servers
price_server = ClientSession("https://financial-datasets-mcp.com", "62a31f50-9abf-4560-955d-a493288682cc")
news_server = ClientSession("https://google-researcher-mcp.com", "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")
# trade_server = ClientSession("https://zerodha-mcp.com")

llm = get_Gemini_ChatModel("gemini-2.0-flash")

async def handle_query(user_query):
    ticker = get_ticker(user_query)  

    # Step 1: Get current price
    async with ClientSession(...) as session:
        tool = session.get(price_server)  # e.g., 'query_sql_db'
        result = await tool.call_tool("get_current_stock_price", {"ticker": ticker})

    #price_result = price_server.get("get_current_stock_price", {"ticker": ticker})

    # Step 2: Get recent news
    news_result = news_server.get("get_company_news", {"company": ticker})

    # Step 3: Compose prompt for Gemini
    prompt = f"""
    User asked: "{user_query}"

    Current price of {ticker}: ₹{price_result['price']}
    Recent news:
    {news_result['headlines']}

    Based on this, should the user consider buying {ticker} today?
    """

    # Step 4: Get Gemini's response
    response = llm.invoke(prompt)
    return response.content



import streamlit as st

st.title("Real-Time Stock Advisor")
query = st.text_input("Ask your question (e.g. Should I buy HDFC?)")

if st.button("Submit") and query:
    response = handle_query(query)
    st.markdown("### Response")
    st.write(response)
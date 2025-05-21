import os
from getpass import getpass

# Define environment variables
#os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyAx3V4SgE2KCjrGQ37iyvkCevFnrkIhA8w")
os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20")
os.environ["LANGCHAIN_API_KEY"] = getpass("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")
#os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"] = getpass("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")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../../Resources/googleCreds.json")
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0"

GOOGLE_API_KEY = "AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20"



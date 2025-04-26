import os
from getpass import getpass

# Define environment variables
os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyAx3V4SgE2KCjrGQ37iyvkCevFnrkIhA8w")
os.environ["LANGCHAIN_API_KEY"] = getpass("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")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../../Resources/GoogleCredentials.json")


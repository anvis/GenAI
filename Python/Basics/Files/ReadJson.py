
import json
import os

# Open and read the JSON file
with open(os.path.dirname(__file__) + '/data.json', 'r') as file:
    data = json.load(file)

# Access the data
print(data)


import json
from json.decoder import JSONDecodeError

try:
    with open(os.path.dirname(__file__) + '/dat.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found.")
except JSONDecodeError:
    print("Invalid JSON format.")

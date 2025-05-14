from Models.llm import llm
from Models.URLLoader import Read

url = "https://medium.com/@anveshgouds/human-intelligence-b10c570b7206"
summary = Read( llm.get_Gemini_model(), url)

print("summary\n")
print(summary)

document = summary['input_documents'][0]

print("document\n")
print(document)
print("page content\n")
page_content = document.page_content

'''
# Extracting the required fields
source = document['metadata']['source']
title = document['metadata']['title']


# Printing the extracted values
print("Source:", source)
print("Title:", title)
print("Page Content:", page_content)


'''
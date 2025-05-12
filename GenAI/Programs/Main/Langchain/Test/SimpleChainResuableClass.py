from langchain.chains.base import Chain

# Define simple functions
def extract_keywords(text: str) -> list:
    """Extracts simple keywords from a sentence."""
    words = text.split()
    return [word.lower() for word in words if len(word) > 3]

def sort_keywords(keywords: list) -> list:
    """Sorts keywords alphabetically."""
    return sorted(keywords)

# Create a simple chain
class SimpleChain(Chain):
    def __init__(self):
        super().__init__()
        self.steps = [self.extract_step, self.sort_step]

    def invoke(self, input_text):
        keywords = self.extract_step(input_text)
        sorted_keywords = self.sort_step(keywords)
        return sorted_keywords

    def extract_step(self, input_text):
        return extract_keywords(input_text)

    def sort_step(self, keywords):
        return sort_keywords(keywords)

# Example usage
simple_chain = SimpleChain()
result = simple_chain.invoke("LangChain enables dynamic workflows for data processing")
print(result)
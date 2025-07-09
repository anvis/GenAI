import os

def fetch_lines():
    with open(os.path.dirname(__file__) + '/data.txt', 'r') as file:
        lines = []
        for line in file:
            # yield line.strip()
            lines.append(line.strip())
        return lines

#data = fetch_lines()
#print(data)

def fetch_generator():
    with open(os.path.dirname(__file__) + '/data.txt', 'r') as file:
        for line in file:
            yield line.strip()

generator = fetch_generator()
print(generator)
print(next(generator))  # Fetch the first line
print(next(generator))  # Fetch the second line 
print(list(generator))  # Fetch the remaining lines



    
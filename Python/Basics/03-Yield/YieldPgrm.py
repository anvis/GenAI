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
#print(list(generator))  # Fetch the remaining lines

print("Using yield to fetch chunks of data")

def fetch_chunk():
    with open(os.path.dirname(__file__) + '/data.txt', 'r') as file:
        while chunk := file.read(2):
            yield chunk

chunck = fetch_chunk()
print(chunck)
print(next(chunck))  # Fetch the first chunk
print(next(chunck))  # Fetch the second chunk
    
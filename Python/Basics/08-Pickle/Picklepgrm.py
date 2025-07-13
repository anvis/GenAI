import pickle
import os

basePath = os.path.dirname(__file__)

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        return f"{self.name} is {self.color}"
    
apple = Fruit("Apple", "Red") 

# Serialize the object to a binary format
with open(basePath + '/fruit.pkl', 'wb') as file:
    pickle.dump(apple, file)

# Deserialize the object from the binary format
with open(basePath + '/fruit.pkl', 'rb') as file:
    loaded_apple = pickle.load(file)
# Access the data
print(loaded_apple.describe())


print("# Attempt to load a non-existent file")

try:
    with open('non_existent.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
except FileNotFoundError:
    print("File not found.")
except pickle.UnpicklingError:
    print("Error unpickling the data.")


print("# Create a dictionary to be pickled")

data = {'name': 'Banana', 'color': 'Yellow'}
# Serialize the dictionary to a binary format
with open(basePath + '/data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize the dictionary from the binary format
with open(basePath + '/data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
# Access the data
print(loaded_data)


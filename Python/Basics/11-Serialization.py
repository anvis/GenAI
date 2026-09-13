
import json
import os

json_str = '{"name": "Rex", "age": 3, "breed": "Labrador"}'
data = json.loads(json_str)  # "loads" = load from string

print(data)         # {'name': 'Rex', 'age': 3, 'breed': 'Labrador'}
print(data["name"]) # Rex
print(type(data))   # <class 'dict'>

#################################

import json

with open(os.path.dirname(__file__) + '/data.json', 'r') as f:
    data = json.load(f)  # "load" = load from file object (no 's')

print(data)

#####################################

import json

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

json_str = '{"name": "Rex", "age": 3, "breed": "Labrador"}'
data = json.loads(json_str)

dog = Dog(**data)   # unpack dict keys as keyword arguments
print(dog)           # Dog(name=Rex, age=3, breed=Labrador)
print(dog.name)      # Rex

################################

print("Using object_hook (automatic conversion during parsing)")

# Using object_hook (automatic conversion during parsing)

def dog_decoder(d):
    return Dog(**d)

json_str = '{"name": "Rex", "age": 3, "breed": "Labrador"}'
dog = json.loads(json_str, object_hook=dog_decoder)
print(dog)  # Dog(name=Rex, age=3, breed=Labrador)

############################################

print("Data Class")

import json
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    breed: str

json_str = '{"name": "Rex", "age": 3, "breed": "Labrador"}'
data = json.loads(json_str)
dog = Dog(**data)

print(dog)  # Dog(name='Rex', age=3, breed='Labrador')


#############################################

print("Pydantic")


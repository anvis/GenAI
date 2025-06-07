class Person:
    def __init__(self, name):
        self._name = name  # Using a private variable convention (_name)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():  # Ensuring valid input
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")
    
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

# Example usage
person = Person("Anvesh")
print(person.name)  # Accessing property
person.name = "Raj"  # Setting property
print(person.name) 
del person.name      # Deleting property
print("Deleting name...") 
 
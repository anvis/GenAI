class Person:
    _name = "Default Name"  # Class-level attribute
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            Person._name = new_name  # Modify class-level attribute
        else:
            raise ValueError("Name must be a non-empty string.")

    @name.deleter
    def name(self):
        print("Deleting name...")
        del Person._name

# Example usage
p1 = Person()
print(p1.name)  # Accessing property

p1.name = "Anvesh"  # Setting property without __init__
print(p1.name)  # Updated property

del p1.name  # Deleting property
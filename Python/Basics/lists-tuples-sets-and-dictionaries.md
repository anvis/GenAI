
Python: lists, tuples, sets, and dictionaries. Each of these structures offers unique features and functionalities suitable for different use cases:


**Lists**

provide an ordered, mutable collection of items, allowing for easy manipulation and dynamic resizing. They are perfect for maintaining sequences of elements where modifications are required.

**Tuples**

offer an immutable alternative to lists, making them ideal for representing fixed collections of items. Their immutable nature ensures data integrity and can also lead to performance optimizations in certain scenarios.

We can create a new tuple by modifying existing Tuple.

**Sets**

are valuable for handling unique items and enabling efficient membership testing and set operations such as union, intersection, and difference. They are particularly useful for eliminating duplicates and performing mathematical set operations.

**Dictionaries**

enable the storage of key-value pairs, facilitating quick data retrieval based on unique keys. This makes dictionaries essential for managing structured data, configurations, and any scenario where fast lookups are necessary.

List Examples

```
Creating a list of OS

operating_systems = ["Linux", "Windows", "MacOS"]  
print(operating_systems)

first_os = operating_systems[0]   # 'Linux'  
second_os = operating_systems[1]  # 'Windows'
```

Tuple Examples

```
# Creating a tuple of cars  
cars = ("BMW", "Cadillac", "Ford")  
print(cars)

# Accessing elements  
first_car = cars[0]   # 'BMW'  
second_car = cars[1]  # 'Cadillac'
```

Set Examples

```
# Creating a set of cars  
cars = {"BMW", "Cadillac", "Ford"}  
print(cars)

# Creating a set of operating systems  
operating_systems = {"Windows", "macOS", "Linux"}  

# Adding an element  
operating_systems.add("Ubuntu")  

# Removing an element  
operating_systems.remove("Windows")  # Raises KeyError if 'Windows' is not found  
# operating_systems.discard("Windows")  # Safely removes 'Windows' if it exists  

print(operating_systems)

# Creating a set of numbers  
numbers = {1, 2, 3, 4, 5}  

# Testing membership  
is_three_in_set = 3 in numbers  # True  
is_six_in_set = 6 in numbers    # False  

print("Is 3 in numbers?", is_three_in_set)  
print("Is 6 in numbers?", is_six_in_set)

```

Dictionary Examples

```
# Creating a dictionary to store fruit prices  
fruit_prices = {  
    "apple": 0.60,  
    "banana": 0.50,  
    "cherry": 1.00  
}  
print(fruit_prices)

# Accessing prices  
apple_price = fruit_prices["apple"]  # Using brackets  
banana_price = fruit_prices.get("banana", "Not found")  # Using get()  

print("Apple Price:", apple_price)  
print("Banana Price:", banana_price)

# Removing an entry using del  
del fruit_prices["cherry"]

```

---


Here’s a clear breakdown of the differences between **lists**, **tuples**, **sets**, and **dictionaries** in Python — each with its own personality and purpose:

### 🧩 Overview Table

| Feature           | List            | Tuple           | Set             | Dictionary        |
|------------------|-----------------|-----------------|-----------------|-------------------|
| **Syntax**        | `[ ]`           | `( )`           | `{ }`           | `{key: value}`    |
| **Ordered**       | ✅ Yes          | ✅ Yes          | ❌ No           | ✅ Yes (Py 3.7+)   |
| **Mutable**       | ✅ Yes          | ❌ No           | ✅ Yes          | ✅ Yes             |
| **Duplicates**    | ✅ Allowed      | ✅ Allowed      | ❌ Not allowed  | ❌ Keys only       |
| **Indexing**      | ✅ Integer      | ✅ Integer      | ❌ No           | ✅ Key-based       |
| **Use Case**      | Collections     | Fixed records   | Unique items    | Key-value mapping |

---

### 📚 Detailed Breakdown

#### 1. **List**
- Ordered and mutable.
- Allows duplicates.
- Ideal for dynamic collections.
- Example:  
  ```python
  fruits = ['apple', 'banana', 'apple']
  fruits.append('orange')
  ```

#### 2. **Tuple**
- Ordered but immutable.
- Allows duplicates.
- Great for fixed data like coordinates or constants.
- Example:  
  ```python
  point = (10, 20)
  ```

#### 3. **Set**
- Unordered and mutable.
- No duplicates allowed.
- Perfect for membership tests and set operations.
- Example:  
  ```python
  unique_numbers = {1, 2, 3, 2}
  # Result: {1, 2, 3}
  ```

#### 4. **Dictionary**
- Ordered (since Python 3.7) and mutable.
- Keys must be unique; values can repeat.
- Best for mapping relationships.
- Example:  
  ```python
  student = {'name': 'Anvesh', 'age': 30}
  ```

---





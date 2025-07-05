
In Python, a **dataclass** is a decorator that simplifies the creation of classes meant primarily for storing data. Introduced in Python 3.7, it automatically generates special methods like `__init__()`, `__repr__()`, and `__eq__()` so you don’t have to write boilerplate code.

---

### 🧰 Why Use `@dataclass`?

- Reduces repetitive code
- Improves readability and maintainability
- Supports default values, immutability, ordering, and more

---

### 🧪 Basic Example

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    department: str = "Engineering"

emp = Employee("Anvesh", 30)
print(emp)
# Output: Employee(name='Anvesh', age=30, department='Engineering')
```

---

### ⚙️ Key Features

| Feature         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `init=True`     | Auto-generates `__init__()` constructor                                     |
| `repr=True`     | Auto-generates `__repr__()` for readable string representation             |
| `eq=True`       | Auto-generates `__eq__()` for comparisons                                   |
| `order=True`    | Adds ordering methods like `__lt__`, `__gt__`, etc.                         |
| `frozen=True`   | Makes the instance immutable (like a read-only object)                     |
| `slots=True`    | Optimizes memory usage by creating `__slots__`                             |

---

### 🧬 Advanced Use: Default Factories

```python
from dataclasses import dataclass, field

@dataclass
class Project:
    name: str
    contributors: list = field(default_factory=list)
```

This avoids the common pitfall of using mutable default arguments like `contributors = []`.

---

### 🔄 Conversion Utilities

- `asdict(obj)` → Converts dataclass to dictionary
- `astuple(obj)` → Converts dataclass to tuple

---

Would you like to see how dataclasses compare to regular classes or how they’re used in AI workflows like config management or model metadata?

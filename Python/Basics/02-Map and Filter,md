
In Python, `map()` and `filter()` are powerful built-in functions that let you process iterables in a clean, functional style. Here's a breakdown to help you master them:

---

### 🗺️ `map()` — Transforming Data

The `map()` function applies a given function to **every item** in an iterable (like a list or tuple).

**Syntax:**
```python
map(function, iterable)
```

**Example:**
```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

🔹 You can also use lambdas:
```python
squared = map(lambda x: x * x, numbers)
```

---

### 🧹 `filter()` — Selecting Data

The `filter()` function filters elements from an iterable based on a **Boolean condition**.

**Syntax:**
```python
filter(function, iterable)
```

**Example:**
```python
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(is_even, numbers)
print(list(evens))  # Output: [2, 4, 6]
```

🔹 With lambdas:
```python
evens = filter(lambda x: x % 2 == 0, numbers)
```

---

### 🧠 Key Differences

| Feature        | `map()`                          | `filter()`                          |
|----------------|----------------------------------|-------------------------------------|
| Purpose        | Transforms each item             | Selects items based on condition    |
| Return Type    | `map` object (convert to list)   | `filter` object (convert to list)   |
| Function Output| Any value                        | Must return `True` or `False`       |

---





TODO
---
Decorators in Python are a powerful way to **augment or modify the behavior of functions** without changing their actual code. They’re especially useful for logging, access control, memoization, timing, and more. Here's a structured breakdown to help you master them:

---

### 🧠 What Is a Decorator?

- A **decorator** is a higher-order function that takes another function as input and returns a new function with extended behavior.
- It uses the `@decorator_name` syntax to wrap the target function.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Anvesh")
```

---

### 🔧 Common Use Cases

| Use Case         | Example Decorator         | Purpose                                  |
|------------------|---------------------------|------------------------------------------|
| Logging          | `@log_calls`              | Track function calls and arguments       |
| Authentication   | `@require_login`          | Check user credentials before execution  |
| Timing           | `@measure_time`           | Measure execution time                   |
| Caching          | `@lru_cache`              | Store results for faster reuse           |
| Validation       | `@validate_input`         | Ensure inputs meet criteria              |

---

### 🧩 Decorators with Arguments

You can pass arguments to decorators by nesting them:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
```

---

### 🧪 Built-in Decorators

- `@staticmethod`: Defines a method that doesn’t access instance or class data.
- `@classmethod`: Operates on the class rather than an instance.
- `@property`: Turns a method into a read-only attribute.

---

### 🧵 Chaining Decorators

You can stack multiple decorators:

```python
@log_calls
@measure_time
def process_data():
    pass
```

The innermost decorator (`@measure_time`) is applied first.

---

Would you like to explore how decorators can be used in AI workflows or LangChain agents? I think you'd enjoy how they can modularize tool wrappers and memory handlers.

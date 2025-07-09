
Decorators in Python
---

Pre-requisites

**Functions as Objects**

``` python
def f1():
    print("f1 called")
    
def f2(f):
    f()
    return 1

f2(f1)
    
print(f1) # This will print the function object

print(f1()) # This will call the function and print its return value (None in this case)

print(f2(f1)) # This will call the function and print its return value (None in this case)

Output:

f1 called
<function f1 at 0x000001F12EDD1440>
f1 called
None
f1 called
1

```

**Wrapper Functions**

``` python
def wrapperFunc(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

def Executer():
    print("f4 called")

f5 = wrapperFunc(Executer)  # Wrap f4 with f3
print("---calling f5()---")
f5()  # Call the wrapped function
print("---printing f5---")
print(f5)  # This will print the wrapper function object

print("---calling wrapperFunc(Executer) ---")
wrapperFunc(Executer)  # This will return the wrapper function, but not call it
print("---calling wrapperFunc(Executer)()---")
wrapperFunc(Executer)()  # This will call the wrapper function, which in turn calls f4

Output:

---calling f5()---
Before calling the function
f4 called
After calling the function
---printing f5---
<function wrapperFunc.<locals>.wrapper at 0x0000022DABC7FEC0>
---calling wrapperFunc(Executer) ---
---calling wrapperFunc(Executer)()---
Before calling the function
f4 called
After calling the function
```

**Using Decorator Keyword**

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

Output:
Before function call
Hello, Anvesh!
After function call


@my_decorator
def add(a, b):  
    return a + b

result = add(5, 3)
print(f"Result of add: {result}")

Output:

Before function call
After function call
Result of add: 8

```

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

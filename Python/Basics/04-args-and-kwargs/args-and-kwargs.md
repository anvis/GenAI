
In Python, *args and **kwargs are used to make functions more flexible by allowing them to accept variable numbers of arguments.

---

🧵 *args – Non-keyword Variable Argument

- Collects positional arguments into a tuple.
- Useful **when you don’t know how many arguments will be passed.**

``` python
nums = [1,2,3,4,5]

print(nums)

print(*nums)  # Unpacking the list

output

[1, 2, 3, 4, 5]
1 2 3 4 5
```

``` python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # Output: 6
```

---

 **kwargs – Keyword Variable Argument

- Collects named arguments into a dictionary.
- Useful **for passing optional or named parameters.**

``` python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Anvesh", role="AI Engineer")

name: Anvesh
role: AI Engineer
```

---

You can combine them to accept any mix of arguments:

``` python
def mixed_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

mixed_args(1, 2, 3, name="Anvesh", level="Intermediate")
```

---

🧪 Function Calls with Unpacking

You can also use them when calling functions:

``` python
def greet(name, age):
    print(f"Hello {name}, age {age}")

args = ("Anvesh", 30)
kwargs = {"name": "Anvesh", "age": 30}

greet(*args)
greet(**kwargs)

```



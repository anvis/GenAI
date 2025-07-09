def f1():
    print("f1 called")
    
def f2(f):
    f()
    return 1

f2(f1)
    
print(f1) # This will print the function object

print(f1()) # This will call the function and print its return value (None in this case)

print(f2(f1)) # This will call the function and print its return value (None in this case)


## Wrapper Functions Example


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

print("111")
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


print("222")

@my_decorator
def add(a, b):  
    return a + b

result = add(5, 3)
print(f"Result of add: {result}")

add(10, 20)  # This will also print the decorator messages
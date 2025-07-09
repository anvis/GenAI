def f1():
    print("f1 called")
    
def f2(f):
    f()
    return 1

f2(f1)
    
print(f1) # This will print the function object

print(f1()) # This will call the function and print its return value (None in this case)

print(f2(f1)) # This will call the function and print its return value (None in this case)



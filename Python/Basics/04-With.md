
The with statement in Python is used for resource management and exception handling. 
It ensures that resources are properly acquired and released, making the code cleaner and more readable.

It simplifies working with resources like files, network connections and database connections by ensuring they are properly acquired and released. 
When we open a file, we need to close it ourself using close(). But if something goes wrong before closing, the file might stay open, causing issues. 
Using with open() automatically closes the file when we're done, even if an error happens.

**Example**: Without with (Manual closing)

```python

file = open("example.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed

```

**Example**: Using With

``` python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File closes automatically
```

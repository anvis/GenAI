

---

### 📥 Basic JSON File Reading

#### ✅ Using `json.load()` for files
```python
import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the data
print(data)
```
- This reads the file and converts it into a Python dictionary or list depending on the JSON structure.

#### ✅ Using `json.loads()` for strings
```python
import json

json_string = '{"name": "Anvesh", "skills": ["Python", ".NET", "AI"]}'
data = json.loads(json_string)

print(data['skills'])
```

---

### 🧠 Tips for Complex JSON Structures

If your JSON has nested objects:
```python
# Access nested values
city = data['user']['address']['city']
```

---

### 🛡️ Error Handling Example
```python
import json
from json.decoder import JSONDecodeError

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found.")
except JSONDecodeError:
    print("Invalid JSON format.")
```

---

### 🎨 Pretty Print JSON
```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))
```

---



## Table of Contents
- [What Is Pickle](#What-Is-Pickle)
- [Pickle vs Json](#Pickle-vs-Json)
- [Pickle vs Dill](#Pickle-vs-Dill)

---
## What Is Pickle

The pickle module in Python is a powerful tool for serializing and deserializing Python objects.

- Serialization (Pickling): Converts Python objects (e.g., lists, dicts, custom classes) into a byte stream.
- Deserialization (Unpickling): Reconstructs the original object from the byte stream.
- Useful for saving objects to disk, sending them over a network, or storing in databases.
- Unlike JSON, pickle uses a binary format.
- Pickle is ideal for saving Python-specific objects like classes, functions, and complex data structures.
- It’s simpler than JSON for internal use but not safe for external data exchange.


 ---


### 🔧 Core Functions

| Function         | Purpose                                      |
|------------------|----------------------------------------------|
| `pickle.dump(obj, file)` | Serialize `obj` to a file-like object |
| `pickle.load(file)`      | Deserialize object from file          |
| `pickle.dumps(obj)`      | Serialize `obj` to bytes              |
| `pickle.loads(bytes)`    | Deserialize object from bytes         |

---

### 🧪 Example

```python
import pickle

# Pickling
data = {'name': 'Anvesh', 'role': 'AI Engineer'}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

wb = Write Binary
pickle.dump = writes the object to a file
This will actually cretes a file in folder.


# Unpickling
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

rb = Read Binary
pickle.load = restores the object
This will read the file from folder to internal memory.


print(loaded_data)
```

---
## Pickle vs Json


| Feature            | Pickle                          | JSON                          |
|--------------------|----------------------------------|-------------------------------|
| Format             | Binary                          | Text                          |
| Human-readable     | ❌                              | ✅                            |
| Cross-language     | ❌ Python-specific               | ✅ Language-independent       |
| Custom objects     | ✅ Supports complex types        | ❌ Limited to basic types     |
| Security           | ❌ Risk of code execution        | ✅ Safer for untrusted data   |


---
## Pickle vs Dill


### 🧠 Dill vs Pickle: Feature Comparison

| Feature                          | `pickle`                          | `dill`                             |
|----------------------------------|-----------------------------------|------------------------------------|
| Standard Library                 | ✅ Yes                            | ❌ No (needs `pip install dill`)   |
| Custom Functions (e.g. lambdas) | ❌ Limited support                | ✅ Full support                    |
| Nested Functions                | ❌ Not supported                  | ✅ Supported                       |
| Closures / Cell Objects         | ❌ Not supported                  | ✅ Supported                       |
| Interpreter Session State       | ❌ Not supported                  | ✅ Can serialize entire session    |
| Source Code Inspection          | ❌ No                             | ✅ Via `dill.source`               |
| Multiprocessing Compatibility   | ❌ Limited                        | ✅ Used in `multiprocess` fork     |
| Performance                     | ✅ Faster                         | ❌ Slightly slower                 |
| Security                        | ❌ Not secure                     | ❌ Not secure                      |

---

### 🔍 Use Cases Where `dill` Shines

- **LangChain Agents**: Serializing memory buffers, nested logic, or lambda-based tools.
- **Machine Learning Pipelines**: Storing `FunctionTransformer` with custom logic.
- **Session Persistence**: Saving and restoring entire interpreter states for reproducibility.
- **Advanced AI Workflows**: Serializing closures, decorators, and dynamically generated functions.

---

### 🧪 Example: Lambda Serialization

```python
import dill

# Serialize a lambda
squared = lambda x: x ** 2
with open('lambda.dill', 'wb') as f:
    dill.dump(squared, f)

# Deserialize and use
with open('lambda.dill', 'rb') as f:
    loaded_func = dill.load(f)

print(loaded_func(5))  # Output: 25
```

---

### ⚠️ Caveats

- **Performance**: Dill is more flexible but slower than pickle.
- **Compatibility**: Dill pickles may not be backward-compatible across versions.
- **Security**: Like pickle, dill is unsafe for untrusted data.

---



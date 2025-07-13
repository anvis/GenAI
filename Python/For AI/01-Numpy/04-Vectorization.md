
Vectorization in NumPy is a technique that allows you to perform **operations on entire arrays without using explicit loops**. This is a cornerstone of efficient numerical computing and is especially critical in AI workflows where performance and scalability matter.

---

## ⚡ What Is Vectorization?

- **Definition**: Replacing slow Python loops with fast, array-wide operations.
- **Powered by**: NumPy’s underlying C implementation.
- **Benefit**: Massive speedup and cleaner code.

- Vectorization is about speed and loop elimination.
- Broadcasting is about shape compatibility and memory efficiency.
- They often work together: broadcasting enables vectorized operations on arrays of different shapes


🔗 [AskPython’s guide to vectorization](https://www.askpython.com/python-modules/numpy/vectorization-numpy)  
🔗 [GeeksforGeeks practical examples](https://www.geeksforgeeks.org/numpy/vectorized-operations-in-numpy/)

---

## 🧪 Examples of Vectorized Operations

### 1️⃣ Element-wise Arithmetic
```python
import numpy as np
a = np.array([1, 2, 3])
b = a + 10  # [11, 12, 13]
```

### 2️⃣ Element-wise Comparison
```python
a = np.array([10, 20, 30])
mask = a > 15  # [False, True, True]
```

### 3️⃣ Matrix Multiplication
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)  # [[19, 22], [43, 50]]
```

### 4️⃣ Aggregations
```python
a = np.array([1, 2, 3])
print(a.sum())   # 6
print(a.mean())  # 2.0
```

---

## 🧠 Why It Matters in AI

| Benefit             | AI Impact                                      |
|---------------------|------------------------------------------------|
| Speed               | Faster training and inference                  |
| Clean code          | Easier to debug and maintain                   |
| Scalability         | Handles large datasets and tensors efficiently |
| GPU compatibility   | Aligns with tensor operations in PyTorch/TF    |

---

## 🧰 Bonus: `np.vectorize()` for Custom Functions

```python
def square(x):
    return x ** 2

vec_square = np.vectorize(square)
result = vec_square(np.array([1, 2, 3]))  # [1, 4, 9]
```

> Note: `np.vectorize()` is syntactic sugar—it doesn’t offer performance gains like true vectorized operations.


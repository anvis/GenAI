
## 🧠 What Is `ndarray`?

- `ndarray` stands for **N-dimensional array**.
- It’s the core data structure in NumPy, used to represent scalars, vectors, matrices, and tensors.
- All AI data—images, embeddings, weights, activations—can be modeled as `ndarray`s.

---

## 📐 Dimensions and Their Meaning

| Structure   | Shape Example     | NumPy Representation           | AI Use Case                              |
|-------------|-------------------|--------------------------------|------------------------------------------|
| Scalar      | `()`              | `np.array(5)`                  | Single value (e.g., loss, bias)          |
| Vector      | `(n,)`            | `np.array([1, 2, 3])`          | Feature vector, embedding                |
| Matrix      | `(m, n)`          | `np.array([[1, 2], [3, 4]])`   | Weight matrix, image (grayscale)         |
| Tensor      | `(d1, d2, ..., dn)`| `np.array([...])`             | Batch of images, multi-head attention    |

---

- Vector: A 1D array representing magnitude and direction.
→ Used for embeddings, gradients, feature sets.
- Matrix: A 2D array (rows × columns).
→ Used for weights in neural networks, tabular data, transformations.
- Tensor: A generalization of vectors and matrices to higher dimensions.
→ Used for storing batches, image data, activations, and more.
✅ A vector is a 1D tensor, a matrix is a 2D tensor, and tensors are N-dimensional arrays that generalize both.

---

## 🧪 Examples

### 1️⃣ Vector (1D Tensor)
```python
import numpy as np
v = np.array([1, 2, 3])
print(v.shape)  # (3,)
```

### 2️⃣ Matrix (2D Tensor)
```python
m = np.array([[1, 2], [3, 4]])
print(m.shape)  # (2, 2)
```

### 3️⃣ Tensor (3D or higher)
```python
t = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(t.shape)  # (2, 2, 2)
```

---

## 🔍 Where They Fit in AI

| Concept   | AI Application Example                          |
|-----------|--------------------------------------------------|
| Vector    | Word embeddings, feature vectors                |
| Matrix    | Neural network weights, image pixels            |
| Tensor    | Batch of images `(batch_size, height, width, channels)` |
| Scalar    | Loss value, learning rate                       |

---


Here’s a concise guide to essential NumPy array creation operations, with examples and their AI relevance:

---

## 🧠 1. `np.array()`: Create from Python list

```python
import numpy as np
a = np.array([1, 2, 3])
print(a)        # [1 2 3]
print(a.shape)  # (3,)

# Initializing the array
arr1 = np.arange(4, dtype = np.float_).reshape(2, 2)

print('\nSecond array:') 
arr2 = np.array([12, 12]) 
print(arr2)

print('First array:') 
print(arr1)

First array:
[[ 0.  1.]
 [ 2.  3.]]

Second array:
[12 12]


```

🔹 **Use case**: Convert raw data or features into NumPy format.

---

## ⚪ 2. `np.zeros()`: Create array of zeros

```python
z = np.zeros((2, 3))
print(z)
# [[0. 0. 0.]
#  [0. 0. 0.]]
```

🔹 **Use case**: Initialize weights, masks, or padding arrays.

---

## ⚪ 3. `np.ones()`: Create array of ones

```python
o = np.ones((3, 2))
print(o)
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
```

🔹 **Use case**: Bias initialization, dummy inputs.

---

## 🔢 4. `np.arange()`: Range with step

```python
r = np.arange(0, 10, 2)
print(r)  # [0 2 4 6 8]
```

🔹 **Use case**: Index generation, time steps, synthetic data.

---

## 📏 5. `np.linspace()`: Evenly spaced values

```python
l = np.linspace(0, 1, 5)
print(l)  # [0.   0.25 0.5  0.75 1.  ]
```

🔹 **Use case**: Sampling, interpolation, plotting axes.

---



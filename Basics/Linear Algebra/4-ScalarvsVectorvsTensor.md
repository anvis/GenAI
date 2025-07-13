

Vector: A 1D array representing magnitude and direction. → Used for embeddings, gradients, feature sets.
Matrix: A 2D array (rows × columns). → Used for weights in neural networks, tabular data, transformations.
Tensor: A generalization of vectors and matrices to higher dimensions. → Used for storing batches, image data, activations, and more. ✅ A vector is a 1D tensor, a matrix is a 2D tensor, and tensors are N-dimensional arrays that generalize both.
🧪 Examples
1️⃣ Vector (1D Tensor)
import numpy as np
v = np.array([1, 2, 3])
print(v.shape)  # (3,)
2️⃣ Matrix (2D Tensor)
m = np.array([[1, 2], [3, 4]])
print(m.shape)  # (2, 2)
3️⃣ Tensor (3D or higher)
t = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(t.shape)  # (2, 2, 2)




<img width="977" height="827" alt="image" src="https://github.com/user-attachments/assets/100ede94-8e41-415a-885c-11cafbb11246" />

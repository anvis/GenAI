
import numpy as np

# Dot product of scalars
result = np.dot(5, 4)
print("Dot Product of scalars:", result) # Output: 20

# Dot product of 1D arrays
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
result = np.dot(vector_a, vector_b)
## (1*4 + 2*5 + 3*6 = 32)
print("Dot Product of vectors:", result) # Output: 32

# Dot product of 2D arrays (matrix multiplication)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
result = np.dot(matrix_a, matrix_b)
print("Dot Product of matrices:\n", result)
# Output:
# [[19 22]
# [43 50]]

## First row of matrix_a × Columns of matrix_b
#- [1, 2] · [5, 7] → 1×5 + 2×7 = 5 + 14 = 19
#- [1, 2] · [6, 8] → 1×6 + 2×8 = 6 + 16 = 22

# Second row of matrix_a × Columns of matrix_b
#- [3, 4] · [5, 7] → 3×5 + 4×7 = 15 + 28 = 43
# - [3, 4] · [6, 8] → 3×6 + 4×8 = 18 + 32 = 50
















A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)

print(result)

multiply = A * B
print(multiply)


Singular Value Decomposition (SVD), one of the most powerful matrix decomposition techniques. 
SVD is widely used in machine learning, data science, and other computational fields for applications such as dimensionality reduction, noise reduction, and matrix approximation.

Unlike Eigen Decomposition, which works only for square matrices, SVD can be applied to any matrix, making it a versatile tool.

Singular Value Decomposition is a matrix factorization method that breaks a matrix A into three components:

![image](https://github.com/user-attachments/assets/5bed7fe5-50d0-40e2-9ccc-0712de216b76)

Where:
- U is an orthogonal matrix (m x m)
- Σ is a diagonal matrix containing the singular values (m x n)
- V^T is the transpose of another orthogonal matrix V (n x n)

The singular values in Σ reveal important properties about the matrix, such as its rank, and allow us to perform matrix approximations, noise filtering, and other data manipulation tasks.

Properties of SVD:

- Orthogonal Matrices: Both U and V are orthogonal matrices, meaning their columns are mutually perpendicular.
- Singular Values: The diagonal entries of Σ are the singular values of the matrix A, which are always non-negative.
- Applications: SVD is commonly used in machine learning for dimensionality reduction (PCA), data compression, and collaborative filtering.

  


https://medium.com/@ebimsv/mastering-linear-algebra-part-8-singular-value-decomposition-svd-3dbc34c91908

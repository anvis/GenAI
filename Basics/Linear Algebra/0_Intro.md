
# Linear Algebra

## Table of Contents
- [Linear Algebra](#Linear-Algebra)
- [Connection between Linear Albegra and Machine Learning](#Connection-between-Linear-Albegra-and-Machine-Learning)
- [Vector and Matrix](#Vector-and-Matrix)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Linear Algebra

Linear algebra is the branch of mathematics that deals with vectors, matrices, and linear transformations.

At the heart of many machine learning models are linear equations and transformations. Whether we are working with simple linear regression or more complex deep learning models, linear algebra provides the framework to represent and solve these equations systematically. Understanding the principles of linear algebra enables data scientists and engineers to grasp how algorithms work, leading to better implementation and optimization.

## Connection between Linear Albegra and Machine Learning

In image recognition, each pixel of an image can be represented as a vector, and the entire image as a matrix. Operations such as rotation, scaling, and translation of images are essentially linear transformations. 
- Use Case: Facial recognition, object detection, medical imaging, and augmented reality.

In natural language processing (NLP), linear algebra plays a crucial role in word embedding, where words or phrases from a vocabulary are mapped to vectors of real numbers.
Words and sentences are represented as vectors (word embeddings like Word2Vec, GloVe, and transformers). Matrix operations enable efficient similarity computations and transformations.
- Use Case: Chatbots, language translation, sentiment analysis, and speech recognition.

In Recommendation systems, User-item interactions are stored in a matrix, where factorization methods (like **Singular Value Decomposition**, SVD) extract patterns for better recommendations.
- Use Case: Netflix movie recommendations, e-commerce product suggestions, personalized advertising

In Neural Networks & Deep Learning, Inputs, weights, and activations in neural networks are represented as matrices. The forward pass computes activations using matrix multiplications, and **backpropagation** optimizes weights using gradients.
- Use Case: Autonomous vehicles, image classification, generative AI models (like GPT-based chatbots).

For Optimization & Machine Learning Algorithms, **Gradient descent**, a key optimization technique, involves computing gradients using matrix operations. **Principal Component Analysis (PCA)** reduces dimensionality by finding optimal linear projections.
- Use Case: Feature selection, anomaly detection, dimensionality reduction in big data.

For Graph-Based Learning (Social Networks, Fraud Detection), Graphs are represented as adjacency matrices, allowing node relationships to be analyzed with **eigenvalues** and vector transformations.
- Use Case: Fraud detection in transactions, influence analysis in social media networks, and recommender systems.

For Time Series Analysis (Finance, Weather Forecasting), Autoregressive models and recurrent neural networks (RNNs) use matrix operations to process sequences of data efficiently.
- Use Case: Stock market predictions, weather forecasting, predictive maintenance in industries.

## Vector and Matrix

**Matrix**

A matrix is a two-dimensional array that has a fixed number of rows and columns and contains a number at the intersection of each row and column.

A matrix is usually delimited by square brackets.

Example Here is an example of a matrix having two rows and two columns:

![image](https://github.com/user-attachments/assets/8c697930-6ce0-4539-a78c-900f746f75a3)

![image](https://github.com/user-attachments/assets/f69f90d2-5042-4792-9cd3-b4589dc55dad)

**Vectors**

If a matrix has only one row or only one column it is called a vector.

A matrix having only one row is called a row vector.

Example The 1*3 matrix is a row vector because it has only one row.

![image](https://github.com/user-attachments/assets/68903bda-ea9a-48bc-b7b4-8cc3e86dd9f6)


A matrix having only one column is called a column vector.

Example The 2*3 matrix is a column vector because it has only one column.

![image](https://github.com/user-attachments/assets/087ef258-0e08-4ea3-b55d-1faf8148e4c1)


**Scalars**

A matrix having only one row and one column is called a scalar.

Example The 1*1 matrix is a scalar. In other words, a scalar is a single number.

![image](https://github.com/user-attachments/assets/56c0b810-e2b0-4d86-b8bc-dd629bdb359e)



Source: https://medium.com/@ebimsv/mastering-linear-algebra-part-1-introduction-to-linear-algebra-in-machine-learning-fafcae1a5879


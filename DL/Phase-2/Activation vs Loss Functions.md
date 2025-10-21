
---

### ⚡ Activation Function: Adds Non-Linearity

- **Purpose**: Determines whether a neuron should "fire" based on its input.
- **Why it's needed**: Without activation functions, neural networks would just be linear models. Non-linearity lets them learn complex patterns.

#### 🔧 Common Types:
| Function | Formula | Behavior |
|----------|---------|----------|
| ReLU     | \( f(x) = \max(0, x) \) | Fast, sparse activation |
| Sigmoid  | \( f(x) = \frac{1}{1 + e^{-x}} \) | Smooth output between 0 and 1 |
| Tanh     | \( f(x) = \tanh(x) \) | Output between -1 and 1 |
| Softmax  | Converts scores to probabilities | Used in classification |

📌 Example: In image classification, ReLU helps extract features, while Softmax turns final scores into class probabilities.

---

### 🎯 Loss Function: Measures Error

- **Purpose**: Quantifies how far off the model’s predictions are from the actual values.
- **Why it's needed**: Guides the model during training to improve accuracy by minimizing this error.

#### 🔧 Common Types:
| Function | Use Case | Behavior |
|----------|----------|----------|
| Mean Squared Error (MSE) | Regression | Penalizes large errors |
| Cross-Entropy Loss | Classification | Penalizes wrong class predictions |
| Hinge Loss | SVMs | Focuses on margin violations |

📌 Example: In a binary classifier, cross-entropy loss increases when the predicted probability for the correct class is low.

---

### 🧠 How They Work Together

- **Forward pass**: Activation functions shape the output of each layer.
- **Backward pass**: Loss function computes error, and gradients flow back to update weights.


***Supervised Learning***

In Supervised Learning, we learn from existing data, we will have existing data from which we learn the relationship betwwen input and output.
when a new Input comes with the help of relationship we have we will able to predict the output.

Ultimately, we find the relationship between input and output, when new data comes we can map the function and prdeict the output.

Predict output based on some Input.

Examples Include:
- Email Spamming
- Weather Forecast
- Stock Price
- Sentiment Analysis

In supervised learning, we have labeled data—meaning we know the correct answers. The model learns by mapping inputs to known outputs.

Supervised algorithms require humans to provide both input and desired output.

---

**Linear Regression**: Used for predicting continuous values (e.g., stock prices, house prices).

**Logistic Regression**: Used for binary classification problems (e.g., spam detection, fraud detection).

**Decision Trees & Random Forests**: Used for classification and regression tasks (e.g., customer segmentation, recommendation systems).

**Support Vector Machines (SVM)**: Great for text classification or image recognition when data is well-separated.

**Neural Networks** (ANNs, CNNs, RNNs): Used for complex tasks like image recognition (CNNs) or language translation (RNNs).

---

Supervised Learning is divided into Regression and Clasification, where Regression refrs to some Numeric value and Classification refer to some Category.

The Output could be a number or a Category for Supervised Learning.

In Supervised Learning Category refer to specific pre-determined value. In Un-supervised Learning we group the values rather than predicting, there is no specific output.

---

The type of classification—**binary**, **multi-class**, or **multi-label**—depends on how many labels you're predicting and how they're structured. Here's a clear breakdown:

---

### 🟢 Binary Classification
**Definition**: Predicting one of two possible classes.

- **Example**: Is this email spam or not spam?
- **Labels**: Typically encoded as 0 and 1.
- **Model Output**: A single probability score (e.g., sigmoid activation).
- **Use Cases**:
  - Fraud detection
  - Disease diagnosis (positive/negative)
  - Sentiment analysis (positive/negative)

---

### 🔵 Multi-Class Classification
**Definition**: Predicting one label out of **three or more** mutually exclusive classes.

- **Example**: Classifying an image as either a cat, dog, or horse.
- **Labels**: One-hot encoded (e.g., [0, 1, 0] for "dog").
- **Model Output**: A probability distribution across all classes (e.g., softmax activation).
- **Use Cases**:
  - Handwritten digit recognition (0–9)
  - Language identification
  - Product category prediction

---

### 🟣 Multi-Label Classification
**Definition**: Predicting **multiple labels** for each instance, where labels are **not mutually exclusive**.

- **Example**: Tagging a news article as ["politics", "economy", "India"].
- **Labels**: Multi-hot encoded (e.g., [1, 0, 1] for "politics" and "India").
- **Model Output**: Multiple independent probability scores (e.g., sigmoid per label).
- **Use Cases**:
  - Movie genre classification (a movie can be both "comedy" and "romance")
  - Medical diagnosis (multiple conditions per patient)
  - Document tagging

---

### 🧠 Summary Table

| Type               | # Labels per Sample | Labels Exclusive? | Output Layer | Common Activation |
|--------------------|---------------------|--------------------|--------------|-------------------|
| Binary             | 1                   | Yes                | 1 neuron     | Sigmoid           |
| Multi-Class        | 1                   | Yes                | N neurons    | Softmax           |
| Multi-Label        | ≥1                  | No                 | N neurons    | Sigmoid           |




---

<img width="635" height="447" alt="image" src="https://github.com/user-attachments/assets/72456cf4-faff-4f91-a11d-cfcfc4829706" />

---

<img width="707" height="457" alt="image" src="https://github.com/user-attachments/assets/deda8746-67ae-45aa-8e18-7054c6b0b43f" />

---

<img width="717" height="451" alt="image" src="https://github.com/user-attachments/assets/59e81f0c-6f9c-4df0-bffa-d9405012cf4d" />





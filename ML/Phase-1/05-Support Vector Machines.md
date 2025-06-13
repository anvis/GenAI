
## Linear Regression
- [History & Problem it Solves](#History-&-Problem-it-Solves)
- [Prerequisites](#Prerequisites)
- [Working Mechanism](#Working-Mechanism)
- [What is SVM How Does It Work](#What-is-SVM-How-Does-It-Work)
- [How is it Used in Deep Learning AI GenAI](#How-is-it-Used-in-Deep-Learning-AI-GenAI)
- [Real World Example](#Real-World-Example)
- [Explain It to a 10Year Old](#Explain-It-to-a-10Year-Old)

## History & Problem it Solves

Before SVMs, classification models struggled with **complex decision boundaries**—meaning they couldn’t easily separate overlapping data points. Traditional algorithms, like Logistic Regression, worked well for simple cases but failed when data was **scattered or mixed**.

SVMs were introduced to solve this problem by **finding the best boundary (or hyperplane)** to separate different classes. They were designed to **maximize the gap** between categories for better accuracy.

## Prerequisites

Concept of vectors, distance calculation, optimization.

## Working Mechanism

1. It finds a **hyperplane** that best separates two categories.
2. If data isn’t cleanly separable, SVM introduces **kernel tricks** to transform data into higher dimensions, making separation possible.
3. It focuses on **support vectors**—the data points closest to the boundary, ensuring robust classification.

## What is SVM How Does It Work

SVM works by creating a **hyperplane**—a decision boundary that **maximizes separation** between different classes.

## How is it Used in Deep Learning AI GenAI

- **Text Classification:** Used for sentiment analysis (positive vs. negative reviews).
- **Image Recognition:** Helps detect objects in images.
- **Medical Diagnosis:** Predicts diseases based on complex patterns in patient data.

## Real World Example

Imagine a **tumor classification system**:
- **Input variables:** Tumor size, shape, texture, location.
- **Output variable:** **Benign or malignant.**

SVM finds the best boundary between cancerous and non-cancerous tumors based on historical patient data.

## Explain It to a 10Year Old

Imagine you're **drawing a line in the sand** 🏖️ to separate shells from stones. You want to **maximize the gap** so the division is clear. SVM does the same—it draws the best possible boundary between two groups, making sure the separation is strong.





## Principal Component Analysis (PCA)
- [History & Problem it Solves](#History-&-Problem-it-Solves)
- [Prerequisites](#Prerequisites)
- [Working Mechanism](#Working-Mechanism)
- [What is PCA How Does It Work](#What-is-PCA-How-Does-It-Work)
- [How is it Used in Deep Learning AI GenAI](#How-is-it-Used-in-Deep-Learning-AI-GenAI)
- [Real World Example](#Real-World-Example)
- [Explain It to a 10Year Old](#Explain-It-to-a-10Year-Old)

## History & Problem it Solves

Before machine learning, analyzing high-dimensional data was difficult. For example, researchers studying genetics had thousands of variables, making manual interpretation impossible.

The problem? **How do we simplify large datasets while preserving meaningful information?** PCA solves this by **reducing dimensions**, making data easier to analyze and visualize.

## Prerequisites

Understanding of vectors, eigenvalues, variance, and covariance.

## Working Mechanism

1. Identifies the most **important patterns** in data (called principal components).
2. Projects data onto these new components to reduce complexity.
3. Preserves as much meaningful information as possible.

This helps when dealing with **datasets with many features**.

## What is PCA How Does It Work

PCA is a **dimensionality reduction** technique that transforms high-dimensional data into fewer important variables.

## How is it Used in Deep Learning AI GenAI

- **Image Compression:** Reduces image size while maintaining clarity.
- **Feature Engineering:** Helps eliminate irrelevant features in ML models.
- **Finance & Stock Market Analysis:** Finds the most influential indicators affecting stock prices.

## Real World Example

Imagine a **face recognition system**:
- **Input variables:** Hundreds of pixel values in a high-resolution image.
- **Output variable:** Simplified version of the face for easier classification.

PCA **reduces the number of pixels** while keeping the unique features necessary for identification.

## Explain It to a 10Year Old

Imagine you have **100 crayons** 🖍️, but you can only take **5**. Instead of randomly picking them, you **find the colors used most often** in your drawings.

That’s PCA—it **keeps the most important information** while removing the extra details.





## Linear Regression
- [History & Problem it Solves](#History-&-Problem-it-Solves)
- [Prerequisites](#Prerequisites)
- [Working Mechanism](#Working-Mechanism)
- [What is Random Forests How Does It Work](#What-is-Random-Forests-How-Does-It-Work)
- [How is it Used in Deep Learning AI GenAI](#How-is-it-Used-in-Deep-Learning-AI-GenAI)
- [Real World Example](#Real-World-Example)
- [Explain It to a 10Year Old](#Explain-It-to-a-10Year-Old)

## History & Problem it Solves

Decision Trees are powerful, but they can sometimes **overfit**, meaning they get too specific and don’t generalize well. Before Random Forests, ML models often relied on just **one tree**, which could lead to biased decisions.

Random Forests solve this issue by using **multiple Decision Trees** and averaging their results. This technique makes predictions more **robust and accurate**.

## Prerequisites

Understanding Decision Trees, averaging predictions.

## Working Mechanism

1. **Multiple Decision Trees** are trained on random subsets of data.
2. Each tree gives a prediction.
3. The final result is based on a **majority vote** (classification) or **average prediction** (regression).

This approach **reduces bias** and **handles missing data better** than single Decision Trees.

## What is Random Forests How Does It Work

Random Forest is an **ensemble learning** algorithm—it combines multiple Decision Trees to improve accuracy.

## How is it Used in Deep Learning AI GenAI

- **Fraud Detection:** Banks use Random Forests to detect fraudulent transactions.
- **Medical Diagnosis:** Used for predicting diseases based on multiple symptoms.
- **Text Classification:** Helps categorize documents more accurately than single trees.

## Real World Example

Imagine a **credit card fraud detection system**:
- **Input variables:** Unusual spending patterns, transaction location, amount.
- **Output variable:** Fraud or not fraud.

Instead of relying on **one rule**, Random Forest looks at multiple indicators from various trees and **averages results** to make a better decision.

## Explain It to a 10Year Old

Imagine you're **choosing the best ice cream flavor** 🍦. You ask **10 friends** what they like:
1. Some say chocolate.
2. Some say vanilla.
3. Others say mango.

Instead of relying on **one person’s choice**, you go with the **flavor most people picked**—that’s how Random Forest works!




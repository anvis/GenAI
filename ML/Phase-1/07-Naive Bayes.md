
## Linear Regression
- [History & Problem it Solves](#History-&-Problem-it-Solves)
- [Prerequisites](#Prerequisites)
- [Working Mechanism](#Working-Mechanism)
- [What is Naive Bayes How Does It Work](#What-is-Naive-Bayes-How-Does-It-Work)
- [How is it Used in Deep Learning AI GenAI](#How-is-it-Used-in-Deep-Learning-AI-GenAI)
- [Real World Example](#Real-World-Example)
- [Explain It to a 10Year Old](#Explain-It-to-a-10Year-Old)

## History & Problem it Solves

Before Naïve Bayes, categorizing information relied on manual labeling and complex statistical techniques. For instance, early spam detection systems relied on simple keyword matching rather than learning from patterns.

The challenge? How do we efficiently classify data using probabilities? **Naïve Bayes simplifies classification by assuming features are independent and using Bayes’ theorem to make predictions**.

## Prerequisites

Basic probability, Bayes’ theorem.

## Working Mechanism

1. It calculates the probability of a class given the input features.
2. Uses Bayes' theorem:  
     \[
     P(A|B) = \frac{P(B|A) P(A)}{P(B)}
     \]
3. Assumes that all features are **independent** (this is the "naïve" part).

   Despite this assumption being unrealistic, Naïve Bayes works remarkably well for many tasks.

## What is Naive Bayes How Does It Work

Naïve Bayes is a **probabilistic classifier** that predicts categories based on conditional probabilities.

a probability-based algorithm that excels in classification tasks.


## How is it Used in Deep Learning AI GenAI

- **Text Classification:** Used for spam filtering and sentiment analysis.
- **Medical Diagnosis:** Helps classify diseases based on symptoms.
- **Fraud Detection:** Identifies fraudulent transactions based on risk probabilities..

## Real World Example

Imagine a **spam detection system**:
- **Input variables:** Presence of words like "FREE", "WIN", "LIMITED TIME".
- **Output variable:** Spam or not spam.

Naïve Bayes **assigns probabilities** based on past spam/non-spam emails and classifies new emails accordingly.

## Explain It to a 10Year Old

Imagine you love **chocolate and strawberries** 🍫🍓. You see a new dessert with both ingredients. Since you like **both separately**, you assume you’ll love them together. 

That’s how Naïve Bayes works—it **predicts an outcome based on separate features**, even if they aren’t strongly connected.



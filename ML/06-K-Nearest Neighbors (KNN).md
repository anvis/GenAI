
## Linear Regression
- [History & Problem it Solves](#History-&-Problem-it-Solves)
- [Prerequisites](#Prerequisites)
- [Working Mechanism](#Working-Mechanism)
- [What is KNN How Does It Work](#What-is-KNN-How-Does-It-Work)
- [How is it Used in Deep Learning AI GenAI](#How-is-it-Used-in-Deep-Learning-AI-GenAI)
- [Real World Example](#Real-World-Example)
- [Explain It to a 10Year Old](#Explain-It-to-a-10Year-Old)

## History & Problem it Solves

Before machine learning, classifying things was largely manual. Suppose a doctor wanted to diagnose a patient—they would compare symptoms with past cases to make a judgment.

The problem? These comparisons relied on **intuition** rather than **mathematical certainty**. KNN solves this by looking at similar past examples and predicting new cases based on them.

## Prerequisites

Understanding distance metrics like Euclidean distance.

## Working Mechanism

1. When a new data point arrives, KNN looks at the **K closest past examples**.
2. It checks which category is most common among those neighbors.
3. The new data is assigned to the most frequent class.

Think of it like **asking your closest friends for advice**—their opinions influence your decision!

## What is KNN How Does It Work

KNN is a **lazy learning** algorithm—it doesn’t create a complex mathematical model but simply **stores past data** and classifies new cases by finding the **closest neighbors**.

## How is it Used in Deep Learning AI GenAI

- **Recommendation Systems:** Used in Netflix or Spotify suggestions.
- **Image Recognition:** Helps identify objects in images.
- **Fraud Detection:** Banks use KNN to detect suspicious transactions.

## Real World Example

Imagine a **music recommendation system**:
- **Input variables:** Listener history, genre preference, mood.
- **Output variable:** Recommended song.

KNN finds users with similar taste and suggests songs based on their preferences.

## Explain It to a 10Year Old

Imagine you're **choosing a football team** ⚽. You ask your **5 closest friends**:
1. **3 say Barcelona** → Most votes!
2. **2 say Manchester United**.

Since **Barcelona has more votes**, you pick them—that’s KNN in action!




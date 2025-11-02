**Precision vs Recall**

For Loan Eligibility 
If your goal is minimizing risk, you might want higher precision. If it’s maximizing access, go for higher recall.

High Precision actually give access to most of eligibile customers, but may loose out on some.
High Recall actually give access to most of the customers and might give access to in eligibile customers aswell.

---

**Precision**: Precision measures the proportion of predicted positives that are actually correct.

**Recall**: Recall measures the proportion of actual positives that were correctly identified.

**Tradeoff**

High Precision, Low Recall: You’re very sure when you say something is spam, but you miss a lot of actual spam.

High Recall, Low Precision: You catch most spam, but also flag many legitimate emails incorrectly.

Precision: Of all people diagnosed with a disease, how many actually have it?

Recall: Of all people who truly have the disease, how many did the test catch?

---

| Concept | Precision | Recall |
|--------|-----------|--------|
| Definition | True Positives / Predicted Positives | True Positives / Actual Positives |
| Focus | How accurate are positive predictions | How many actual positives were captured |
| Tradeoff | High precision may miss positives | High recall may include false alarms |

---

Example: Suppose your spam filter flags 100 emails as spam.

80 are actually spam (True Positives)
20 are not spam (False Positives) → Precision = \frac{80}{80 + 20} = 0.8 or 80%

Suppose there are 120 spam emails in total.

Your filter correctly caught 80 (True Positives)
Missed 40 (False Negatives) → Recall = \frac{80}{80 + 40} = 0.67 or 67%

---

How to Decide Which Matters More

| Scenario | Prioritize | Why |
|---------|------------|-----|
| **Spam detection** | Precision | You don’t want to wrongly flag important emails as spam. |
| **Disease screening** | Recall | You want to catch as many true cases as possible, even if some false alarms happen. |
| **Loan approval agent** | Depends | High precision avoids false approvals; high recall ensures eligible users aren’t missed. |

---

Choosing a Balance: F1 Score

If you want a **balanced view**, use the **F1 Score**, which combines precision and recall:

It’s especially useful when classes are imbalanced (e.g., fraud detection).

---



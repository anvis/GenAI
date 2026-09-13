# ML Algorithms — Interview-Ready Guide

A quick-reference for *what each algorithm is, when to use it, and how to compare it against the others without getting tangled up.*

---

## 1. Linear Regression

**What it is:** Predicts a continuous number by fitting a straight line (or hyperplane): `y = w1x1 + w2x2 + ... + b`. Trained by minimizing Mean Squared Error, usually via gradient descent or the closed-form Normal Equation.

**Use when:**
- Target variable is continuous (price, salary, temperature)
- Relationship between features and target is roughly linear
- You need an interpretable model (coefficients = feature impact)

**Assumptions (interviewers love this):** linearity, independence of errors, homoscedasticity (constant variance of errors), no multicollinearity, normally distributed residuals.

**Watch out for:** outliers (they pull the line hard), multicollinearity (inflates coefficient variance — check with VIF).

**One-liner for interviews:** "Regression problem, linear relationship, need interpretability → Linear Regression."

---

## 2. Logistic Regression

**What it is:** Despite the name, it's a **classification** algorithm. It applies a sigmoid function to a linear combination of inputs to output a probability between 0 and 1, then thresholds it (typically at 0.5) into a class.

**Use when:**
- Binary (or multi-class via one-vs-rest/softmax) classification
- You want probability estimates, not just labels
- You need a fast, interpretable baseline

**Key trick question:** *"Why is it called regression if it's used for classification?"* → Because it models the log-odds (logit) as a linear regression, then maps that through sigmoid to get a probability.

**Watch out for:** assumes a linear decision boundary in log-odds space; struggles with complex non-linear boundaries unless you add polynomial/interaction features.

**vs. Linear Regression:** Linear predicts a continuous value directly; Logistic predicts a probability via sigmoid, used for classification.

---

## 3. Decision Tree

**What it is:** A flowchart-like structure that splits data recursively based on feature values (e.g., "is age > 30?") to arrive at a prediction. Splits are chosen to maximize purity — measured via **Gini impurity** or **Entropy/Information Gain**.

**Use when:**
- You need a highly interpretable, visualizable model ("white box")
- Data has non-linear relationships or feature interactions
- Mixed data types (categorical + numerical) without much preprocessing

**Watch out for:** **overfitting** — a fully grown tree memorizes training data. Controlled via max_depth, min_samples_split, pruning.

**Key trick question:** *"Gini vs Entropy?"* → Both measure impurity; Gini is computationally cheaper (no log), Entropy is more sensitive to changes in class probability. In practice, they usually produce similar trees.

---

## 4. Random Forest

**What it is:** An **ensemble** of many decision trees, each trained on a random bootstrap sample of the data and a random subset of features per split (this randomness is the whole point). Final prediction = majority vote (classification) or average (regression). This is **bagging** (Bootstrap Aggregating).

**Use when:**
- You want strong accuracy without much tuning
- You want to reduce overfitting compared to a single tree
- You need feature importance estimates but not full interpretability

**vs. Decision Tree:** A single tree is interpretable but overfits; Random Forest trades some interpretability for much better generalization by averaging many trees.

**Key trick question:** *"Why does randomness help?"* → It decorrelates the trees — if trees are less correlated, averaging their errors cancels out more noise (bias stays similar, variance drops significantly).

---

## 5. Support Vector Machines (SVM)

**What it is:** Finds the hyperplane that maximizes the **margin** between classes (the widest possible "street" separating them). Only the closest points — the **support vectors** — determine this boundary. For non-linear data, the **kernel trick** (RBF, polynomial) implicitly projects data into higher dimensions where it becomes linearly separable, without ever computing that transformation explicitly.

**Use when:**
- High-dimensional data (e.g., text classification, gene data) where dimensions > samples
- Clear margin of separation exists
- Medium-sized datasets (SVMs scale poorly to very large datasets)

**Watch out for:** slow training on large datasets; sensitive to feature scaling (always standardize first); choosing the right kernel and C/gamma parameters requires tuning.

**Key trick question:** *"What does the C parameter control?"* → Trade-off between maximizing margin width and minimizing misclassification. Low C = wider margin, more tolerance for errors (more regularization); high C = narrower margin, fits training data more tightly (risk of overfitting).

---

## 6. K-Nearest Neighbors (KNN)

**What it is:** A **lazy, instance-based** algorithm — there's no real "training" step. To classify a new point, it looks at the K closest points in the training data (by distance, usually Euclidean) and takes a majority vote (or average, for regression).

**Use when:**
- Simple baseline for small-to-medium datasets
- Decision boundary is irregular / non-linear
- You have low-dimensional, well-scaled data

**Watch out for:**
- **Curse of dimensionality** — distance becomes meaningless in high dimensions
- Feature scaling is critical (unscaled features dominate the distance calc)
- Slow at prediction time on large datasets (must compute distance to every point)
- Choosing K: small K = noisy/overfit, large K = smooth/underfit

**Key trick question:** *"Is KNN parametric or non-parametric?"* → Non-parametric — it makes no assumption about the underlying data distribution, and model complexity grows with data size.

---

## 7. Naive Bayes

**What it is:** A probabilistic classifier based on **Bayes' Theorem**, with the "naive" assumption that all features are **conditionally independent** given the class. Computes `P(class | features)` proportional to `P(features | class) × P(class)`.

**Use when:**
- Text classification (spam detection, sentiment analysis) — its classic use case
- You need a fast, simple baseline
- High-dimensional data with limited training samples

**Why it still works despite the "naive" (usually false) independence assumption:** it often only needs to get the *ranking* of class probabilities right, not their exact values, and errors from the independence assumption tend to cancel out in practice.

**Variants:** Gaussian NB (continuous features), Multinomial NB (word counts — most common for text), Bernoulli NB (binary features).

---

## 8. K-Means Clustering

**What it is:** An **unsupervised** algorithm — no labels required. Groups data into K clusters by iteratively: (1) assigning each point to its nearest centroid, (2) recomputing centroids as the mean of assigned points, until convergence.

**Use when:**
- You need to discover groups/segments in unlabeled data (customer segmentation, image compression)
- Clusters are expected to be roughly spherical and similar in size
- You know (or can estimate) K in advance

**Watch out for:**
- Must choose K upfront — use the **Elbow Method** or **Silhouette Score** to pick it
- Sensitive to initial centroid placement (K-Means++ helps)
- Sensitive to feature scaling
- Struggles with non-spherical clusters or very different cluster densities (DBSCAN handles those better)

**Key trick question:** *"Is K-Means guaranteed to find the global optimum?"* → No — it converges to a local minimum depending on initialization, which is why it's typically run multiple times with different seeds.

---

## 9. PCA (Principal Component Analysis)

**What it is:** An **unsupervised dimensionality reduction** technique (not a predictive model). It finds new axes (principal components) — linear combinations of original features — that capture the maximum variance in the data, ordered by how much variance each explains.

**Use when:**
- Too many features (curse of dimensionality) and you want to reduce them while keeping most information
- Visualizing high-dimensional data in 2D/3D
- Removing multicollinearity before feeding into another model
- Speeding up training / reducing noise

**Watch out for:** it's a linear technique (won't capture non-linear structure — see t-SNE/UMAP for that); components are linear combinations of original features, so **interpretability is lost**; always standardize data first (PCA is sensitive to scale/variance).

**Key trick question:** *"Is PCA supervised or unsupervised, and is it a classifier?"* → Unsupervised, and it's *not* a classifier at all — it's a preprocessing/feature-engineering step, often confused with LDA (which IS supervised and does use class labels).

---

## Quick Decision Framework

| Question | Answer points to... |
|---|---|
| Predicting a number? | Linear Regression, Random Forest (regressor), SVM (regressor) |
| Predicting a category, need probability + interpretability? | Logistic Regression, Naive Bayes |
| Need max accuracy, don't care about interpretability? | Random Forest, SVM (with tuning) |
| Need a fully interpretable, "explain-to-a-manager" model? | Decision Tree, Linear/Logistic Regression |
| High-dimensional text/sparse data? | Naive Bayes, SVM |
| No labels at all — want to find groups? | K-Means |
| No labels, want to reduce feature count? | PCA |
| Small dataset, simple non-linear boundary, no real training desired? | KNN |
| Data has complex feature interactions, mixed types? | Decision Tree, Random Forest |

## Supervised vs. Unsupervised — don't mix these up in an interview

- **Supervised (need labels):** Linear Regression, Logistic Regression, Decision Tree, Random Forest, SVM, KNN, Naive Bayes
- **Unsupervised (no labels):** K-Means, PCA

## Bias-Variance Cheat Sheet

- **High bias (underfit) risk:** Linear/Logistic Regression on non-linear data, shallow Decision Trees, high-K KNN
- **High variance (overfit) risk:** Deep unpruned Decision Trees, low-K KNN, SVM with high C/complex kernel
- **Naturally balances bias/variance well:** Random Forest (via averaging/bagging)

---

## The #1 interview trap across this whole list

Interviewers love asking **"why not just use X"** for any two similar algorithms. The fastest way to sound confident: always answer in terms of **(1) interpretability, (2) data size/dimensionality, (3) linear vs non-linear boundary, (4) supervised vs unsupervised.** Almost every "why this over that" question collapses into one of these four axes.

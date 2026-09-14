
**NumPy — Numerical Computing Foundation**

NumPy's core job is fast, memory-efficient numerical operations on arrays and matrices. 
Python's built-in lists are slow for math-heavy work; 
NumPy solves this with its ndarray object and vectorized operations (written in C under the hood).

Primary use cases:

- Array/matrix operations (linear algebra, reshaping, broadcasting)
- Mathematical functions (statistics, trigonometry, random number generation)
- Foundation layer — pandas, scikit-learn, TensorFlow, PyTorch are all built on top of NumPy arrays

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())        # 3.0
print(arr * 2)            # [2, 4, 6, 8, 10] — vectorized, no loop needed

```

Think of it as: "How do I work with numbers/arrays fast?"

---

**pandas — Data Manipulation & Analysis**

pandas is built for working with structured/tabular data — think Excel-like rows and columns, but programmable. 
Its core objects are Series (1D) and DataFrame (2D table).

Primary use cases:

- Loading data (CSV, Excel, SQL, JSON) into a table-like structure
- Cleaning data (handling missing values, filtering, deduplication)
- Transforming data (grouping, merging, pivoting, aggregating)
- Exploratory data analysis before feeding data into a model

```

import pandas as pd

df = pd.read_csv("employees.csv")
print(df.groupby("department")["salary"].mean())
df = df.dropna()  # remove missing values

```

Think of it as: "How do I load, clean, and explore my data?"

---

**scikit-learn — Machine Learning**

scikit-learn provides ready-made implementations of classic machine learning algorithms — classification, regression, clustering — plus tools for the full ML workflow (splitting data, scaling features, evaluating models).

Primary use cases:

- Training models (Linear Regression, Random Forest, SVM, K-Means, etc.)
- Preprocessing (scaling, encoding categorical variables)
- Model evaluation (accuracy, precision/recall, cross-validation)
- Building ML pipelines

```
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
```

Think of it as: "How do I build and evaluate a predictive model?"

In short: NumPy handles the numbers, pandas handles the data table, scikit-learn handles the modeling — a typical ML workflow moves data through all three in that order.







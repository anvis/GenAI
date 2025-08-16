
Probability Mass Function applies to Discrete Variables, Gives the probability that a discrete random variable is exactly equal to some value.

Probability Density Function applies to Continous Variables, Describes the relative likelihood for a continuous random variable to take on a given value.

PMF (Probability Mass Function)

- Used when dealing with discrete outcomes (e.g., number of heads in coin tosses).
- The sum of all probabilities in a PMF is 1.

PDF (Probability Density Function)

- Used for continuous variables (e.g., height, temperature).
- The probability of a specific value is zero; instead, we calculate probability over an interval.
- The area under the curve of the PDF over an interval gives the probability.

Use in Machine Learning

✅ 1. Modeling Uncertainty

- PMFs and PDFs help model the uncertainty in predictions.
- Used in Bayesian models, Hidden Markov Models, and Naive Bayes classifiers.
  
✅ 2. Sampling & Data Generation

- PDFs are used in generative models like GANs and VAEs to sample realistic data points.
  
✅ 3. Anomaly Detection

- Points with low PDF values are considered anomalies in Gaussian-based models.
  
✅ 4. Loss Functions
- In probabilistic models, loss functions often involve log-likelihoods derived from PMFs or PDFs.
  
✅ 5. Density Estimation
- Techniques like Kernel Density Estimation (KDE) use PDFs to estimate the underlying distribution of data.


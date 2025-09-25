**covariance vs correlation**, using the key insights from the referenced [YouTube video](https://www.youtube.com/shorts/PzOijddw4eg):

---

### 🧮 Covariance: Direction of Relationship
- **Definition**: Covariance measures how two variables change together.
- **Interpretation**:
  - **Positive covariance** → both variables increase together.
  - **Negative covariance** → one increases while the other decreases.
- **Example from video**:
  - If height and weight tend to increase together, their covariance is positive.
  - If study time increases but stress decreases, their covariance is negative.

> Covariance tells you *whether* two variables move together, but not *how strongly*.

---

### 📊 Correlation: Strength + Direction
- **Definition**: Correlation standardizes covariance to a scale from -1 to +1.
- **Interpretation**:
  - **+1** → perfect positive relationship.
  - **-1** → perfect negative relationship.
  - **0** → no linear relationship.
- **Example from video**:
  - If two stocks move in sync, correlation might be close to +1.
  - If one stock rises while another consistently falls, correlation could be near -1.

> Correlation is **unitless** and easier to compare across datasets.

---

### 🔍 Key Differences

| Feature         | Covariance                     | Correlation                          |
|----------------|--------------------------------|--------------------------------------|
| Measures        | Direction of relationship      | Direction **and** strength           |
| Range           | Unbounded                      | Between -1 and +1                    |
| Units           | Depends on variables' units    | Unitless                             |
| Comparability   | Hard to compare across datasets| Easy to compare                      |

---

Would you like to see Python code to compute both, or examples from finance or household data?

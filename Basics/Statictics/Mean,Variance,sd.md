
- Mean (μ): The average of all data points.
- Variance (σ²): Measures how far each data point is from the mean.
- Standard Deviation (σ): The square root of the variance; it shows the spread of data.

---

## Example

data = [4, 8, 6, 5, 3]

**Mean**

= {4 + 8 + 6 + 5 + 3}/{5} ==> 26/5 ==> 5.2

**Variance**

To Calculate Variance, first get Deviation from Mean, Square each deviation, and calulate variance

Deviations: (4 - 5.2), (8 - 5.2), (6 - 5.2), (5 - 5.2), (3 - 5.2) 
            = -1.2, 2.8, 0.8, -0.2, -2.2

Square Deviations: 1.44, 7.84, 0.64, 0.04, 4.84

Calculate the Variance:
Sample Variance (s²) = (1.44 + 7.84 + 0.64 + 0.04 + 4.84) / (5) = 2.96

**Standard Deviation**

Sqrt(Variance) ==> Sqrt(2.96) ==> 1.96

---

Python Code

``` python

import numpy as np

data = [4, 8, 6, 5, 3]

mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

```




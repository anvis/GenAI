
Measures of Central Tendency:- Mean, Mode and Median

Measures of Dispersion:- Variance, Standard Deviation, Range and Interquartile Range

Tables:- Frequent Table, contingency table

---

**Mean**:- 

Average value of all data points.

data = [4, 8, 6, 5, 3]

Mean

= {4 + 8 + 6 + 5 + 3}/{5} ==> 26/5 ==> 5.2

---

**Median**:- 

If data is arranged in ascending orderCenter, the value of the data middle value is considered as Median. If total number of values are odd then the middle value is median. If total number of values are even then median is the mean(or avaerage) of both middle values. 

Median doesnot effect with outliners, means if the last is very high or even you increase it doesnot effect value of median. As median is always stays at center. but if outlier is big or updated the mean value is changed accordingly. 

---

**Mode**:- 

Frequently repeated values are considered as Mode.

Uni-Mode:- 2,4,4,5,6,7 => Mode is 4

Bi-Modal:- 2,4,4,5,5,6,7 ==> Mode is 4 and 5

---

**Standard Deviation**:- 

on an average how much is the deviation of data points from mean.

**Variance**:-  

Variance also tells how much data is scatterd around mean, same as standard deviation. but while calculation we use square in Variance. Thus our units will differ when you do variance. 

It's adviced to use Standard Deviation instead of Variance.

Example:- 
We have 5 people with different heights, average of their heights is the mean, and each person have a different height few or tall and few are short of the mean. We dont need how each peron is deviated from mean. we calculate the average deviation of all persons. that is called standard deviation. This value will tell us how the data points are scatted around mean. Are they near to mean or far to mean.


To Calculate Variance, first get Deviation from Mean, Square each deviation, and calulate variance

Deviations: (4 - 5.2), (8 - 5.2), (6 - 5.2), (5 - 5.2), (3 - 5.2) 
            = -1.2, 2.8, 0.8, -0.2, -2.2

Square Deviations: 1.44, 7.84, 0.64, 0.04, 4.84

Calculate the Variance:
Sample Variance (s²) = (1.44 + 7.84 + 0.64 + 0.04 + 4.84) / (5) = 2.96

Standard Deviation

Sqrt(Variance) ==> Sqrt(2.96) ==> 1.96

---

**Range**:- 
 Difference between Minimum and Maximum value.

** Interquartile Range**:- 
            It will reperesent the Middle 50% of the data, it removes the first and last quater of the data. only picks from 25-75 and 75-100 and 0-25 were ignored. Insimple terms it picks Q2 and Q3.

---

**Frequency Table**:- 
            It lets us know how many times each distinct value is repeated.

<img width="683" height="477" alt="image" src="https://github.com/user-attachments/assets/1999bcec-d2a2-4fbf-8e6b-40e58e302085" />

**contingency table**:-
            It is frequency table with multiple columns.
            
<img width="865" height="365" alt="image" src="https://github.com/user-attachments/assets/d8592ca0-e554-4e00-b86d-9d2780bd1282" />


---




<img width="905" height="403" alt="image" src="https://github.com/user-attachments/assets/20e6923b-ff8e-4acd-98d9-da69b5a2d0de" />

<img width="902" height="478" alt="image" src="https://github.com/user-attachments/assets/e305da84-4998-4c0f-b6d8-a76619e8c709" />

<img width="966" height="497" alt="image" src="https://github.com/user-attachments/assets/bd20fabd-b34a-4f22-8e4a-d092db3bd695" />

<img width="1096" height="447" alt="image" src="https://github.com/user-attachments/assets/8d5b2b29-d83c-45f4-a139-21686405fa29" />

Variance

<img width="1092" height="636" alt="image" src="https://github.com/user-attachments/assets/81921650-3620-4f8d-bbc4-8b37f142a0f1" />

<img width="1142" height="640" alt="image" src="https://github.com/user-attachments/assets/871ad48e-3639-4bca-a50f-dfdb064bc158" />

<img width="908" height="518" alt="image" src="https://github.com/user-attachments/assets/0fe7b206-d610-4898-8fe5-54dfdfa7480f" />

---

- Mean (μ): The average of all data points.
- Variance (σ²): Measures how far each data point is from the mean.
- Standard Deviation (σ): The square root of the variance; it shows the spread of data.

---

## Example





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






# 3 Univariate Analysis


```python
import pandas as pd
import numpy as np
df = pd.read_csv('train.csv')
```

### Analyze the target variable SalePrice

Show the average, min, max SalePrice


```python
df['SalePrice'].describe()
```

We can inspect the distribution of SalePrice.


```python
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # to suppress a numpy warning
%matplotlib inline
```


```python
sns.distplot(df.SalePrice);
```


![png](output_6_0.png)


So we can observe that SalePrice:
- Deviates from the normal distribution
- Has a positive skewness (peak is left of center)
- Shows peakedness (kurtosis) (is more pointy than a normal distribution)


```python
# We can also show skewness and kurtosis in numbers
# A normal dist has skewness=0, skewness < 0 mean is right-skewed, skewness > 0 mean left-skewed
# A normal dist has kurtosis=3, kurtosis < 3 mean flat-topped and low-tailed, kurtosis > 3 mean peak and fat-tailed
print("Skewness: %f" % df.SalePrice.skew())
print("Kurtosis: %f" % df.SalePrice.kurt())
```

    Skewness: 1.882876
    Kurtosis: 6.536282


In general, you want to analyze whether continuous variables follow a Normal distribution and transform them if they are not (up next).

#### Assignment: Analyze the variable GrLivArea.


```python
df.GrLivArea.describe()
```




    count    1460.000000
    mean     1515.463699
    std       525.480383
    min       334.000000
    25%      1129.500000
    50%      1464.000000
    75%      1776.750000
    max      5642.000000
    Name: GrLivArea, dtype: float64




```python
import matplotlib.pyplot as plt

plt.hist(df.GrLivArea,bins = 35)
```




    (array([   3.,    9.,   27.,  133.,  151.,  164.,  174.,  174.,  175.,
             145.,   92.,   64.,   43.,   31.,   23.,   21.,   11.,    2.,
               5.,    4.,    3.,    2.,    0.,    0.,    0.,    0.,    1.,
               1.,    1.,    0.,    0.,    0.,    0.,    0.,    1.]),
     array([  334.        ,   485.65714286,   637.31428571,   788.97142857,
              940.62857143,  1092.28571429,  1243.94285714,  1395.6       ,
             1547.25714286,  1698.91428571,  1850.57142857,  2002.22857143,
             2153.88571429,  2305.54285714,  2457.2       ,  2608.85714286,
             2760.51428571,  2912.17142857,  3063.82857143,  3215.48571429,
             3367.14285714,  3518.8       ,  3670.45714286,  3822.11428571,
             3973.77142857,  4125.42857143,  4277.08571429,  4428.74285714,
             4580.4       ,  4732.05714286,  4883.71428571,  5035.37142857,
             5187.02857143,  5338.68571429,  5490.34285714,  5642.        ]),
     <a list of 35 Patch objects>)




![png](output_11_1.png)


Looks like the distribution resembles a normal one
- It is a bit left skewd
- It has a high peak


```python
print("Skewness: %f" % df.GrLivArea.skew())
print("Kurtosis: %f" % df.GrLivArea.kurt())
```

    Skewness: 1.366560
    Kurtosis: 4.895121




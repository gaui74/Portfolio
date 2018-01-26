
# 1. Checking data edges


```python
import pandas as pd
df = pd.read_csv('train.csv')
```

Pandas reads the file as a `Dataframe` object, which resembles a table in a database. The header (first line) provides the column labels, and every row in the file is inserted as a row in the Dataframe. We can view the first view lines with the `head()` method. You can also use `head(n)` to show the first `n` lines.

### the number of rows of a dataframe

If you know how many samples there should be (for instance from the source where you obtained the data) check it.

#### Assignment: Enter code to get the number of rows in the dataframe using the len() function, the correct answer should be 1460.


```python
len(df)
```




    1460



### columns in the dataframe

Similarly, if you known how many features there should be, check it. Also check for key features that you need for the problem you want to study. In this dataset, since the task is to predict the target variable SalePrice, we would require features that we expect to be most useful such as the size of the house.


```python
df.columns
```

### the number of columns in a dataframe


```python
len(df.columns)
```

### Inspecting the first and last rows

One of the reasons you want to inpect the first and last rows is to make sure all the data was read ok. Sometimes, files are split, meaning you end up with half a record, or someone inserted some commentary on the first or last lines.


```python
df.head() # first rows
```

#### Assignment: Enter the code to only inspect the first row, hint you can pass the number of rows to head()


```python
print(df.head(1))
```

       Id  MSSubClass MSZoning  LotFrontage  LotArea Street Alley LotShape  \
    0   1          60       RL         65.0     8450   Pave   NaN      Reg   
    
      LandContour Utilities    ...     PoolArea PoolQC Fence MiscFeature MiscVal  \
    0         Lvl    AllPub    ...            0    NaN   NaN         NaN       0   
    
      MoSold YrSold  SaleType  SaleCondition  SalePrice  
    0      2   2008        WD         Normal     208500  
    
    [1 rows x 81 columns]


We can view the datatypes and the number of non-null values, using the `info()` method. Null refers to 'no value' or 'unkown value'.


```python
df.tail() # last 5 rows
```

### subsetting rows


```python
# select the first two rows (the upper bound is always exclusive)
df[:2]
```


```python
# select the last 2 rows, negative numbers are an index that count back from the end of the dataframe
df[-2:]
```

#### Assignment: select rows 2 and 3 in one statement


```python
df[2:4]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 81 columns</p>
</div>



### Some additional inspections
### Subset rows by boolean indexing (logical statements)


```python
# creates a boolean index that indicates which rows have '04' in ExpMM.
df.MSZoning == 'RL'
```


```python
# create a subset dataframe of only rows that contain 'IR1' for the column LotShape
dfrl = df[df.LotShape == 'IR1']
dfrl.head(4)
```


```python
# create a subset dataframe of only rows that contain
# 'IR1' for the column LotShape AND '2008' for YrSold
dfrlreg = df[(df.LotShape == 'IR1') | (df.YrSold == 2008)]
dfrlreg.head(4)
```


```python
# create a subset dataframe of only rows that contain
# IR1' for the column LotShape OR '2008' for YrSold
dfrlreg = df[(df.LotShape == 'IR1') | (df.YrSold == 2008)]
dfrlreg.head(4)
```

#### Assignment: Show the sizes of the poolareas of the 7 houses that have a pool area (tip: PoolArea > 0)


```python
df.PoolArea[df.PoolArea >0]
```




    197     512
    810     648
    1170    576
    1182    555
    1298    480
    1386    519
    1423    738
    Name: PoolArea, dtype: int64



### Subsetting columns
More advanced subsetting can be done with df.ix. The first range selects the rows (: selects all). The second range selects columns, either by index number of label name. Somewhat confusing, the upperbounds are inclusive here.


```python
# More advanced subsetting can be done with df.ix. The first range selects the rows. 
df.ix[:5, 'LotArea':'LotShape']
```


```python
# alternatively, give a list of columns.
df[['1stFlrSF', '2ndFlrSF']]
```


# 2 Identifying variables


```python
import pandas as pd
df = pd.read_csv('train.csv')
```

### Showing the types and values


```python
df.info()
```

You can also check how many missing values there are in a column using **isnull()** and **sum()**


```python
df.Fence.isnull().sum()
```

## Describe the range of each feature


```python
df.LotFrontage.max()
```


```python
df.LotFrontage.min()
```


```python
df.LotFrontage.describe()
```

### Unique values of a column
For categorical features, you can inspect which values occur in a column, using `unique`


```python
df.MSZoning.unique()
```


```python
df.KitchenQual.unique()
```

We can also show the frequency of every value for a column.


```python
df.PavedDrive.value_counts()
```

### Convert values
Often, it is easier to process your data as numbers. For instance, the feature PavedDrive has a categorical label, bit of we want to use it in a regression algorithm we need to convert it to a number. In this case we convert it in the following way: N=0, P=1, Y=2 (assuming P means something like Partial).


```python
paved_drive = {'N':0, 'P':1, 'Y':2} # setup a dictionary to do the conversion

def convert_paved_drive(p):
    return paved_drive[p] # return the value of p in paved_drive dict

convert_paved_drive('P') # returns 1 because P is at position 1 in the array (indexing starts at 0)
```

We can use Python's **map()** function to apply a function to every element in a collection (or more formally, an iterable). Note that we could alternatively pass the dictionary paved_drive to the map() function, since map() also accepts dictionaries.


```python
df.PavedDrive = df.PavedDrive.map(convert_paved_drive)
```


```python
df.PavedDriveN[df.PavedDriveN < 2][:10]
```

#### Assignment:  convert KitchenQual to a number. In the description of the dataset it reads that the labels mean:

|Label|description|
|:---|---|
|Ex|Excellent|
|Gd|Good|
|TA|Typical/Average|
|Fa|Fair|
|Po|Poor|


```python
kitchenqual = {"Po":0,"Fa":1,"TA":2,"Gd":3,"Ex":4}

def con_kit_qual(element):
    return kitchenqual[element]
```


```python
df.KitchenQual = df.KitchenQual.map(con_kit_qual)
```

### Add features

We can add new features to the Dataframe by simply assigning a value to it. In this example we will compute the sum of the 1st floor space and 2nd floor space.


```python
# note you need to index these with [''] because in Python variable names cannot start with a number.
df['2FlrSF'] = df['1stFlrSF'] + df['2ndFlrSF']
df['2FlrSF'][:10]
```


```python
# alternatively, give a list of columns.
df[['1stFlrSF', '2ndFlrSF', '2FlrSF']]
```

### Code book

Write a code book. A book in which you list some collections specifics, such as the number of samples, and for every variable a description, datatype, numeric/categorical, #missing values, the value range, an example of a value. After the analysis, you can include the distribution over each variable, how the data was cleaned (missing values and outliers) and transformed. Include every operation done on the data to allow exact replication of these steps.

| variable | description | datatype | numeric/categorical | #missing | range | example value |
|--|--|--|--|--:|:-:|--|
| 1stFlrSF | First Floor square feet | int | Numeric | 0 | 334-4602 | 334 |
| 2FlrSF | Sum First Floor + Second Floor Square Feet | int | Numeric | 0 | 334-5642 | 5642 |
| PavedDriveN | State of driveway | int | numeric | 0 | 0-2 (gravel/dirt, partially paved, paved)| 2 |
| PavedDrive | State of driveway | text | Categorical | 0 | N, P, Y (gravel/dirt, partially paved, paved) | N |
| BsmtQual | Height of the basement | text | Categorical | 37 | Ex, Gd, TA, Fa, Po, NA (Excellent 100+", Good 90-99", Typical 80-89", Fair 70-79", Poor <70", No Basement | Ex |

#### Assignment: Add KitchenQual to the Code Book


```python
colommen = ["Variable", "Description","VoorDatatype","VoorNum/Cat","VoorRange","Changes made","NaDatatype","NaNum/Cat","NaRange"]
code_book = pd.DataFrame(index = range(1),columns = colommen)
code_book["Variable"] = "KitchenQual"
code_book["Description"]="Quality of Kitchen"
code_book["VoorDatatype"]="text"
code_book["VoorNum/Cat"]="Categorical"
code_book["VoorRange"] = "Po, Fa, TA, Gd, Ex (poor, fair, typical/avarage, good, excellent)"
code_book["Changes made"] = "Categorical value changed to numeric value"
code_book["NaDatatype"] = "integer"
code_book["NaNum/Cat"] = "Categorical"
code_book["NaRange"]= "0, 1, 2, 3, 4 (poor, fair, typical/avarage, good, excellent)"

print(code_book.head())
```

          Variable         Description VoorDatatype  VoorNum/Cat  \
    0  KitchenQual  Quality of Kitchen         text  Categorical   
    
                                               VoorRange  \
    0  Po, Fa, TA, Gd, Ex (poor, fair, typical/avarag...   
    
                                     Changes made NaDatatype    NaNum/Cat  \
    0  Categorical value changed to numeric value    integer  Categorical   
    
                                                 NaRange  
    0  0, 1, 2, 3, 4 (poor, fair, typical/avarage, go...  



```python

```

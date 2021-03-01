import pandas as pd
import numpy as np

df = pd.read_csv("data/melbourne.csv")
original_df_size = len(df)
print("\n Non null rows in each column :\n")
print(df.info())
print(df.isnull().sum())

print("\n Columns having atleat 1 missing value :\n")
print(df.isnull().any(axis=0))

print("\n Rows having atleat 1 missing value :\n")
print(df.isnull().any(axis=1))

print("\n Number of missing values on each row :\n")
print(df.isnull().sum(axis=1))

print("\n Percentage of missing values in columns:\n")
'''
Columns : BuildingArea, YearBuilt have more than 30% data missing
          CouncilArea has 33% of data missing
          we can drop them
'''
print(round(df.isnull().sum() / len(df)  * 100,2))
df.drop(columns=['BuildingArea', 'YearBuilt', 'CouncilArea'], axis=0, inplace=True)

print("\n Percentage of rows which have more than 5 columns missing out of 21:\n")
rows_with_missing_values = df[df.isnull().sum(axis=1) > 5]
print("Percentage of rows : {}".format(round(len(rows_with_missing_values) / len(df)  * 100,2)))

## Retain rows which have 5 or less missing data
df = df[df.isnull().sum(axis=1) <= 5]
print(round(df.isnull().sum() / len(df)  * 100,2))

'''
Now only the price column has has 21% dat missing
Remove NaN price rows
'''
df = df[-np.isnan(df['Price'])]

'''
Column Landsize has 10% missing data
On describe we see that it has huge variance, so missing values cannot be substituted
with mean, so we need to drop the rows which have null values 
'''
df = df[-np.isnan(df['Landsize'])]

'''
There are broadly 3 ways to treat missing values:

Doing nothing : some ML algorithms can handle this like decision trees
Delete: Delete the missing values
Impute: Imputing by a simple statistic: Replace the missing values by another value,
        commonly the mean, median, mode etc.
        
Impute rules :
    - Replace with mean if
        - standard deviation is less
        - median is close to mean
        - variation from 25th to 75th quartile is also less          

numerical columns involved
    - both mean and median offer up as a good imputed value

categorical column
    - mode turns out to be a decent enough imputation to carry out.

Predictive techniques: Use statistical models such as k-NN, SVM etc. to predict and impute missing values
In general, imputation makes assumptions about the missing values and replaces missing values
by arbitrary numbers such as mean, median etc. It should be used only when you are reasonably confident
about the assumptions. 

Otherwise, deletion is often safer and recommended. You may lose some data, but will
not make any unreasonable assumptions.
'''
print(round(df.isnull().sum() / len(df)  * 100,2))

'''
Columns to take care of : 
Lattitude        0.16
Longtitude       0.16
Car              0.46
Bathroom         0.01
'''

print(df[['Lattitude', 'Longtitude']].describe())
'''
    std deviation is small
    replace with mean
'''
df.loc[np.isnan(df['Lattitude']), ['Lattitude']] = df['Lattitude'].mean()
df.loc[np.isnan(df['Longtitude']), ['Longtitude']] = df['Longtitude'].mean()
print(round(df.isnull().sum() / len(df)  * 100,2))

'''
Bathroom and car
    - should we whole numbers
    - let' look at the frequency distribution
'''
print(df[['Bathroom', 'Car']].describe())

print(df[['Bathroom']].value_counts())
print(df[['Car']].value_counts())
'''
Most of the people have 1 bathroom and 2 cars
'''
df.loc[pd.isnull(df['Bathroom']), ['Bathroom']] = 1
df.loc[pd.isnull(df['Car']), ['Car']] = 2

print(round(df.isnull().sum() / len(df)  * 100,2))

print("Rows lost : {} %".format(round(len(df)/original_df_size  * 100, 2)))

'''
Do read :
 https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4
 https://www.theanalysisfactor.com/missing-data-mechanism/
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
import statsmodels.api as sm
import sklearn

name = ['Reetesh', 'Shruti', 'Kaustubh', 'Vikas', 'Mahima', 'Akshay']
response = ['No', 'Maybe', 'yes', 'Yes', 'maybe', 'Yes']
df = pd.DataFrame({'Name': name,'Response': response})

df['Response'] = df['Response'].str.lower()
# Write your code here
def binary_map(x):
    dict = {'yes': 1, "no": 0, "maybe":0.5}
    return dict[x]

# Applying the function to the housing list
df['Response'] = df['Response'].apply(binary_map)

# Print the final DataFrame
print(df)
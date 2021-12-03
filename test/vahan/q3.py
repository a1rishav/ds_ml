import pandas as pd
import numpy as np


'''
Based on the CSV data read in step 1,
 create another CSV file with the salary rank for each employee. Rank 1 is the highest salary
'''

df = pd.read_csv("data.csv")
df['rank'] = df['salary'].rank(ascending=False, method='dense')
df = df.sort_values(by='rank', ascending=True)

# print
for index, row in df.iterrows():
    print("Employee : {}, Department : {}, Salary : {}, Rank : {}".\
          format(row['employee'], row['department'], row['salary'], row['rank']))

df.to_csv("q3_output.csv", index=False)

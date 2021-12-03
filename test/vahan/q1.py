import pandas as pd

df = pd.read_csv("data.csv")

# print rows
for index, row in df.iterrows():
    print("Employee : {}, Department : {}, Salary : {}". \
          format(row['employee'], row['department'], row['salary']))

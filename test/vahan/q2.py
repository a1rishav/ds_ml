import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# summarise by department and sum
summary_df = df.groupby("department").agg({'salary': np.sum}).sort_values(by='salary', ascending=False)

for index, row in summary_df.iterrows():
    print("Department : {}, Salary : {}".format(index, row['salary']))

summary_df.to_csv("q2_output.csv")


import pandas as pd
marks = pd.read_csv('../data/marks.csv')
print(marks.is_null())

filtered_marks = marks.apply(axis=1, func=lambda x : x.isnull().sum() == 5)
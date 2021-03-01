import numpy as np
import pandas as pd

print("Series :\n")
series_1 = pd.Series([6,7,8,9,2,3,4,5])
print(series_1)
print("\nApply\n :")
series_2 = series_1.apply(lambda x : x **2)
print(series_2)

print("\n Series Index :\n")
n = 4
series_index = pd.Series(range(1, n+1))
series = series_index.apply(lambda x: x **2)
series.index = range(1, n +1)
print(series)

print("\nDataframe: \n")
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df = df.set_index("X")
df = df.sort_values(by=["month", "day"], ascending=True)
print(df.head())

print("\nDataframe: selecting rows and columns\n")
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df = df.sort_index(ascending=True)

# Row 5:10
print(df[4:10].head())

# Row 5:end, every alternate
print(df[4::2].head())

# Select column "month"
print(df["month"].head())

# Select columns "month", "day"
print(df[["month", "day"]].head())

# series and dataframe
print(type(df["month"]))
print(type(df[["month"]]))

print("\nDataframe position based indexing : iloc :\n")

# selecting a single element located at 4,6
print(df.iloc[3,5])

# select a single row 5th and all columns
print(df.iloc[4])
print(df.iloc[4,:])

print(df.iloc[[4,7,9]])
print(df.iloc[[4,7,9], :])
print(df.iloc[4:8])

# all rows column 3
print(df.iloc[:, 2])

# multiple columns all rows
print(df.iloc[:, 2:5])

# multiple columns and multiple rows
print(df.iloc[8:12, 2:5])

print("\nDataframe label based indexing : loc :\n")

df.set_index('month', inplace=True)
df = df.loc[['jan', 'feb'],  :]
print(df)

print("\nFiltering dataframe : loc :\n")
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.loc[(df['area']) > 0 & (df['wind'] > 1) & (df['temp'] > 15), :]
print(df_2.head(20))

print("\nMerging dataframe :\n")
df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
df_3 = pd.merge(df_1, df_2, how='inner', on='unique_id')
print(df_3.head(20))

'''
Concatenation is much more straightforward than merging.
It is used when you have dataframes having the same columns and want to append them
(pile one on top of the other), or having the same rows and want to append them side-by-side.
'''
df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
df_3 = pd.concat([df_1, df_2])
print(df_3.head())

gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )
all_df = pd.concat([gold, silver, bronze])
all_df = all_df.groupby('Country').agg({'Medals' : np.sum}).sort_values(by='Medals', ascending=False)
print()

print("\n Group By : \n")
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_1 = df.groupby(["month", "day"]).mean()[["rain", "wind"]]

print(df_1.head(20))

print("\n Dataframe Apply : \n")
df['X_sqaure'] = df['X'].apply(lambda x : x ** 2)
print(df.head())

print("\n Dataframe Pivot : \n")
df.pivot_table(values="wind", index="month", aggfunc='sum', columns='day')
print(df.head())

print("\n Change data type : \n")
ipl18 = pd.DataFrame({'Team': ['SRH', 'CSK', 'KKR', 'RR', 'MI', 'RCB', 'KXIP', 'DD'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [9, 9, 8, 7, 6, 6, 6, 5],
                         'Lost': [5, 5, 6, 7, 8, 8, 8, 9],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 0, 0, 0, 0, 0, 0],
                         'Points': [18, 18, 16, 14, 12, 12, 12, 10],
                         'NRR': [0.284, 0.253, -0.070, -0.250, 0.317, 0.129, -0.502, -0.222],
                         'For': [2230, 2488, 2363, 2130, 2380, 2322, 2210, 2297],
                         'Against': [2193, 2433, 2425, 2141, 2282, 2383, 2259, 2304]},
                         index = range(1,9)
                    )
ipl18['Points'] = ipl18['Points'].astype("int32")
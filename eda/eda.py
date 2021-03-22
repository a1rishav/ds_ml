import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# <<------------------  Univariate analysis --------------->>
# Tendulkar's odi runs dataset
df = pd.read_csv("../data/tendulkar_odi.csv")

# Q : Find types of invalid runs data
df['Invalid_Runs'] = df['Runs'].apply(lambda x : x if not x.isnumeric() else "NA")
print(df['Invalid_Runs'].unique())

# Q : Tendulkar's runs histogram
df['Runs'] = df['Runs'].apply(lambda x : int(x.replace("*", "")) if x.replace("*", "").isnumeric() else "NA")
df = df[df['Runs'] != "NA"]
df['Runs'] = df['Runs'].astype('int32')
sns.displot(df['Runs'], bins=20)
print()

# Q : Tendulkar's 4s histogram
df['4s'] = df['4s'].astype('int32')
sns.displot(df['4s'],binwidth=1)
plt.show()

# News popularity dataset

df = pd.read_csv("../data/news_popularity.csv")
print(df[" num_keywords"].describe())

# Q : Affect of ouliers
print(df[" shares"].mean())
print(df[" shares"].median())

# Q : Get 78th percentile
print(df[" shares"].quantile(q=0.78))

# Q : remove all outliers above 95th percentile
cut_off_value = df[" shares"].quantile(q=0.95)
filtered_df = df[df[" shares"] <= cut_off_value]
print(filtered_df[' shares'].describe())

# Q : percentage of rows removed
print(len(filtered_df) / len(df) * 100)

# Segmented analysis ------------>>

# Dataset : eda_nas.csv

df = pd.read_csv("../data/eda_nas.csv")
print(df.columns.tolist())

# Q : What is the impact of the variable 'Watch.TV' on Science marks?

# df.groupby('Watch.TV').agg({'Science..' : np.mean}).sort_values(by='Science..', ascending=False)
df.groupby('Watch.TV')['Science..'].mean().plot.bar()

# Impact of practising math
df.groupby('Solve.Maths')['Maths..'].mean().plot.bar()

# Dataset : eda_census.csv

df = pd.read_csv("../data/eda_census.csv")

# Q : What percentage of females in the age group 20-24 are illiterate in India ?
#  ---> can be directly seen in the row

# Q : Compare the literacy rates (i.e. the number of literates / total number of population)
# in each age group and choose the correct option.
literacy_df = df[(df['total_rural_urban'] == 'Total') & (df['Area Name'] == 'INDIA')]
literacy_df['literacy_rate'] = df['li_person'] / df['total_person']
literacy_df.groupby('age_group').mean()['literacy_rate'].plot.barh()
plt.show()


# Which state shows the highest female literacy rate?
state_female_literacy_df = df[(df['Area Name'] != 'INDIA')]
state_female_literacy_df['literacy_rate'] = df['li_female'] / df['total_female']
state_female_literacy_df.groupby('Area Name').mean()['literacy_rate'].plot.barh()
plt.show()

## Across all the states, which state shows the lowest literacy rate in 2011 (total population)?
state_literacy_df = df[(df['Area Name'] != 'INDIA')]
state_literacy_df['Area Name'] = state_literacy_df['Area Name'].apply(lambda x : x.replace("State - ", ""))
state_literacy_df['literacy_rate'] = df['li_person'] / df['total_person']
state_literacy_df.groupby('Area Name').mean()['literacy_rate'].plot.barh()
plt.show()

'''
# <<------------------ Bivariate analysis --------------->>

# Dataset : gold_silver_prices.csv

# Q : What is the correlation in Gold and Silver prices (round off the answer to two decimal places)?

'''
df = pd.read_csv("../data/gold_silver_prices.csv")
print(df.corr().iloc[0:1].values[0][1])

# Q : What is the correlation in Gold and Silver prices for the years 2008(nearest two decimal places )?
df["Month"] = pd.to_datetime(df["Month"], format='%b-%y')
df["Year"] = df["Month"].apply(lambda x : x.year)
df.loc[(df["Year"] == 2008)].corr()

# Dataset : currencies.csv

# Q : Indian rupee is the most correlated with

df = pd.read_csv("../data/currencies.csv")
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df.select_dtypes(include=numerics)
ind_corr = newdf.corr().loc[["Indian Rupee"],:]
# sns.heatmap(data=ind_corr, cmap = "Greens", annot=True)
# plt.show()
print()

# Q : Correlation of (Japanese Yen and US dollar), (Australian dollar and INR),
# (Japanese Yen and UK Pound Sterling), (Chinese Yuan and Euro)
print(newdf.corr().loc[["Japanese Yen"],:["U.S. Dollar"],])

# Dataset : nas.csv

# Q : You want to understand the distribution of two variables — mother’s education
# and the number of siblings. Complete the following statement:
# Most children whose mother is illiterate have how many siblings

df = pd.read_csv("../data/nas.csv")
df_ilt = df.loc[(df["Mother.edu"] == 'Illiterate')]
print(df_ilt['Siblings'].value_counts())
print()

# <<------------------ Derived metrics --------------->>

# Q : How father's education and children age affect science marks

# Dataset : odi-batting.csv

# Q : Which player scored the highest number of centuries?
df = pd.read_csv("../data/odi-batting.csv")
df["century"] = df["Runs"].apply(lambda run : 1 if run >= 100 else 0)
df.groupby("Player").agg({'century' : np.sum}).sort_values(by='century', ascending=False)

# Q : Fastest century innings
df["strike_rate"] = df.apply(lambda row : row["Runs"]/row["Balls"] *100, axis=1)
df.loc[(df.Runs >= 100)].sort_values(by='strike_rate', ascending=False)

# Q : In which year were the maximum number of centuries scored by Indian players?
df["year"] = df["MatchDate"].apply(lambda date : date[-4:])
df.loc[(df.Country == 'India')].groupby("year").agg({'century' : np.sum}).sort_values(by='century', ascending=False)


# Dataset : grades.csv

# Q : Which player scored the highest number of centuries?
df = pd.read_csv("../data/grades.csv")
df["format"] = df["submission"].apply(lambda link : link.split("/")[-1].split(".")[-1])
df["roll_no"] = df["submission"].apply(lambda link : link.split("/")[-1].split(".")[0])
df["format"].value_counts()['zip'] / len(df)

# Q : How many students submitted the assignment after the first deadline -> Jan 3, 2017 - 11:59:59 PM
# (including the students who submitted after the second deadline)  ?
df["submit_datetime"] = pd.to_datetime(df['submit_time'])
first_deadline = datetime.strptime('2017-01-03 23:59:59', '%Y-%m-%d %H:%M:%S')
len(df.loc[(df.submit_datetime > first_deadline)].sort_values(by='submit_datetime', ascending=True))

# Q : On which date did the most students submit the assignment?
df["date"] = df["submit_time"].apply(lambda x : x.split("-")[0])
df.date.value_counts()

# Q : In which hour of the day did most students submit the solution?
df["hour"] = df["submit_datetime"].apply(lambda x : x.hour)


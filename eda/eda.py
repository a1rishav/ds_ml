import pandas as pd
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


# <<------------------  Univariate analysis --------------->>

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analysing ordered categorical variable
df = pd.read_csv("../data/tendulkar_odi.csv")

# Tendulkar's runs histogram

# Runs values with string datatype
df['Invalid_Runs'] = df['Runs'].apply(lambda x : x if not x.isnumeric() else "NA")
print(df['Invalid_Runs'].unique())

df['Runs'] = df['Runs'].apply(lambda x : int(x.replace("*", "")) if x.replace("*", "").isnumeric() else "NA")
df = df[df['Runs'] != "NA"]
df['Runs'] = df['Runs'].astype('int32')
sns.displot(df['Runs'], bins=20)
print()

# Tendulkar's 4s histogram
df['4s'] = df['4s'].astype('int32')
sns.displot(df['4s'],binwidth=1)
plt.show()
print()


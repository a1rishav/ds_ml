import pandas as pd

'''
1. Find the expected loss of student loan - dataset : student_loan.csv
 Expected Loss is EAD * P(loss) *  (1 - Recovery rate)
'''

df = pd.read_csv("data/student_loan.csv")
df['Recovery (%)'] = df['Recovery (%)'].apply(lambda x : float(x.split("%")[0].strip())/100)

df['expected_loss'] = df.apply(lambda row : row["Exposure at Default (in lakh Rs.)"] * \
                               row["Probability of Default"] * (1 - row['Recovery (%)']), axis=1)

df = pd.read_csv("data/rents.csv")

mean = df["mr"].sum()/ len(df)
df["variance"] = df["mr"].apply(lambda x : pow(x - mean, 2))
std = pow(df["variance"].sum() / (len(df) - 1), 0.5)
print()

m=100#mean
sd=10
import scipy.stats as stats


z_score = ((90 - m) / sd)
probaility = 1 - stats.norm.cdf(z_score)
print(str(round(probaility, 2)))
print()



def checkmail(email):
    username = email.split()
    #the function should return the strings "invalid" or "valid" based on the email ID entered
email=input()
print(checkmail(email))
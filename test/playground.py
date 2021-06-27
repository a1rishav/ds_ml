import pandas as pd
import numpy as np

n = 4
arr =np.array( [[0 , 1],  [1,  0]])
print(np.tile(arr, (n // 2, n //2)))

m = 3
a = np.ones(shape=(m,m), dtype = int)
print()

for row in range(m) :
    for column in range(m) :
        if row != 0 and row != m-1 and column != 0 and column != m-1:
            a[row][column] = 0

print(a)
print()
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
ipl18 = ipl18.loc[(ipl18['NRR'] > 0) & (ipl18["For"] > ipl18["Against"]), :]

ipl17 = pd.DataFrame({'Team': ['MI', 'RPS', 'SRH', 'KKR', 'KXIP', 'DD', 'GL', 'RCB'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [10, 9, 8, 8, 7, 6, 4, 3],
                         'Lost': [4, 5, 5, 6, 7, 8, 10, 10],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 1, 0, 0, 0, 0, 1],
                         'Points': [20, 18, 17, 16, 14, 12, 8, 7],
                         'NRR': [0.784, 0.176, 0.469, 0.641, 0.123, -0.512, -0.412, -1.299],
                         'For': [2407, 2180, 2221, 2329, 2207, 2219, 2406, 1845],
                         'Against': [2242, 2165, 2118, 2300, 2229, 2255, 2472, 2033]},
                         index = range(1,9)
                    )

ipl_17_is_df = pd.concat([ipl17, ipl18])

cat_cols = {"MSZoning", "Street", "Alley", "LotShape", "LandContour", "LotConfig", "LandSlope", "Neighborhood",
            "Condition1", "Condition2", "BldgType", "HouseStyle", "RoofStyle", "RoofMatl", "Exterior1st", "Exterior2nd",
            "MasVnrType", "Foundation", "BsmtCond", "Heating", "Electrical", "GarageType", "SaleType", "SaleCondition"}

label_encoding = { "Utilities","ExterCond","ExterQual","BsmtQual","BsmtCond",
"BsmtExposure","BsmtFinType1","BsmtFinType2"," HeatingQC",
"KitchenQual","Functional","FireplaceQu","GarageQual","GarageFinish",
"PavedDrive","Fence"}

print()
import pandas as pd

## 1. Check if email is valid
import re

def checkmail(email):
    splits = re.split('@|\.',email)
    username = splits[0]
    website = splits[1]
    extension = splits[2]

    if len(splits) != 3:
        return "invalid"

    if not username.isalnum():
        return "invalid"

    if not (website.islower() and website.isalpha()):
        return "invalid"

    if not (extension.islower() and extension.isalpha() and \
                (len(extension) == 2 or len(extension) == 3)):
        return "invalid"

    return "valid"
    #the function should return the strings "invalid" or "valid" based on the email ID entered

email="prerna@upgrad.com"
print(checkmail(email))

## 2. Flatten nested list

flattened_list = []
input_list = [[1,2,3],[4,5],[6,7,8,9]]

for elements in input_list:
    for element in elements :
        flattened_list.append(element)

out = 0
for counter in range(1, 5) :
    out+= int(str(2) * counter)


string = sorted("ddddaccbb")
count_map = {}
for char in string:
    count_map[char] = string.count(char)

df = pd.DataFrame.from_dict(count_map, orient="index", columns=['count'])
df = df.sort_values(by="count", ascending=False)
list(df[:2].index.values)
print()
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file1data = pd.read_excel("RESULT1.xlsx")
print(file1data)
print(type(file1data))

file2data = pd.read_excel("RESULT2.xlsx")
print(file2data)

alldata = pd.concat([file1data,file2data])
print(alldata)

name = list(alldata['NAME'])
total = list(alldata['TOTAL'])

plt.bar(name,total)
plt.show()

print(alldata.sort_values(['TOTAL'],ascending=False))
print(alldata.sort_values(['TOTAL'],ascending=False).head(3))
print(alldata.sort_values(['TOTAL'],ascending=False).tail(3))

# print all dat with total greater than 200
# create one column 'CATEGORY' and store result.csv file  as below
# 80-100 : SCHOLER
# 50-79 : AVERAGE
# BELOW 50 : WEAK
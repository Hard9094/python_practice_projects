import pandas as pd
from sklearn import linear_model

df = pd.read_csv("orderdata.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['users','orders','age']],df.amount)
print(reg.predict([[500,1750,33]]))
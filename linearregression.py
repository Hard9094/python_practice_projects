#linear Regression
import  pandas as pd
from matplotlib import pyplot as plt
from sklearn import  linear_model
df = pd.read_csv('prices.csv')
print(df)
# y = b0 + b1x
plt.scatter(df.area,df.price)
plt.show()
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df[['price']])
print(reg.predict([[3300]]))
# y = b0 + b1 ( x )
print(reg.coef_) # b1
print(reg.intercept_) # b0
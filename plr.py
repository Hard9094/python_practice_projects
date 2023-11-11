from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("orders.csv")
plt.scatter(df.slot,df.amount)
#plt.show()
poly = PolynomialFeatures(degree=5)
x_poly = poly.fit_transform(df[['slot']])

reg = LinearRegression()
reg.fit(x_poly,df[['amount']])


import pandas as pd
import numpy as np

mydata = [15,25,35]
pddata = pd.DataFrame(mydata)
print(pddata)

newdata = (15,25,35)
newpddata = pd.DataFrame(newdata)
print(newpddata)

impdata = {"a":[30,20],'b':[40,10],'c':[50,0]}
imppddata = pd.DataFrame(impdata)
print(imppddata)

game = pd.DataFrame([['ROHIT','BATSMAN',50],['KOHLI','BATSMAN',80],['BUMRAH','BOWLER',15]],
                    columns=["NAME",'TYPE','SCORE'])
print(game)
print(game['NAME'][1])

empdata = np.array([[8000,10000,18000],[15000,18000,25000]])
pdempdata = pd.DataFrame(empdata,index=["RAMESH","MAHESH"],columns=[2020,2021,2022])
print(pdempdata)
pdempdata['TOTAL'] = 12*(pdempdata[2020]+pdempdata[2021]+pdempdata[2022])
print(pdempdata)

pdempdata[2023] = pdempdata[2022] + (pdempdata[2022]*0.30)
print(pdempdata)

pdempdata.to_csv('filename.csv')
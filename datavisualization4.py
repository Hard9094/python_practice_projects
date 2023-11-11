import numpy as np
from matplotlib import pyplot as plt

matches = [1,2,3,4,5]
rohit = [25,15,45,70,65]
kohli = [17,12,55,42,35]
dhavan =  [10,47,23,17,94]
barwidth = 0.15

fig = plt.figure(figsize=(15,10))
plt.bar(np.arange(len(matches)),rohit,width=barwidth,label="ROHIT")
plt.bar(np.arange(len(matches))+0.15,kohli,width=barwidth,label="KOHLI")
plt.bar(np.arange(len(matches))+0.30,dhavan,width=barwidth,label="DHAVAN")

plt.xlabel("MATCHES")
plt.ylabel("SCORE")
plt.title("PLAYER PERFOMANCE")
plt.legend()
plt.show()

from matplotlib import pyplot as plt

cities = ["Ahmedabad","Surat","Rajkot"]
cases = [275,195,75]

mydata = {"cities":["AHMEDABAD","SURAT","RAJKOT"],"cases":[275,195,75]}
cities_new = mydata["cities"]
cases_new = mydata["cases"]

mydata = {"alldata":[{"city":"Ahmedabad","cases":275},
                     {"city":"SURAT","cases":195},
                     {"city":"RAJKOT","cases":75}]}

cities_api = []
cases_api = []
for i in range(0,len(mydata["alldata"])):
    cities_api.append(mydata["alldata"][i]["city"])
    cases_api.append(mydata["alldata"][i]["cases"])

plt.bar(cities_api,cases_api,color="r")
plt.xlabel("Cities")
plt.ylabel("Covid Cases")
plt.title("GUJARAT COVID CASES")
plt.show()

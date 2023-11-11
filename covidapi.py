# go to terminal and instll package : pip install requests

import requests

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()
print(mydata)
print(type(mydata))

# print all the keys
for i in mydata:
    print(i)
print(mydata["cases_time_series"][0]["date"])

# total number of days :
print("total number of days : ",len(mydata["cases_time_series"]))

# print all data :
for i in range(0,len(mydata["cases_time_series"])):
    print("Date : ",mydata["cases_time_series"][i]["date"],
          "Cases : ",mydata["cases_time_series"][i]["dailyconfirmed"],
          "Deaths : ",mydata["cases_time_series"][i]["dailydeceased"])

print("=====================================================")
# print  all data of days which are having cases more than 100000
for i in range(0,len(mydata["cases_time_series"])):
    if int(mydata["cases_time_series"][i]["dailyconfirmed"])>=100000:
        print("Date : ", mydata["cases_time_series"][i]["date"],
              "Cases : ", mydata["cases_time_series"][i]["dailyconfirmed"])


# store all dates
# highest cases
# print date of that day
# print total number of days ( count ) which having greater than 1 lac

userdate = input("Enter Date :")

for i in range(0,len(mydata["cases_time_series"])):
    if userdate == mydata["cases_time_series"][i]["date"]:
        #print("Date found")
        print("New cases :",mydata["cases_time_series"][i]["dailyconfirmed"])
        break
else:
    print("Date Not Found")

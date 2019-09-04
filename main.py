# To-do
# 1. find out finance api for currency converter (fixer.io) - done
# 2. Allow users to select any of the 3 values (user selection model = in terminal) 
# 3. build function to convert currency A to currency build
# 4. Return result





# Description of project
# build a simple terminal currency converter from RM to 3 currencies
# 1. United States Dollar (USD)
# 2. Japanese Yen (YEN)
# 3. Singapore Dollar (SGD)







import requests
import json

requests = requests.get('http://data.fixer.io/api/latest?access_key=64462d177fc6f5eddae277f0290382a3&symbols=USD,JPY,SGD,MYR,EUR')

# print(requests.json())

data = requests.json()

USD = data['rates']['USD']
JPY = data['rates']['JPY']
SGD = data['rates']['SGD']
MYR = data['rates']['MYR']
EUR = data['rates']['EUR']

print(USD)
print(JPY)
print(SGD)
print(MYR)
# print(EUR)

# User input of MYR
amount = float(input("Enter your MYR: "))

# from MYR to EUR as a base
msiaRinggit = amount / MYR

# conversion formulas
conversionUSD = msiaRinggit * USD
conversionJPY = msiaRinggit * JPY
conversionSGD = msiaRinggit * SGD


# print (conversionUSD)
# print (conversionJPY)
# print (conversionSGD)

# currencyChoice = int(input("Select your currency:\n1.USD\n2.JPY\n3.SGD\n"))

def looping():
    # currencyChoice = str(input("Select your currency:\n1.USD\n2.JPY\n3.SGD\n"))

    test = 0


    while test != "4":
        currencyChoice = str(input("Select your currency:\n1.USD\n2.JPY\n3.SGD\n"))


        if currencyChoice == "1":
            print(conversionUSD)
            return currencyChoice
        elif currencyChoice == "2":
            print(conversionJPY)
            return currencyChoice
        elif currencyChoice == "3":
            print(conversionSGD)
            return currencyChoice
        else: 
            test == "4"
            print("Please select the right choice.")
            looping()
            return test



looping()




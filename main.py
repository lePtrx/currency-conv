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

# print(USD)
# print(JPY)
# print(SGD)
# print(MYR)
# print(EUR)

# User input of MYR

# amount = float(input("Please key in your MYR to convert: "))

# from MYR to EUR as a base
# msiaRinggit = amount / MYR

# conversion formulas
# conversionUSD = msiaRinggit * USD
# conversionJPY = msiaRinggit * JPY
# conversionSGD = msiaRinggit * SGD


# print (conversionUSD)
# print (conversionJPY)
# print (conversionSGD)

#currencyChoice = int(input("Select your currency:\n1.USD\n2.JPY\n3.SGD\n"))

# choice = True


# if currencyChoice == 1:
#     print(conversionUSD)
# elif currencyChoice == 2:
#     print(conversionJPY)
# elif currencyChoice == 3:
#     print(conversionSGD)
# else:
#     print("Please select the right choice.")

def menu():
    print("Welcome to project9you! Please select option (1) to key in your MYR amount before selecting the other options:")
    print()
    print("1.Insert MYR amount.")
    print("2.Convert to USD")
    print("3.Convert to JPY")
    print("4.Convert to SGD")
    print("5.Quit")
    print()

loop = 1

while loop == 1:
    menu()
    userChoice = str(input("What would you like to do? "))
    if userChoice == "1":
        print()
        amount = float(input("MYR to convert: "))
        msiaRinggit = amount / MYR
        print()
        print (amount,"MYR")
        print()
    elif userChoice == "2":
        conversionUSD = msiaRinggit * USD
        print()
        print (amount,"MYR")
        print ("=")
        print(conversionUSD,"USD")
        print()
    elif userChoice == "3":
        conversionJPY = msiaRinggit * JPY
        print()
        print (amount,"MYR")
        print ("=")
        print(conversionJPY,"JPY")
        print()
    elif userChoice == "4":
        conversionSGD = msiaRinggit * SGD
        print()
        print (amount,"MYR")
        print ("=")
        print(conversionSGD,"SGD")
        print()
    elif userChoice == "5":
        loop = 0
        print("\nThank you for using project9you, hope to see 9 you again!")
    else:
        print("\nPlease select from the above option.\n")   








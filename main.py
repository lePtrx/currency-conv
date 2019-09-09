""" 
To-do
1. Find out finance api for currency converter (fixer.io) - done
2. Allow users to select any of the 3 values (user selection model = in terminal) - done
3. Build function to convert currency A to currency build - done
4. Return result - done
"""

"""
Description of project
------------------------------------------------------------------
Build a simple terminal currency converter from Malaysian Ringgit (MYR) to 3 foreign currencies:
1. United States Dollar (USD)
2. Japanese Yen (YEN)
3. Singapore Dollar (SGD)
"""

# Importing libraries and modules
import json
import requests

# To get data from finance API
requests = requests.get('http://data.fixer.io/api/latest?access_key=64462d177fc6f5eddae277f0290382a3&symbols=USD,JPY,SGD,MYR,EUR')

# To get the rates for each currencies using European Euro (EUR) as the base currency
data = requests.json()

USD = data['rates']['USD']
JPY = data['rates']['JPY']
SGD = data['rates']['SGD']
MYR = data['rates']['MYR']
EUR = data['rates']['EUR']

# The body of the programme
def startProgram():

    print("This program converts MYR to USD, JPY or SGD!")
    
startProgram()

runloop = 1

while runloop == 1:

    # Try and Exception error handling to ensure user input only integers ir floats value
    try:

        amount = float(input("\nWhat's your MYR amount?: "))
       
        # From the conversion of EUR to MYR with MYR as base currency
        msiaRinggit = amount / MYR

        # Conversion formulas from MYR to other currencies
        conversionUSD = msiaRinggit * USD
        conversionJPY = msiaRinggit * JPY
        conversionSGD = msiaRinggit * SGD

        # To ask user to input choices of currency conversion or other choices
        def menu():
            print("\nPlease select your currency:")
            print("\n1." ,amount, "MYR to USD")
            print("2." ,amount, "MYR to JPY")
            print("3." ,amount, "MYR to SGD")
            print("4. Input another MYR amount")
            print("5. Quit")

        loop = 1

        while loop == 1:
            menu()
            currencyChoice = str(input("\nYour choice?: "))

            # To do the conversion calculations and printing of result
            if currencyChoice == "1":
                print("\n",amount, "MYR is" ,round(conversionUSD,2), "in US Dollars (USD)!")
            elif currencyChoice == "2":
                print("\n",amount, "MYR is" ,round(conversionJPY,2), "in Japanese Yen (JPY)!")
            elif currencyChoice == "3":
                print("\n",amount, "MYR is" ,round(conversionSGD,2), "in Singapore Dollars (SGD)!")
            
            # To redirect users to input another value
            elif currencyChoice == "4":
                loop = 0
                startProgram()

            # To end programme
            elif currencyChoice == "5":
                loop = 0
                runloop = 0
                print("\nProgramme closed! Thanks for using! :D\n")

            # To alert users to input only the available options
            else:
                print("\nPlease select only from the above options.\n")

    # To alert users to input only values of correct formats and redirect users to input another value
    except:
        print("\nPlease input only numeric!\n")
        startProgram()
    
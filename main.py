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


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
print(EUR)
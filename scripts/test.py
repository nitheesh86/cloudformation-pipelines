# Python program to demonstrate
# Conversion of JSON data to
# dictionary


# importing the module
import json


import json

with open('credential.json', 'r') as f:
  data = json.load(f)
  print(data)

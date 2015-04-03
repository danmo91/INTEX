#!/usr/bin/python

# requires "pip install requests"
import requests

# send the request with the data
API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
API_KEY = 'f8b32e2588393caea9c8b92f7336fefd'

r = requests.post(API_URL, data={
    'apikey': API_KEY,
    'currency': 'usd',
    'amount': '5.99',
    'type': 'Visa',
    'number': '4732817300654',
    'exp_month': '10',
    'exp_year': '15',
    'cvc': '411',
    'name': 'Cosmo Limesandal',
    'description': 'Charge for cosmo@is411@byu.edu',
})

# check repsonse text
print(r.text)

# parse response dictionary
resp = r.json()
if 'error' in resp:
    print('ERROR: ', resp['error'])

else:
    print(resp.keys())
    print(resp.['ID']

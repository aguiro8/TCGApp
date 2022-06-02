import requests
import json
# https://towardsdatascience.com/building-a-cardboard-empire-introduction-to-the-tcgplayer-api-using-python-fbfc2d62ef51
url = "https://api.tcgplayer.com/token"
# client_id=PUBLIC_KEY&client_secret=PRIVATE_KEY
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {'grant_type': 'client_credentials',
'client_id': '42cac4f7-4ea9-438d-8c0a-111c09a864ea', 
'client_secret': '3e89eaed-9974-4aee-b80b-586c2564b992'}

response = requests.post(url, headers = headers, data=data)

access = response.json()['access_token']

url = 'https://api.tcgplayer.com/catalog/categories/66/search'
headers = {'accept': 'application/json',
            'content-type': 'application/json',
            'User-Agent': 'Meta-Zoo',
             'Authorization' : "bearer "+ access}
params = {'limit': '67'}
payload = {
    'sort': 'Relevance',
    'filters' : [{
        'values': ['Wendigo'],
        'name': 'productName'
    }]
}
# Metazoo = categoryId :66
search_response = requests.request("POST",url, headers = headers, json=payload)

endpoint = "https://api.tcgplayer.com/catalog/products/"
productids = str(search_response.json()["results"])
productids = productids.replace('[','')
productids = productids.replace(']','')
url = endpoint + productids
response = requests.get( url, headers=headers)
print(response.json())

import json
import requests

headers = {'Accept': 'application/json'}
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url, headers=headers)
response_data = r.json()
print("$" + response_data["bpi"]["USD"]["rate"])




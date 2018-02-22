import pprint
import requests

response = requests.get('https://httpbin.org/get')
pprint.pprint(response.json())


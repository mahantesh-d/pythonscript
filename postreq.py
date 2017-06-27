import requests

url = 'http://10.252.169.12:7788/v1/product/productSpecification/productMaster.json'

headers = {'Authorization' : '(anything)', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.post(url, data=open('productMaster.json', 'rb'), headers=headers)
print('Status Code: ',r.status_code)
print(r.json())
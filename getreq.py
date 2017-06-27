import requests
import json
try:
    r = requests.get("http://10.252.169.12:7788/v1/product/productSpecification/productMaster.json?filter=(|(matCode_key15=003)(company_key0=asas10))")
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
    exit(1)
r.close()
print('Request_URL: ', r.url)
print ('Status Code: ', r.status_code)
print ('Content-Length: ', r.headers.get('Content-Length'))
print('Response_Time: ', r.elapsed)
print ('Data: ',r.json())



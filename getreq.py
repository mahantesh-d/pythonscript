import requests
import json
try:
   # r = requests.get("http://10.252.169.12:7788/v1/product/productSpecification/productMaster.json?filter=(|(matCode_key15=003)(company_key0=asas10))")
    r = requests.get("https://httpbin.org/get")
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
    exit(1)
r.close()
print('Request_URL: ', r.url)
print ('Status Code: ', r.status_code)
print ('Content-Length: ', r.headers.get('Content-Length'))
print('Response_Time: ', r.elapsed)
print ('Data: ',r.json())
a = list((r.url, r.status_code, r.headers.get('Content-Length'),r.elapsed))
print(type(a))
print(a)

b = []
for i in range(0,5):
    try:
        # r = requests.get("http://10.252.169.12:7788/v1/product/productSpecification/productMaster.json?filter=(|(matCode_key15=003)(company_key0=asas10))")
        rr = requests.get("https://httpbin.org/get")
        b.append((rr.url, rr.status_code, rr.headers.get('Content-Length')))
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        exit(1)
print(b)

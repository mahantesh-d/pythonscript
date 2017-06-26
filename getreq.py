import requests
try:
    r = requests.get("http://10.252.169.12:7788/v1/product/productSpecification/productMaster.json?filter=(|(matCode_key15=qwqw17)(company_key0=asas10))")
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
    exit(1)
r.close()
print('Request_URL: ', r.url)
print ('Status Code: ',r.status_code)
#print ('Headers: ',r.headers)
print ('Content-Length: ',r.headers.get('Content-Length'))
print('Response_Time: ',r.elapsed)
#print (r.json())
#a = {'abc':1, 'abcd':'2'}
#print(a.get('abcd'))
print("Host not found")

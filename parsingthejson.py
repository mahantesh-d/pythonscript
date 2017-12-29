import json
with open('alltrade_unified.json') as json_data:
    d = json.load(json_data)
#key = d['stock_adjustment']
#print('>>>>>>>>>>>>>>>>>>>>>>>>',key['apiName'])
apiName = list(d)
fieldsName = []
count1 = 0
for x in range (0, len(apiName)):
    key = d[apiName[x]]
    convList = list(key)
    fieldsName.append(list(key['fields']))
    abcd = list(key['fields'])
    #print('>>>>>>>>>>>>>>>>>>>', abcd[5])
    key2 = abcd[5]
    print('>>>>>>>>>>>>>>>>>>>', key2)
    count1 = count1 + 1
print(count1)
count = 0
for i in range(0, len(fieldsName)):
    print('APIName>>>>>>>>>>>>>',apiName[i])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>.',fieldsName[i][5])
    count = count + 1
print(count)



#print(c)
#print(type(c))

import json
with open('alltrade_unified.json') as json_data:
    d = json.load(json_data)
#key = d['stock_adjustment']
#print('>>>>>>>>>>>>>>>>>>>>>>>>',key['apiName'])
apiName = list(d)
fieldsName = []
#print(apiName)
for x in range (0, len(apiName)):
    key = d[apiName[x]]
    fieldsName.append(list(key['fields']))
#print(fieldsName)
#print(len(fieldsName))
count = 0
for i in range(0, len(fieldsName)):
    #print('APIName>>>>>>>>>>>>>',apiName[i])
    createfile = open(apiName[i]+'.toml', 'w')
    createfile.write('[%s]\n'%apiName[i])
    createfile.write('update_filter = %s\n'%fieldsName[i][5])
    createfile.write('get_filter = %s\n'%fieldsName[i][5])
    createfile.write('delete_filter = %s\n'%fieldsName[i][5])
    createfile.write('update_payload = \n')
    createfile.write('post_payload = \n')
    #print(fieldsName[i][5])
    count = count + 1
print(count)



#print(c)
#print(type(c))

import json
with open('alltrade_unified.json') as json_data:
    d = json.load(json_data)
#print(d)
listd = list(d)
print(listd[21])
for x in range (0, len(listd)):
    #print('>>>>>>>>>>> APIName: ',x, listd[x])
    apiName = d[listd[x]]
    #print('>>>>>>>>>>> APIName: ',apiName)
    fields = apiName['fields']
    #print(fields)
    fieldslist = list(fields)
    column = fields[fieldslist[5]]
    #print(column)
    column1 = column['name']
    #print('>>>>>>>>>>>>>>>>>>>>>>> Column Name: ',column1)

import json
with open('alltrade_unified.json') as json_data:
    d = json.load(json_data)
#print(d)
count = 0
listd = list(d)
for x in range (0, len(listd)):
    print('>>>>>>>>>>> APIName: ',x, listd[x])
    createfile = open(listd[x]+'.toml', 'w')
    createfile.write('[%s]\n'%listd[x])
    apiName = d[listd[x]]
    #print('>>>>>>>>>>> APIName: ',apiName)
    fields = apiName['fields']
    #print(fields)
    fieldslist = list(fields)
    column = fields[fieldslist[5]]
    #print(column)
    column1 = column['name']
    print('>>>>>>>>>>>>>>>>>>>>>>> Column Name: ',column1)
    createfile.write('\tupdate_filter = \"%s\"\n'%column1)
    createfile.write('\tget_filter = \"%s\"\n'%column1)
    createfile.write('\tdelete_filter = \"%s\"\n'%column1)
    createfile.write('\tupdate_payload = \n')
    createfile.write('\tpost_payload = \n')
    count = count + 1
print('Number of Toml files Created: ', count)
import json
with open('alltrade_unified.json') as json_data:
    key1 = json.load(json_data)

#declare empty list
listkey2 = []
listkey3 = []
#print the entire json
#print('Type: ',type(key1),': ', key1)

#convert json into list
listkey1 = list(key1)

#print the list it will print first key------1 in json like ['stock_adjustment', 'obtain_detail',........]
#print('Type: ',type(listkey1),': ',listkey1)
#print(len(listkey1))
#Iterate over the list to print the values of key------1
for x in range (0,len(listkey1)):
    #print the values of key------1
    key2 = key1[listkey1[x]]
    key3 = key2['fields']
    listkey3.append(key3)
    print(listkey3)
    #key4 = key3[listkey3[x]]
    #print(key4)
    #print(key3)
    #print(key4)
    #print('Type: ',type(key2),': ',key2)

    #Convert into list for that append into the list declared above
    listkey2.append(key2)
#print(len(listkey2))
#print key2 as list
#print('Type: ',type(listkey2),': ',listkey2)




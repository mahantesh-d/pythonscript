import re
a = open('alltrade_unified.json', 'r+')

#list=['a cat','a dog','a yacht','cats','"apiName": "alltrade_stock_adjustment"']
#string = 'a cat'
#if string in list:
#    print('found cat')
regex=re.compile(".*(apiName).*")
found = filter(regex.match, a)
print(*found)
#regrealname = re.compile()




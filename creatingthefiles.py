import os
a = open('filenames.txt', 'r+')
d = open('abcdefgh.txt', 'w')
d.write("hello world")
print(a)
read = a.readlines()
#print(read)
count=0
for x in range(0, len(read)):
    print(read[x])
    count=count+1
print(count)
b = 'test.toml'
print('this the filename %s'%b)
c = open('test.txt', 'r+')
c.write('this is the testfile')
c.close()

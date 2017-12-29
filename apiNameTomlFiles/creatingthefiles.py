import os
a = open('filenames.txt', 'r+')
#d = open('abcdefgh.txt', 'w')
#d.write("hello world")
#print(a)
read = a.readlines()
print(type(read[0]))
#print(read)
count=0
for x in range(0, len(read)):
    z = open(read[x].rstrip(), 'w')
    z.write("this demo of file creating")
    z.close()
    count=count+1
print(count)


import configparser

Config = configparser.ConfigParser()
print(Config)
print(Config.read("sampleconfig.txt"))
print(Config.sections())
a = Config.items('your-config')
print(a)
print(type(a))
#print(a[0][1])
for i in range(0,len(a)):
    print(a[i][1])

items = [1, 2 , 3]
def sqr(x): return x ** 2
print(list(map(sqr, items)))

#splitlist = ['abc','xyz']
#sd = dict(u.split(":") for u in splitlist.split(","))
#print(sd)

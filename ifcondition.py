import sys

print('Number of Arguments: ', len(sys.argv), 'arguments')
a = str(sys.argv[1])
if a == "Foo" :
        print('Hello', a)
else:
        print("Wrong Entry")
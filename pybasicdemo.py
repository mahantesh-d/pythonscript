print ("Hello World")		#print hello world

a = 5+6 					#*************
print ('a = 5 + 6 ----->', a)					#declaring the variable
b = 10 + a 					#using the variable
print ('b = 10 + a ----->', b)  					#printing the variable

print ("print ('Spam Eggs') ----->", 'Spam Eggs') 		#normal print
print ("print ("'Spam Eggs'") ----->", "'Spam Eggs'") 		#it will print with single quote
print('"hello"') 			#print string with double quote

#print ('doesn't') this will throw error
print ("doesn't") 			#you can use the double quote
print ('doesn\'t') 			#use \' to escape the single quote in string

print ("This is first line\nThis second line") #Using the new line character
print ('C:\some\name') 		#\name it take as \n as new line
print (r'C:\some\name') 	#use r to at beginning to print it properly

print ("""\
		printing the multiple lines
		using the the triple double quotes
		this good for paragraph writing
		""")

print (3 * 'uni') 			#multiplying the string thrice
print (3 * 'maha' + ' dhale') # string concatenation
print ('mahan''tesh') 		#string concatenation

word = 'mahantesh'
print(word[0]) 			#Print the character in '0'th position
print(word[5])			#Print the character in '5'th position
print(word[0],word[1],word[2],word[3],word[4],word[5],word[6],word[7],word[8]) #Indexing, check the position
print('0'' 1'' 2'' 3'' 4'' 5'' 6'' 7'' 8')
print('*********************************')
print(word[-1],word[-2],word[-3],word[-4],word[-5],word[-6],word[-7],word[-8],word[0]) #Indexing, check the position
print('-1''-2''-3''-4''-5''-6''-7''-8'' 0')
print('*********************************')
print(word[0:2]) #Print the character from 0 (included) till 2 (excluded)
print(word[3:5]) #Print the character from 3 (included) till 5 (excluded)
print(word[:2]+word[1:]) #This is print(word[:i]+word[i:]) is always equal to print(word)
print(word[:2]) #This printing character from beginning to 2 excluded
print(word[4:]) #This printing character from 4 included to end
print(word[-2:]) #This printing character from second-last included to end
print(word[:-2]) #This printing character from beginning to second-last excluded to end
#print(word[42]) this will throw index out of range
print(word[2:42]) #Out of index range is handled gracefully
#word[0] = 'J' python string cannot be changed they are immutable
print('J' + word[1:]) #can build a new string
print('J' + word[-7])
print(len(word)) #length of the string
print(word[:]) #This will return new copy of string

#List Demo
square = [1, 4, 9, 16, 25] #Creating the list
print(square)
print(square[0]) #Indexing
print(square[-1])
print(square[-3:]) #Slicing the list
print(square[:]) #this will return new copy of list
print(square + [36,49,64,81,100]) #List Concatenation
cube = [1, 8, 27, 16] #List are mutable 
print(cube)
cube[3] = 16*4 #Inserting the correct value at 3 postion
print(cube)
cube.append(125) #appending the cube
print(cube)
cube.append(6**3)
print(cube)
print(len(cube))
#More on list and Slices
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
letters[2:5] = ['C', 'D', 'E'] #replace the contents of the list
print(letters)
letters[2:5] = [] #remove the letters from the list
print(letters)
letters[:] = [] #clear the entire list
print(letters)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
nested = [square, cube, letters]
print(nested)
print(nested[0])
print(nested[1],nested[2])

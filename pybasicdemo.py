print ("Hello World")		#print hello world

a = 5+6 					#*************
print (a)					#declaring the variable
b = 10 + a 					#using the variable
print (b)  					#printing the variable

print ('Spam Eggs') 		#normal print
print ("'Spam Eggs'") 		#it will print with single quote
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
print(word[0:2]) #Print the character from 


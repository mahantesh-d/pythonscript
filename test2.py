import xlrd     #package for reading the excel
from operator import itemgetter

book = xlrd.open_workbook('sample.xlsx')           #Open the excel file

print ('Number of sheets: ',book.nsheets)       # print number of sheets

print ('Sheet Names: ',book.sheet_names())      # print sheet names

first_sheet = book.sheet_by_index(0)        # get the first worksheet

a = ""
con = ""

#read a row
#print (first_sheet.row_values(0))
#-------------------------------------------------------------------------------------

def concatenate(a): #Concatenate the output from the excel to 'http://'
    b = 'http://' + a + ':9001'
    print(b)

#-------------------------------------------------------------------------------------

for i in range(1,x):        #Iterating over the rows and getting the values
    #con = "".join(str(x) for x in first_sheet.row_values(i))        #Combining the the values of the list
    aa = first_sheet.row_values(i)[4]
    print(aa)
    if aa == 'Active':
        bb = first_sheet.row_values(i)[5]
        con = "".join(itemgetter(3,0)(first_sheet.row_values(i)))  #Combining the the values of the list)
        if bb == 'POST':
            concatenate(con) #passing to the concatenate function
        else :
             print('GET')
    else:
        print(first_sheet.row_values(i))

#-------------------------------------------------------------------------------------

# read a cell
cell = first_sheet.cell(0,0)     #Get the cell Values
print ('Data type with Value: ',cell)        #Print with data type
print ('Print the Value: ', cell.value)      #print only values

#-------------------------------------------------------------------------------------

#print ('Reading the rows in slices: ',first_sheet.row_values(rowx=1, start_colx=0, end_colx=4)) # read a row slice

x = first_sheet.nrows       #Get the number of rows

for j in range(1, x):
    z = first_sheet.cell(j, 4).value
    print(z)
    if z == 'Active':
        y = first_sheet.cell(j, 5).value
        rv = first_sheet.row_values(rowx=j, start_colx=0, end_colx=3)
        if y == 'POST':
            print ('Reading the rows in slices: ', rv, ' is a POST Method')
        else:
            print ('Reading the rows in slices: ', rv, ' is a GET Method')
    else:
        print('User is Inactive: ', rv)
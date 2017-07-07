import xlrd
from xlrd.sheet import ctype_text

#Open the excel file
xl_workbook = xlrd.open_workbook('sample.xlsx')

#Get the sheet name and print
sheet_names = xl_workbook.sheet_names()
print('Sheet Names: ', sheet_names)

#Getting the sheet name by index and printing
xl_sheet = xl_workbook.sheet_by_index(0)
print('Sheet Name: ', xl_sheet.name )
tmp = ""
#printing the row value by index
for i in range (0, xl_sheet.nrows):
    row = xl_sheet.row(i)
    print('*'*40)
    for idx, cell_obj in enumerate(row):
        print(i, idx)
        a = str((xl_sheet.cell(i,idx).value))
        print(a)
        tmp = tmp + a
    print(tmp)
        #cell_type_str = ctype_text.get(cell_obj.ctype, 'Unknown type')
        #print('(%s) %s %s' %(idx, cell_type_str, cell_obj.value) )
    print(cell_obj.value)


print(xl_sheet.ncols)
print(xl_sheet.nrows)

#printing the value of the cell
#for i in range(0,xl_sheet.nrows):
#    for j in range (0, xl_sheet.ncols):
#        b = xl_sheet.cell(i,j)
#        c = str(b.value)
#        print(c)




#num_cols = xl_sheet.ncols
#concatenate = ""



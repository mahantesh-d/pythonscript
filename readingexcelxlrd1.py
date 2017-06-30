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

#printing the row value by index
row = xl_sheet.row(2)
print('(Column#) type:value')
for idx, cell_obj in enumerate(row):
    cell_type_str = ctype_text.get(cell_obj.ctype, 'Unknown type')
    print('(%s) %s %s' %(idx, cell_type_str, cell_obj.value) )

#printing the value of the cell
b = xl_sheet.cell(0,0)
print(b.value)
num_cols = xl_sheet.ncols

#Iterating over the row and column
for row_idx in range(0, xl_sheet.ncols):
    print('_'*40)
    print('Rows: %s' %row_idx)
    for col_idx in range(0, num_cols):
        cell_obj = xl_sheet.cell(row_idx, col_idx)
        print('Column: [%s] cell_obj: [%s]' %(col_idx, cell_obj))


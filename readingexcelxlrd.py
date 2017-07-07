import xlrd
book = xlrd.open_workbook('sample.xlsx')

max_nb_row = 0
for sheet in book.sheets():
    max_nb_row = max(max_nb_row, sheet.nrows)

for row in range(max_nb_row) :
    print(row)
    for sheet in book.sheets() :
       if row < sheet.nrows :
           print(sheet.nrows)
           a = str(sheet.row(row))
           print(a)
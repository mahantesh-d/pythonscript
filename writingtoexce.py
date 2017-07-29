import xlsxwriter
import time

a = str(time.asctime(time.localtime(time.time()))).replace(" ", "").replace(":", "") #Creating the file name
print(a)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('%s.xlsx'%a)
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

# Some data we want to write to the worksheet.
expenses = [                                    #Create the list to write into the file
    ('https://httpbin.org/get', 200, '269'),
    ('https://httpbin.org/get', 200, '269'),
    ('https://httpbin.org/get', 200, '269'),
    ('https://httpbin.org/get', 200, '269'),
    ('https://httpbin.org/get', 200, '269')
]
format = workbook.add_format({'bold': True, 'font_color': 'red'})
worksheet.write('A1', 'URL', format)
worksheet.write('B1', 'Status Code', format)
worksheet.write('C1', 'Content_length', format)
# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for url, status_code, content_length in (expenses):
    worksheet.write(row, col, url)
    worksheet.write(row, col + 1, status_code)
    worksheet.write(row, col + 2, content_length)
    row += 1

# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

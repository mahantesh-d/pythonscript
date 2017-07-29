import xlrd  # package for reading the excel
from operator import itemgetter
import requests
import xlsxwriter
import time

book = xlrd.open_workbook('metadata.xlsx')

getSheet = book.sheet_by_index(0)


fetchedData = []
createURL = []
aaa = []
def printtttt(abcbd):
    print('abcd',abcbd, end="")
def printlist(getlist):
    print('getlist',getlist)
    result = []
    for item in getlist:
        print('items',item)
        result.extend(item)
    printtttt(result)
# *********************************"Writing Result to the excel"****************************
def writeToExcel(listResult):
    generateFileName = str(time.asctime(time.localtime(time.time()))).replace(" ", "").replace(":","")  # Creating the file name

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('%s.xlsx' % generateFileName)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    format = workbook.add_format({'bold': True, 'font_color': 'red'})
    worksheet.write('A1', 'URL', format)
    worksheet.write('B1', 'Status Code', format)
    worksheet.write('C1', 'Content_length', format)
    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for url, status_code, content_length in (listResult):
        worksheet.write(row, col, url)
        worksheet.write(row, col + 1, status_code)
        worksheet.write(row, col + 2, content_length)
        row += 1
    workbook.close()

listResult = []
# *******************************"Sending the GET Request"******************************
def getRequest(url):
    try:
        rrr = []
        rr = requests.get(url)
        listResult.append((rr.url, rr.status_code, rr.headers.get('Content-Length')))
        for item in listResult:
            rrr = item + tuple(listResult)
        #bbb = ((rr.url, rr.status_code, rr.headers.get('Content-Length')))
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        exit(1)
    #print('not doing well',listResult)
    print('%%%%%%%%%%%%',rrr, end="")
    printlist(listResult)

# **********************************"Reading the metadata from excel********************************"
maxRows = getSheet.nrows
for i in range(1, maxRows):  # Iterating over the rows and getting the values
    aa = getSheet.row_values(i)[4]
    if aa == 'Active':
        bb = getSheet.row_values(i)[5]
        if bb == 'POST':
            #print('POST')
            dd = str("".join(itemgetter(0, 1, 2)(getSheet.row_values(i))))  # Combining the the values of the list)
            makeURL = 'http://' + dd
            #print('makeURL', makeURL)
            getRequest(makeURL)
        else:
            #print('GET')
            dd = str("".join(itemgetter(0, 1, 2)(getSheet.row_values(i))))  # Combining the the values of the list)
            makeURL = 'http://' + dd
            #print('makeURL', makeURL)
            getRequest(makeURL)
    else:
        print(getSheet.row_values(i))


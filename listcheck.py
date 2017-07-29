import xlrd
from operator import itemgetter

book = xlrd.open_workbook('metadata.xlsx')
getSheet = book.sheet_by_index(0)


def printURL(URL):
    conresult = []
    for i in URL:
        b = 'con' + i
        conresult.append(b)
    print(conresult)


listResult = []
maxRows = getSheet.nrows

for i in range(1, maxRows):  # Iterating over the rows and getting the values
    aa = getSheet.row_values(i)[4]
    if aa == 'Active':
        bb = getSheet.row_values(i)[5]
        if bb == 'POST':
            dd = str("".join(itemgetter(0, 1, 2)(getSheet.row_values(i))))  # Combining the the values of the list)
            makeURL = 'http://' + dd
            listResult.append(makeURL)

        else:
            dd = str("".join(itemgetter(0, 1, 2)(getSheet.row_values(i))))  # Combining the the values of the list)
            makeURL = 'http://' + dd
            listResult.append(makeURL)
    else:
        print(getSheet.row_values(i))
printURL(listResult)

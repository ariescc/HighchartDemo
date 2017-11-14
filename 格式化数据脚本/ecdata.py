import xlrd
import re


def read_xls():
    workbook = xlrd.open_workbook('visits.xlsx')
    booksheet = workbook.sheet_by_name('Sheet1')
    p = list()
    for row in range(booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            if type(val) == float:
                val = int(val)
            row_data.append(val)
        p.append(row_data)
    return p

def write_file(list):
    res = ''
    for item in range(349):
        tmp = '{day: ' + str(item) + ',visits: ' + str(list[0][item]) + '},' + '\n'
        res += tmp

    with open('output.txt', 'w') as file:
        file.write(res);

if __name__ == '__main__':
    write_file(read_xls())
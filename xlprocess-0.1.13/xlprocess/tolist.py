import re

from xlprocess.xlsxlist import xlsxtolist, xlsxalltolist

from xlprocess.xlslist import xlstolist, xlsalltolist


def tolist(filename='', sheetnum=-1):
    if re.search('.xlsx$', filename):
        if sheetnum == -1:
            return alltolist(filename)
        else:
            return [xlsxtolist(filename, sheetnum)]
    elif re.search('.xls$', filename):
        if sheetnum == -1:
            return xlsalltolist(filename)
        else:
            return [xlstolist(filename, sheetnum)]
    else:
        print('Format not support')


def alltolist(filename=''):
    if re.search('.xlsx$', filename):
        return xlsxalltolist(filename)
    elif re.search('.xls$', filename):
        return xlsalltolist(filename)
    else:
        print('Format not support')

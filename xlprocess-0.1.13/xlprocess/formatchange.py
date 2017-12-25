import csv
import re

from xlprocess.tolist import tolist, alltolist
from xlprocess.xlsxlist import listtoxlsx
from xlprocess.xlslist import listtoxls
from xlprocess.listprocess import removesheetform


def setfilename(filename=''):
    if re.search('.xlsx$', filename):
        return filename[:-5]
    elif re.search('.xls$', filename):
        return filename[:-4]


def tocsv(filename='', sheetnum=-1):
    if sheetnum == -1:
        datas = removesheetform(alltolist(filename))
    else:
        datas = tolist(filename, sheetnum)
    filename = setfilename(filename) + '.csv'
    with open(filename, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(datas)


def toxlsx(filename='', sheetnum=-1):
    if sheetnum == -1:
        datas = alltolist(filename)
    else:
        datas = []
        datas.append(tolist(filename, sheetnum))
    filename = setfilename(filename) + '.xlsx'
    listtoxlsx(filename, datas)


def filetype(xlsx=True, filename='', datas=[]):
    if xlsx:
        filename = setfilename(filename) + '.xlsx'
        listtoxlsx(filename, datas)
    else:
        subfilename = setfilename(filename) + '.xls'
        listtoxls(subfilename, datas)
# tocsv('data/test1.xlsx')
# toxlsx('data/test1.xls')

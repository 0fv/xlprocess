from xlprocess.xlsxlist import listtoxlsx
from xlprocess.xlslist import listtoxls
from xlprocess.tolist import alltolist
from os import listdir


# combine in put filename
def combination(xlsx=True, *filenames):
    alist = []
    for filename in filenames:
        list1 = alltolist(filename)
        if list1 != None:
            alist = alist + list1
    alist = testsameheetname(alist)
    if xlsx:
        listtoxlsx('comfile.xlsx', alist)
    else:
        listtoxls('comfile.xls', alist)


def fcombination(xlsx=True, dir=''):
    filelist = listdir(dir)
    alist = []
    for file in filelist:
        filedir = dir + '/' + file
        print(filedir)
        list1 = alltolist(filedir)
        if list1 != None:
            alist = alist + list1
    alist = testsameheetname(alist)
    if xlsx:
        listtoxlsx('comfile.xlsx', alist)
    else:
        listtoxls('comfile.xls', alist)


# combination('data/test.xlsx','data/test1.xls')
def splitfile(xlsx=True, filename=''):
    datas = alltolist(filename)
    for data in datas:
        dat = [data]
        if xlsx:
            subfilename = data[0] + '.xlsx'
            listtoxlsx(subfilename, dat)
        else:
            subfilename = data[0] + '.xls'
            listtoxls(subfilename, dat)
# splitfile('comfile.xlsx')


def testsameheetname(olist=[[]]):
    name = []
    count = 1
    for a in range(len(olist)):
        if olist[a][0] not in name:
            name.append(olist[a][0])
        else:
            olist[a][0] = olist[a][0] + '(renamed' + '' + str(count) + ')'
            count = count + 1
    return olist

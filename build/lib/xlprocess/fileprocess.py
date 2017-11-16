from xlprocess.xlsxlist import listtoxlsx
from xlprocess.xlslist import listtoxls
from xlprocess.tolist import alltolist


def combination(xlsx=True,*filenames):
    alist=[]
    for filename in filenames:
        list1= alltolist(filename)
        if list1 != None:
            alist=alist+list1
    if xlsx:
        listtoxlsx('comfile.xlsx',alist)
    else:
        listtoxls('comfile.xls', alist)
#combination('data/test.xlsx','data/test1.xls')
def splitfile(filename):
    datas=alltolist(filename)
    for data in datas:
        subfilename=data[0]+'.xlsx'
        dat=[data]
        listtoxlsx(subfilename,dat)
#splitfile('comfile.xlsx')
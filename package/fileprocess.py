from xlsxlist import listtoxlsx

from package.tolist import alltolist


def combination(*filenames):
    alist=[]
    for filename in filenames:
        alist=alist+alltolist(filename)
    listtoxlsx('comfile.xlsx',alist)
#combination('data/test.xlsx','data/test1.xls')
def splitfile(filename):
    datas=alltolist(filename)
    for data in datas:
        subfilename=data[0]+'.xlsx'
        dat=[data]
        listtoxlsx(subfilename,dat)
#splitfile('comfile.xlsx')
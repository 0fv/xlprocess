from xlprocess.formatchange import setfilename
from xlprocess.xlsxlist import listtoxlsx

from xlprocess.tolist import alltolist, tolist


def rowtltie(filename='',sheetnum=-1,title=1):
    if sheetnum==-1:
        datas=alltolist(filename)
    else:
        datas=[tolist(filename,sheetnum)]
    adata =[]
    for data in datas:
        data1=[]
        for row in data[:title]:
            data1.append(row)
        rtitle=data[title]
        for row in data[title+2:]:
            data1.append(rtitle)
            data1.append(row)
        adata.append(data1)
    filename=setfilename(filename)+'2.xlsx'
    listtoxlsx(filename,adata)
rowtltie('data/test1.xls',title=3)

def groupby(filename,sheetnum=-1,*col):
    datas=tolist(filename,sheetnum)
    adata=[]
    for data in datas:
        data1=[]
        data1.append(data[0])
        for row in data[1:]:
            rowa=[]
            for a in range(len(row)):
                if  (a+1) in col:
                    rowa.append(row[a])
            if data1==[]:
                data1.append(rowa)
            else:
                datawithoutnum=[]
                for row in data1:
                    datawithoutnum.append(row[:-1])
                if rowa[:-1] in datawithoutnum:
                    p=datawithoutnum.index(rowa[:-1])
                    data1[p][-1]=data1[p][-1]+rowa[-1]
                else:
                    data1.append(rowa)
        adata.append(data1)
    filename = setfilename(filename) + '(groupby).xlsx'
    listtoxlsx(filename,adata)
#groupby('data/test1.xls',0,1,2,3)






from xlprocess.formatchange import filetype, setfilename
from xlprocess.tolist import alltolist, tolist


def rowtltie(xlsx=True, filename='', sheetnum=-1, title=1):
    if sheetnum == -1:
        datas = alltolist(filename)
    else:
        datas = [tolist(filename, sheetnum)]
    adata = []
    for data in datas:
        data1 = []
        for row in data[:title]:
            data1.append(row)
        rtitle = data[title]
        for row in data[title + 2:]:
            data1.append(rtitle)
            data1.append(row)
        adata.append(data1)
    filetype(xlsx, filename, adata)


def groupby(xlsx=True, filename='', sheetnum=-1, *col):
    datas = tolist(filename, sheetnum)
    adata = []
    for data in datas:
        data1 = []
        data1.append(data[0])
        for row in data[1:]:
            rowa = []
            for a in range(len(row)):
                if (a + 1) in col:
                    rowa.append(row[a])
            if data1 == []:
                data1.append(rowa)
            else:
                datawithoutnum = []
                for row in data1:
                    datawithoutnum.append(row[:-1])
                if rowa[:-1] in datawithoutnum:
                    p = datawithoutnum.index(rowa[:-1])
                    data1[p][-1] = data1[p][-1] + rowa[-1]
                else:
                    data1.append(rowa)
        adata.append(data1)
    filename = setfilename(filename) + '(groupby).xlsx'
    filetype(xlsx, filename, adata)
# groupby('data/test1.xls',0,1,2,3)

def classify(xlsx=True,filename='filename',sheetnum=-1,*col):
    datas=tolist(filename,sheetnum)
    sheetnames=[]
    adata=[]
    for data in datas:
        for row in data[1:]:
            sheetname=''
            for co in col:
                sheetname +=row[co-1]
            if sheetname not in sheetnames:
                sheetnames.append(sheetname)
    for sheetname in sheetnames:
        avalues=[]
        avalues.append(sheetname)
        for data in datas:
            for row in data[1:]:
                sheetname1 = ''
                for co in col:
                    sheetname1 += row[co - 1]
                if sheetname1 ==  sheetname:
                    avalues.append(row)
        adata.append(avalues)
    filetype(xlsx, filename, adata)
#classify(True,'123.xlsx',-1,1,2)



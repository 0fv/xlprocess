import xlrd
import xlwt

def xlstolist(filename='',sheetnum=0):
        wb = xlrd.open_workbook(filename)
        sheet = wb.sheets()[sheetnum]
        datas=[]
        datas.append(wb.sheet_names()[sheetnum])
        for row in range(sheet.nrows):
            datas.append(sheet.row_values(row))
        return datas


def xlsalltolist(filename=''):
    wb = xlrd.open_workbook(filename)
    sheetnum=len(wb.sheets())
    datas1=[]
    for a in range(sheetnum):
        sheet = wb.sheets()[a]
        datas = []
        datas.append(wb.sheet_names()[a-1])
        for row in range(sheet.nrows):
            datas.append(sheet.row_values(row))
        datas1.append(datas)
    return datas1

def listtoxls(filename='' ,sheets=[[]]):
        wb = xlwt.Workbook()
        for sheet in sheets:
                table=wb.add_sheet(sheet[0],cell_overwrite_ok=True)
                for a in range(1,len(sheet)):
                        for b in range(len(sheet[a])):
                                table.write(a-1,b,sheet[a][b])
        wb.save(filename)
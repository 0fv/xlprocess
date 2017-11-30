import xlrd
import xlwt


def xlstolist(filename='', sheetnum=0):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheets()[sheetnum]
    datas = []
    datas.append(wb.sheet_names()[sheetnum])
    for row in range(sheet.nrows):
        datas.append(sheet.row_values(row))
    return datas


def xlsalltolist(filename=''):
    wb = xlrd.open_workbook(filename)
    sheetnum = len(wb.sheets())
    datas1 = []
    for a in range(sheetnum):
        sheet = wb.sheets()[a]
        datas = []
        datas.append(wb.sheet_names()[a - 1])
        for row in range(sheet.nrows):
            datas.append(sheet.row_values(row))
        datas1.append(datas)
    return datas1


def listtoxls(filename='', sheets=[[]]):
    wb = xlwt.Workbook()
    renametime = 1
    name = []
    for sheet in sheets:
        sheetname = sheet[0]
        if sheetname in name:
            sheetname = sheetname + 'renamed' + '(' + str(renametime) + ')'
            renametime = renametime + 1
        table = wb.add_sheet(sheetname, cell_overwrite_ok=True)
        for a in range(1, len(sheet)):
            for b in range(len(sheet[a])):
                table.write(a - 1, b, sheet[a][b])
        name.append(sheetname)
    wb.save(filename)

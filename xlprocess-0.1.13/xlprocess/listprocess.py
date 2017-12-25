def removesheetform(datas=[[]]):
    datar = []
    datar.append(datas[0][0])
    for data in datas:
        for dat in data[1:]:
            datar.append(dat)
    return datar

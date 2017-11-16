# xlprocesstoolbox
Find a way to process excel esaily,base on  openpyxl,xlrd,xlwt.support *.xls,**.xlsx*
## Install
```
pip3 install xlprocess
```
## Format change
###  Change format to csv
- formatchange.tocsv(filename,sheetnum=-1)

- \-1 mean include every sheet.
### Change format to xlsx
- formatchange.toxlsx(filename,sheetnum=-1)

- \-1 mean include every sheet.
## Combination file
- fileprocess.combination(xlsx=True,file1,file2,file3...) 

Default return a new file named 'comfile.xlsx',but when the character in cell is too long openpylx might throw IllegalCharacterError exception.In this condition,you can change xlsx parameter to False.But in this case,you should make sure every sheet's name is different.
## Split one file accroding sheet's name
-  fileprocess.filesplit(xlsx=True,'filename')
### Generate row title
- sheeetprocess.rowtltie(xlsx=True,'filename',sheetnum=-1,title=1)
### Groupby
- sheetprocess.groupby(xlsx=True,filename,sheetnum=-1,*col)

- Last of *col mean quantity.For example,groupby(True,'data/test1.xls',0,1,2,3),mean accounting the third column 

## License

The MIT License

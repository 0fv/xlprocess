# xlprocesstoolbox
Find a way to process excel esaily,base on  openpyxl,xlrd,xlwt.support *.xls,**.xlsx*
## Format change
###  Change format to csv
- fornatchange.tocsv(filename,sheetnum=-1)

- \-1 mean include every sheet.
### Change format to xlsx
- formatchange.toxlsx(filename,sheetnum=-1)

- \-1 mean include every sheet.
## Combination file
- fileprocess.combination(file1,file2,file3...) 

return a new file named 'comfile.xlsx'
## Split one file accroding its sheet's name
-  fileprocess.filesplit('filename')

sheetname is file name
## Sheet process
### Generate row title
- sheeetprocess.rowtltie('filename',sheetnum=-1,title=1)
### Groupby
- sheetprocess.groupby(filename,sheetnum=-1,*col)

- Last of *col mean quantity.For example,groupby('data/test1.xls',0,1,2,3),mean accounting the third column 

## License

The MIT License

import xlwt
import xlrd

# #write excel
book = xlwt.Workbook( encoding = 'utf-8', style_compression = 0 )

font = xlwt.Font()
font.colour_index = 2
font.bold= True



style = xlwt.XFStyle()
style.font = font




sheet = book.add_sheet( 'dede', cell_overwrite_ok = True )

sheet.write( 0, 0, 'Test', style )

book.save( 'h:\ddd.xls' )

# xlsfile = ".\data.xls"
#
# book = xlrd.open_workbook(xlsfile)
# sheet_name = book.sheet_names()[0]
# print(sheet_name)
#
# sheet = book.sheet_by_index(0)
#
# nrows = sheet.nrows
# ncols = sheet.ncols
#
# row_data = sheet.row_values(1)
# col_data = sheet.col_values(0)
#
#
#
# print(row_data)
# print(col_data)

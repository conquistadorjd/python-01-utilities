#####################################################################################################################################################
# This program reads file from one excel																										#
# Make changes into sheet  																															#
# Write sheet data into newexcel 																													#
#####################################################################################################################################################
import xlrd
import xlwt
######################################################### Reading file
workbook=xlrd.open_workbook("foobar.xls")
sheet=workbook.sheet_by_name("sheetName")
print sheet.nrows
print sheet.ncols
# print sheet.cell_value(0,0)
data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
# data = [sheet.cell_value(row, col) for row in range(sheet.nrows) for col in range(sheet.ncols) ]
print "*"*10 , 'Before Loop'
##################################### XXXXXXXXXXXXXXXXXXXXXXXXXXXXx this loop is not working
# for row in range(sheet.nrows):
# 	for col in range(sheet.ncols):
# 		print sheet.cell_value(row, col)
# 		print type(sheet.cell_value(row, col))
# 		# data[row,col] = sheet.cell_value(row, col)

# print data

######################################################### Creating output file
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

######################################################### Moving data into sheet
for index, value in enumerate(data):
    sheet.write(0, index, value)

# sheet.write(0, 2, 'foobar updated again') 

workbook.save("output.xls")
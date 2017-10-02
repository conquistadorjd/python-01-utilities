import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheetName")
sheet.write(0, 0, 'foobar') 

workbook.save("foobar.xls")
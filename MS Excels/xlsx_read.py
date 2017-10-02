import xlrd

workbook=xlrd.open_workbook("nsesymbols.xlsx")
sh=workbook.sheet_by_name("EQUITY_L")
print sh.nrows
print sh.ncols

print sh.cell_value(1,2)
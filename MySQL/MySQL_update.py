import xlrd
import mysql.connector

#################################################################################Read from excel
workbook=xlrd.open_workbook("flipkart-amazon-mapping final.xls")
sh=workbook.sheet_by_name("Working Copy")
print sh.nrows
print sh.ncols

cnx = mysql.connector.connect(
          host= "localhost",
          user="root",
          passwd="root",
          db="root")
cursor = cnx.cursor()

print " ***** cursor Opened"
################################################################################# loop
for rownum in range(1, sh.nrows):
	print sh.cell_value(rownum,0), sh.cell_value(rownum,1) , sh.cell_value(rownum,2) , sh.cell_value(rownum,3)

	sql = "UPDATE  m100_mobilesdatamain set m100_amazon_asin = %s, m100_amazon_title = %s where m100_flipkart_productId = %s"
	print sql
	values = ( sh.cell_value(rownum,2) ,sh.cell_value(rownum,3), sh.cell_value(rownum,0))
	print values
	try:
	    cursor.execute(sql,values)
	    cnx.commit()
	except mysql.connector.Error as err:
	    print("*****Something went wrong: {}".format(err))
	    cnx.rollback()

cnx.close()
print " ***** Cursor closed"
#####################################################################################################
# MySQL Select Query: Please chaneg tjhe database and table details for it to work
#####################################################################################################
import json
import mysql.connector
import xlrd
import urllib2

##################################################################################################### connect to Database
cnx = mysql.connector.connect(
                  # host= "localhost",
                  host = 'mysql-rfam-public.ebi.ac.uk',
                  user="rfamro",
                  passwd="",
                  db="Rfam",
                  port=4497
                  )
cursor = cnx.cursor()

##################################################################################################### Get Data from table
sql = "select * from family"
values = ( )

try:
    cursor.execute(sql,values)
    rows = cursor.fetchall()
    for item in rows:
    	print item
except mysql.connector.Error as err:
    print("*****Something went wrong: {}".format(err))
    cnx.rollback()
   

cnx.close()
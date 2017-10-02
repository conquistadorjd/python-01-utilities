import xlrd
from collections import OrderedDict
import simplejson as json
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('c.xlsx')
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
cars_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['BANK'] = row_values[0]
    cars['IFSC'] = row_values[1]
    cars['MICR'] = row_values[2]
    cars['BRANCH'] = row_values[3]
    cars['ADDRESS'] = row_values[4]
    cars['CONTACT'] = row_values[5]
    cars['CITY'] = row_values[6]
    cars['DISTRICT'] = row_values[7]
    cars['STATE'] = row_values[8]

 
    cars_list.append(cars)
 
# Serialize the list of dicts to JSON
j = json.dumps(cars_list)
 
# Write to file
with open('finalData.json', 'w') as f:
    f.write(j)
import gspread
import os
from pyhocon import ConfigFactory 
import time
import pyhocon
gc = gspread.oauth()

# Open a sheet from a spreadsheet in one go
sheet = gc.open("IRIS_ICD")
# # Update a range of cells using the top left corner address
# wks.update('A1', [[1, 2], [3, 4]])

# # Or update a single cell
# wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header


subsystem_list=['TCS','ESW','AOESW','NFIRAOS','IRIS','ESEN','M1CS']
#subsystem_list=['ESEN']
events=[]
for subsystem in subsystem_list:
	
	wks = sheet.worksheet(subsystem)
	subsystem_list= wks.col_values(1)
	component_list= wks.col_values(2)
	name_list=wks.col_values(3)
	for i in range(len(name_list)):
	    flag=wks.cell(i+1, 4).value
	    time.sleep(1)
	    if 'Add' in flag:
		dict_name= {'name':name_list[i],'subsystem':subsystem_list[i],'component':component_list[i]}
		events.append(dict_name)
		print subsystem_list[i],' ',component_list[i],' ',name_list[i]
		
	#config = pyhocon.ConfigTree()
config={'events':events}

fname='subscribe-model.conf'
with open(fname,"w") as outfile: 
    outfile.write(pyhocon.HOCONConverter.to_hocon(config))
fin = open(fname, "rt")
data = fin.read()
data = data.replace('u\'', '')
data = data.replace('\'', '')
data = data.replace(', ', '\n')
data = data.replace('{', '\n{\n')
data = data.replace('}', '\n}\n')
data = data.replace(':', '=')
fin.close()
fin = open(fname, "wt")
fin.write(data)
fin.close()    
	
	


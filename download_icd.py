import gspread
import os
from pyhocon import ConfigFactory 
import time
gc = gspread.oauth()

# Open a sheet from a spreadsheet in one go
sheet = gc.open("IRIS_ICD")
# # Update a range of cells using the top left corner address
# wks.update('A1', [[1, 2], [3, 4]])

# # Or update a single cell
# wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header


subsystem_list=['TCS','ESW','AOESW','NFIRAOS','IRIS','ESEN','M1CS']
#subsystem_list=['IRIS']

for subsystem in subsystem_list:
	
	p_arr=[]
	wks = sheet.add_worksheet(title=subsystem, rows="300", cols="20")
	for root, subdirs, files in os.walk(subsystem+'-Model-Files'):
	    fname=root+'/'+'publish-model.conf'
	    try:
		if os.path.isfile(fname)==True:
		    conf = ConfigFactory.parse_file(fname)
		    subsys = conf['subsystem']
		    component = conf['component']
		    #print 'comp',component
		    for ind in range(len(conf['publish.events'])):
			#print subsys,' ',component,' ',conf['publish.events'][ind]['name']
			p_arr.append([subsys,component,conf['publish.events'][ind]['name']])
			# wks.update_cell(iter, 1, subsys)
			# wks.update_cell(iter, 2, component)
			# wks.update_cell(iter, 3, conf['publish.events'][ind]['name'])
			#time.sleep(3)
						
	    except:		
		continue
	
	iter=1    
	for entry in p_arr:
		wks.update_cell(iter, 1, entry[0])
		wks.update_cell(iter, 2, entry[1])
		wks.update_cell(iter, 3, entry[2])
		print entry[0],' ',entry[1],' ',entry[2]
		iter=iter+1
		time.sleep(3)
		
	
	# component_list=os.listdir(subsystem+'-Model-Files')    
	# for component in component_list:
		# fname=subsystem+'-Model-Files'+'/'+component+'/'+'publish-model.conf'
		# if os.path.isfile(fname)==True:
		    # conf = ConfigFactory.parse_file(fname)
		    # for ind in range(len(conf['publish.events'])):
			# print subsystem,' ',component,' ',conf['publish.events'][ind]['name']
			# #wks.update_cell(iter, 1, subsystem)
			# #wks.update_cell(iter, 2, component)
			# #wks.update_cell(iter, 3, conf['publish.events'][ind]['name'])
			# time.sleep(3)
			# iter=iter+1
			

# IRIS ICD Update using Google Sheets
Code to update ICD model Files from Sheets Interface

The directory structure assumed for this tool. is as below.

root directory/
├── download_icd.py
├── upload_subscribe.py
├── TCS-Model-Files/
├── ESW-Model-Files/
├── AOESW-Model-Files/
├── NFIRAOS-Model-Files/
├── IRIS-Model-Files/
├── ESEN-Model-Files/
├── M1CS-Model-Files/

##Requirements
The tool uses gspread library
https://github.com/burnash/gspread

The authentication method used is oauth. The details of setting up authentication of sheets for read and write are explained in the gspread page.

pyhocon library
##Download ICD
The download_icd.py expects the model file repos to be already cloned in the corresponding subdirectories. It creates different worksheets for each assembl with subsystem and corresponding published item.

##Upload Subscribe
The upload subscribe expects the thirs column in the sheets to be filles with 'Add' for the items that need to be added to the subscribe.conf file to be produced. According to the input the hocon file is generated.


import xlrd
import xlsxwriter
import os

#load File
data = input("Exac File Path: ")
if os.path.isfile(data):
    try: 
        wb = xlrd.open_workbook(data)
        sheet = wb.sheet_by_index(0)
    except: 
        print("Unable to open ExAC Excel File")
 else: 
     print("File path specified is not valid")

#create file that will hold the final visualized data
def findLast(path, character):
    return path.rfind(character)

formatFile = xlsxwriter.Workbook(os.getcwd() + "/FORMATTED" + data[findLast(data, '/') + 1: ])
formatSheet = formatFile.add_worksheet()

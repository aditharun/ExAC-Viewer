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

#figure out which mutation types to consider
mutations = list(sys.argv[2])
dict_mutations = {'1': 'all', '2': 'missense', '3': 'non coding transcript exon', '4': 'frameshift', '5': "5' UTR", '6': "3' UTR", '7': 'synonymous', '8': 'splice', '9': 'intron'}
def mutationMap(dict_mutations, mutations):
    for item in mutations:
        if item =='1':
        	mutations.append(dict_mutations[item])
        	return
        if item in dict_mutations.keys():
            mutations.append(dict_mutations[item])

            
mutationMap(dict_mutations, mutations)
mutations = [x for x in mutations if not (x.isdigit())]

#columns with pertinent information
colList = [6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 , 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#rows to get (frequency greater than 1 and satisfies mutations to consider criteria)

rowListFreq = []
for x in range(sheet.nrows):
    try: 
        if float(sheet.cell_value(x, 11)) > 1.0:
            rowListFreq.append(x)
    except: 
        pass

#pick rows that satisfy mutations to consider criteria
rowListMut = []
if mutations[0] != 'all': 
    for y in range(len(mutations)):
        print (mutations[y])
        for x in range(sheet.nrows):
            if mutations[y].split(" ")[0] == sheet.cell_value(x, 9).split()[0]:
                rowListMut.append(x)
                
rowList = list(set(rowListFreq).intersection(rowListMut))

#create file for final visualized data
def findLast(path, character):
    return path.rfind(character)

formatFile = xlsxwriter.Workbook(os.getcwd() + "/FORMATTED" + data[findLast(data, '/') + 1: ])
formatSheetChart = formatFile.add_worksheet()
formatSheetFreq = formatFile.add_worksheet()

#populate output with necessary data
for x in range(len(rowList)):
    for y in range(len(colList)):
        formatSheetChart.write(x, y, sheet.cecolList[y]))ll_value(rowList[x], 

formatFile.close()

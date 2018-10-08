import xlrd
import xlsxwriter
import os
import sys

#load File
data = sys.argv[1]
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
colList = [6, 7, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23 , 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

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
if 'all' not in mutations: 
    for y in range(len(mutations)):
        for x in range(sheet.nrows):
            if mutations[y].split(" ")[0] == sheet.cell_value(x, 9).split()[0]:
                rowListMut.append(x)

if 'all' in mutations: 
    for x in range(sheet.nrows):
        rowListMut.append(x)
                
rowList = list(set(rowListFreq).intersection(rowListMut))

#create file for final visualized data
def findLast(path, character):
    return path.rfind(character)

formatFile = xlsxwriter.Workbook(os.getcwd() + "/FORMATTED" + data[findLast(data, '/') + 1: ])
formatSheetChart = formatFile.add_worksheet()
formatSheetFreq = formatFile.add_worksheet()

#populate output with necessary data
ethnic = ['Overall', 'African', 'E.Asian', 'Euro(NF)', 'Finnish', 'Latino', 'Other', 'S.Asian']
ethnicCount = 0

#cell_format method does not allow for iteration, and the add format method is a pseudodictionary, not an actual dictionary, one cannot rekey values. This lead to the ugly code below until line 98. 

cell_formatEthnic = formatFile.add_format({'bold': True, 'font_size': 14})

cell_formatColor1 = formatFile.add_format()
cell_formatColor2 = formatFile.add_format()
cell_formatColor3 = formatFile.add_format()
cell_formatColor4 = formatFile.add_format()
cell_formatColor5 = formatFile.add_format()
cell_formatColor6 = formatFile.add_format()
cell_formatColor7 = formatFile.add_format()
cell_formatColor8 = formatFile.add_format()
color = ['blue', 'red', 'black', 'green', 'orange', 'cyan', 'pink', 'purple']

cell_formatColor1.set_bg_color(color[0])
cell_formatColor2.set_bg_color(color[1])
cell_formatColor3.set_bg_color(color[2])
cell_formatColor4.set_bg_color(color[3])
cell_formatColor5.set_bg_color(color[4])
cell_formatColor6.set_bg_color(color[5])
cell_formatColor7.set_bg_color(color[6])
cell_formatColor8.set_bg_color(color[7])

for x in range(3):
    formatSheetChart.write(1, 3 + x, None, cell_formatColor1)
    formatSheetChart.write(1, 6 + x, None, cell_formatColor2)
    formatSheetChart.write(1, 9 + x, None, cell_formatColor3)
    formatSheetChart.write(1, 12 + x, None, cell_formatColor4)
    formatSheetChart.write(1, 15 + x, None, cell_formatColor5)
    formatSheetChart.write(1, 18 + x, None, cell_formatColor6)
    formatSheetChart.write(1, 21 + x, None, cell_formatColor7)
    formatSheetChart.write(1, 24 + x, None, cell_formatColor8)

cell_formatFreq = workbook.add_format({'bold': True, 'font_size': 12, 'font_color': 'blue' })
cell_formatEFreq = workbook.add_format({'bold': True, 'font_size': 12})

#generate ethnicity header
for z in range(len(colList)): 
    if z == 4 + 3*ethnicCount: 
        formatSheetChart.write(0, z, ethnic[ethnicCount], cell_formatEthnic)
        formatSheetFreq.write(0, ethnicCount + 1, ethnic[ethnicCount], cell_formatFreq)
        ethnicCount = ethnicCount + 1

    formatSheetChart.write(2, z, sheet.cell_value(0,colList[z]))

#generate neatly formatted data in correct position and order
for x in range(len(rowList)):
    for y in range(len(colList)):
        formatSheetChart.write(x + 3, y , sheet.cell_value(rowList[x], colList[y]))

formatSheetFreq.write(0, 0, 'Change', cell_formatFreq)

cell_formatval = formatFile.add_format({'font_color': 'red'})

#generate frequency table with percent frequency of each mutation
for x in range(len(rowList)):
    formatSheetFreq.write(x + 1, 0, sheet.cell_value(rowList[x], 6), cell_formatEFreq)
    freq = 0
    for y in range(len(colList)):
        if colList[y] == 11: 
            val = 100 * (sheet.cell_value(rowList[x], colList[y]) / sheet.cell_value(rowList[x], colList[y + 1]))
            if val >= 1.0: 
            	formatSheetFreq.write(x + 1, 1 , val, cell_formatval)
            else: 
                formatSheetFreq.write(x + 1, 1 , val )
        if colList[y] == 15 + 3*freq:
            val = 100 * (sheet.cell_value(rowList[x], colList[y])/ sheet.cell_value(rowList[x], colList[y + 1]))
            if val >= 1.0:
            	formatSheetFreq.write(x + 1, freq + 2, val, cell_formatval)
            else: 
            	formatSheetFreq.write(x + 1, freq + 2, val)
            freq = freq + 1

#close excel workbook
formatFile.close()

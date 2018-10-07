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

#figure out which mutation types to consider
mutations = list(sys.argv[2])
dict_mutations = {'1: all', '2: missense', '3: non coding transcript exon', '4: frameshift', '5: 5' UTR', '6: 3' UTR', '7: synonymous', '8: splice', '9: intron'}def mutationMap(dict_mutations, mutations):
    for item in mutations:
        if item =='1':
        	mutations.append(dict_mutations[item])
        	return
        if item in dict_mutations.keys():
            mutations.append(dict_mutations[item])

            
mutationMap(dict_mutations, mutations)
mutations = [x for x in mutations if not (x.isdigit())]

#columns not to get
colList = [0, 1, 2, 3, 4, 5, 8, 10]

#rows to get (frequency greater than 1 and satisfies mutations to consider criteria)

rowList = []
for x in range(sheet.nrows):
    try: 
        if float(sheet.cell_value(x, 11)) > 1.0:
            rowList.append(x)
    except: 
        pass

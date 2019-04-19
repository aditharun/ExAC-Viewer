import sys
import xlrd
import xlsxwriter
import os


file = sys.argv[1]

if not os.path.isfile(file):
	print("not valid path")
	sys.exit()


#import csv file
wb = xlrd.open_workbook(file)
exac = wb.sheet_by_index(0)


#select mutation types you want, enter mutations you want as a string of numbers (e.x. 123)
mutations = list(sys.argv[2])
mutations = [ x for x in mutations if x.isdigit() ]

mutations.sort()

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

#default parameter is all mutations are considered
if not mutations:
	mutations = ['all']


#create ethnic breakdown w/ change as columns and rows as count, number, 
#Hzygote with color markings for each ethnicity

columns= [6,7,11,12,13,15,16, 17, 18, 19, 20, 21, 22, 23 , 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#get rows that are >1 and fit mutation criteria
rows = []
for x in range(exac.nrows):
	if isinstance(exac.cell_value(x,11), float) and float(exac.cell_value(x,11)) > 1.0:
		rows.append(x)

rows_mut = []
if 'all' not in mutations: 
    for y in range(len(mutations)):
        for x in range(exac.nrows):
            if mutations[y].split(" ")[0] == exac.cell_value(x, 9).split()[0]:
                rows_mut.append(x)
if 'all' in mutations:
	for x in range(exac.nrows):
		rows_mut.append(x)
set_row = list(set(rows).intersection(rows_mut))

chart = xlsxwriter.Workbook(os.getcwd() + "/SummaryChart.xlsx")
table = chart.add_worksheet()
frequency = chart.add_worksheet()

ethnic = ['Overall', 'African', 'E. Asian', 'Euro (NF)', 'Finnish', 'Latino', 'Other', 'S. Asian']
ethnic_format = chart.add_format({'bold': True, 'font_size': 12})

#write data into the new excel spreadsheet
t = 0
for x in range(len(columns)):
	table.write(2,0,"Change")
	table.write(2,1,"Consequence")
	if x % 3 == 1 and x != 0 and x != 1:
		table.write(2,x,"Hzygote")
	if x % 3 == 0 and x != 0 and x != 1:
		table.write(2,x,"Number")
		table.write(0,x,ethnic[t],ethnic_format)
		t = t + 1
	if x % 3 == 2 and x != 0 and x != 1:
		table.write(2,x,"Count")

for x in range(len(set_row)):
	for y in range(len(columns)):
		table.write(x+3,y,exac.cell_value(set_row[x], columns[y]))

#color formatting
color = ['blue', 'red', 'purple', 'green', 'orange', 'cyan', 'pink', 'lime']

cell_formatColor1 = chart.add_format()
cell_formatColor2 = chart.add_format()
cell_formatColor3 = chart.add_format()
cell_formatColor4 = chart.add_format()
cell_formatColor5 = chart.add_format()
cell_formatColor6 = chart.add_format()
cell_formatColor7 = chart.add_format()
cell_formatColor8 = chart.add_format()

cell_formatColor1.set_bg_color(color[0])
cell_formatColor2.set_bg_color(color[1])
cell_formatColor3.set_bg_color(color[2])
cell_formatColor4.set_bg_color(color[3])
cell_formatColor5.set_bg_color(color[4])
cell_formatColor6.set_bg_color(color[5])
cell_formatColor7.set_bg_color(color[6])
cell_formatColor8.set_bg_color(color[7])

#apply colors to spreadsheet
for x in range(3):
	table.write(1, 2 + x, None, cell_formatColor1)
	table.write(1, 5 + x, None, cell_formatColor2)
	table.write(1, 8 + x, None, cell_formatColor3)
	table.write(1, 11 + x, None, cell_formatColor4)
	table.write(1, 14 + x, None, cell_formatColor5)
	table.write(1, 17 + x, None, cell_formatColor6)
	table.write(1, 20 + x, None, cell_formatColor7)
	table.write(1, 23 + x, None, cell_formatColor8)


#create summary chart w/ change as column and ethnicity as subsequent columns with 
#percentage of allele frequency (count / number)
item_list = ['item', 5, 'foo', 3.14, True]
item_list = [e for e in item_list if e not in ('item', 5)]

rem = [6,7,13,17,20,23,26,29,32,35]
columns = list(set(columns).difference(rem))

frequency.write(0,0,"Change")
frequency.write(0,1,"Consequence")
for x in range(len(ethnic)):
	frequency.write(0,x+2,ethnic[x])

for x in range(len(set_row)):
	frequency.write(x+1,0,exac.cell_value(set_row[x],6))
	frequency.write(x+1,1,exac.cell_value(set_row[x],7))

for x in range(len(set_row)):
	for y in range(int(len(columns)/2)):
		allelefreq = float( exac.cell_value(set_row[x], columns[2*y]) ) / ( exac.cell_value(set_row[x], columns[(2*y) + 1]) )
		percentage = allelefreq * 100
		frequency.write(x + 1, y + 2, percentage)


chart.close()

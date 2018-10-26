import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from math import log
import re
import xlrd
import xlsxwriter

def grabFile(value):

	if os.path.isfile(value):
		init = True
		pointer = value
		return init, pointer 

	if os.path.isfile(os.getcwd() + "/" + value):
		init = True 
		pointer = os.getcwd() + "/" + value
		return init, pointer 

	else: 
		init = False
		pointer = "Null"
		return init, pointer 


def openFile(filepointer):
	with open(filepointer, 'r') as infile:
		return infile.readlines()

def removeGarbage(seq):
	regex = re.compile('[^a-zA-Z]')
	filtSeq = []
	for x in range(len(seq)):
		filtSeq.append(regex.sub('', seq[x]))
	filtSeq = "".join(filtSeq).upper()
	return  filtSeq

initialize = grabFile(sys.argv[1])[0]
if initialize:
	seqFilePointer = grabFile(sys.argv[1])[1]
	unfiltSeq = openFile(seqFilePointer)
	finalSeq = removeGarbage(unfiltSeq)

else: 
	exit()

sequence = list(finalSeq)


data = sys.argv[2]
if os.path.isfile(data):
    try: 
        wb = xlrd.open_workbook(data)
        sheet = wb.sheet_by_index(0)
    except: 
        print("Unable to open ExAC Excel File")
else: 
     print("File path specified is not valid")

rowlist = []
for x in range(sheet.nrows):
	if sheet.cell_value(x,9).split()[0] == 'missense':
		print(x)
		rowlist.append(x)

print(rowlist)

storevals = []

numbers = [0] * len(sequence)
#for each row in rowlist, find what the amino acid number is, and the frequency
for r in range(len(rowlist)):
	value = re.sub('[^0-9]', '', sheet.cell_value(rowlist[r], 5))
	try: 
		numbers[int(value) + 1] = log(sheet.cell_value(rowlist[r], 11) + 0.5)
		storevals.append(value)
	except: 
		pass




d = {'Residues': sequence, 'MutFreq': numbers}
df1 = pd.DataFrame(data = d)
print(df1)


ax = df1.plot.bar(x = 'Residues', y = 'MutFreq')
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')


count = 0 


for t in range(len(numbers)):
	for y in range(len(storevals)):
		if t == int(storevals[y]) + 1:
			if count % 5 == 0:
				ax.annotate(str(int(storevals[y]) + 1), xy = (t, numbers[t] + 0.1), fontsize = 8)
			count = count + 1



plt.ylabel("Log Allele Frequency")
plt.xlabel("Residues")
ax.legend().set_visible(False)
plt.xticks([])
ax.plot()



plt.yticks()
plt.show()



plt.show()

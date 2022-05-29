#!/usr/bin/python3
import sys
import os
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

#checking input
if len(sys.argv) == 1:
	print("No input files")
	exit()

#PART 1

#get list of tables from folder
files = []
for item in os.listdir(sys.argv[1]):
	if not item.startswith('.'):
		files.append(item)
os.chdir(sys.argv[1])

#taking input of first table (control)
control_table = pd.read_table(files[0])
control_table['CN_Ctrl'] = control_table['COVERAGE']/(control_table['COVERAGE'].median())

#add a column of approx copy number for each experiment
n = len(files)
for i in range(1,n):
	istring = str(i)
	new_table = pd.read_table(files[i])
	control_table['CN_Expt'+istring] = new_table['COVERAGE']/(new_table['COVERAGE'].median())

#sort final table by approx copy number of control
sorted_output = control_table.sort_values(by=['CN_Ctrl'])

#save main output table as txt file
print("SORTED OUTPUT TABLE:")
print(sorted_output)
sorted_output.to_csv("{}.txt".format(sys.argv[2]), sep='\t')



#PART 2

rowseries = sorted_output["Information"]

labels = []

for row in rowseries.str.split(';'):
	for info in row:
		label = info.split('=')[0]
		if label not in labels:
			labels.append(label)
		else:
			pass

dic = dict()
for row in sorted_output['Information']:
	for l in labels:
		leng = len(l)+1
		pos_t = row.find(l)
		pos0 = pos_t + leng
		if l not in row:
			try:
				dic[l].append(np.nan)
			except:
				dic[l] = [np.nan]
		else:
			if row.find(';',pos_t)==-1:
				try:
					dic[l].append(row[pos0:])
				except:
					dic[l]=[row[pos0:]]
			else:
				try:
					dic[l].append(row[pos0:row.find(';',pos_t)])
				except:
					dic[l]=[row[pos0:row.find(';',pos_t)]]

df_info = pd.DataFrame.from_dict(dic)
df_info.to_csv("{}_information.txt".format(sys.argv[2]), sep='\t')
print("INFORMATION TABLE:")
print(df_info)

#PART 3
#ask user if they want to see heatmap for a cog code

cog_series = pd.Series(df_info['db_xref'])
cog_list = cog_series.tolist()
sorted_output['COGs'] = cog_list

response = input("Would you like to see a heatmap for a specific COG? (y/n)")

while response == 'y':
	
	cog = (input("Insert the COG (example format: COG0197):" ))
	cog_id = "COG:" + str(cog)
	
	ct = sorted_output.loc[sorted_output['COGs'] == cog_id]

	del ct['COGs']
	a = ct.iloc[:,-n:]
	x = min(a.min())
	y = max(a.max())
	
	mapped = sns.heatmap(a, annot=True, fmt='.2f', vmin=x, vmax=y, linewidths=.5, cmap="autumn_r")

	fig = mapped.get_figure()
	fig.savefig("{}_heatmap.png".format(cog),dpi = 300)
	print("Heatmap saved as .png file")
	
	response = input("Would you like to see another heatmap? (y/n)")
	if response == 'y':
		fig.clf()
	if response == 'n':
		print("exiting program")
		exit()

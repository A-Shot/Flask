import csv
import os
def csv_c(mydict,path):
	with open(os.path.join(path,'client_ifo.csv'), 'wb') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in mydict.items():
			writer.writerow([key, value])

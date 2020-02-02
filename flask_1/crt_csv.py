# coding: utf-8
import csv
import os

base = os.path.basename("upload")



def write_csv(path_n,f_name,data_in):
	csv_name = os.path.join(path_n,f_name)+".csv"
	with open(csv_name, 'w') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in data_in.items():
			writer.writerow([key, value])


                 
                                  
def read_csv(path_n,f_name):
	csv_name = os.path.join(path_n,f_name)+".csv"
	with open(csv_name, 'r') as csv_file:
		reader = csv.reader(csv_file)
		mydict = dict(reader)
		return mydict
		
		                                               
		                                                                                        
def write_csv_2(path_n,data_in):
	csv_name = path_n+".csv"
	with open(csv_name, 'w') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in data_in.items():
			writer.writerow([key, value]) 		                                                                                                                                                                                      

tel = {'jack': 4098, 'sape': 4139}                                                                                                                          
	
write_csv(base,"fd-3232",tel)

d = read_csv(base,"fd-3232")



print (d["jack"])	

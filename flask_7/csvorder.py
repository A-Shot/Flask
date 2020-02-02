import csv


def csv_read(file_):
	with open(file_, 'rb') as csv_file:
		reader = csv.reader(csv_file)
		mydict = dict(reader)
		return mydict

def csv_write():
	with open('dict.csv', 'wb') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in mydict.items():
			writer.writerow([key, value])
			
def csv_write_R(file,value):
	with open(file, 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([value])
			
line_ = dict()		
info = list()
total = list()


def csv_read_(file_):
	mydict = dict()
	with open(file_, 'rb') as csv_file:
		reader = csv.reader(csv_file)
		try:
			print "fuck im traing"
			mydict = dict(reader)
			print "oho"
		except:
			print "ok"
	return mydict

c = dict()
c = csv_read_("test1.csv")
print c
index = 0
with open("test1.csv", 'rb') as csv_file:
		reader = csv.reader(csv_file)
		for i in reader:
			try:
				k = i[0]+","+i[2]+","+i[4][3:]
				csv_write_R("test2.csv",k)
				print "oops"
				index+=1
			except:
				csv_write_R("test2.csv",i)
				print "done"

print info
"""		
buf=list()
index = 0		
with open("test1.csv", 'rb') as csv_file:
	while True:
		buf = csv_file.readline()
		print index
		info.append(buf)
		print buf
		
		index+=1
		if not buf: break

print index
print info
"""

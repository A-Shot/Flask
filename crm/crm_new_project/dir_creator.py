import os

UPLOAD_FOLDER = os.path.basename('upload')

class Dir_File_H():
	def __init__(self,F_Path):
		self.UPLOAD_FOLDER = F_Path
		
	def job_num_creator(self):
		jobn = 0
		F= open("Job_number.txt")
		jobn = int(F.read())
		F.close()
		jobn+=1
		F = open("Job_number.txt","w")
		F.write(str(jobn))
		F.close()
		return str(jobn)
		
		
		
		
#___________________
	
def job_num_creator():
		jobn = 0
		F= open("Job_number.txt")
		jobn = int(F.read())
		F.close()
		jobn+=1
		F = open("Job_number.txt","w")
		F.write(str(jobn))
		F.close()
		return str(jobn)
	
def dir_crietor(dir_f,cast_code):
	number = str(job_num_creator())
	path_ = os.path.join(dir_f,cast_code,number)
	try:
		os.makedirs(path_)
		return path_
	except:
		print "Folder Exist"
		return None
	
"""
index = 0
while index < 4:
	g = dir_crietor(UPLOAD_FOLDER,"Cartier")
	print "parh = " + str(g)
	index+=1
"""

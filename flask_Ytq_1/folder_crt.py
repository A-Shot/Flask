import os

def job_num_creator(dir_n,cast_name,cast_code):
	jobm = 0
	F_name = os.path.join(dir_n,cast_name,cast_code)
	F= open(F_name+".txt")
	jobn = int(F.read())
	F.close()
	jobn+=1
	F = open((F_name+".txt"),"w")
	F.write(str(jobn))
	F.close()
	return str(jobn)
	
def folder_creator(dir_f,cast_name,cast_code):
	number = str(job_num_creator(dir_f,cast_name,cast_code))
	
	path_ = os.path.join(dir_f,cast_code,number)
	try:
		os.makedirs(path_)
		return path_
	except:
		return None

def dir_creator(dir_f,cast_name):
	path_=os.path.join(dir_f,cast_name)
	try:
		os.makedirs(path_)
		return path_
	except:
		return None


def xstart_job_N(dir_n,F_name,jobn):
	F_name=os.path.join(dir_n,F_name,F_name)
	F=open((F_name+"_Start"+".txt"),"w")
	F.write(str(jobn))
	F.close()
	return str(jobn)
	
	
def start_job_N(dir_n,F_name,jobn):
	F_name=os.path.join(dir_n,F_name)
	F=open((F_name+"_Start"+".txt"),"w")
	F.write(str(jobn))
	F.close()
	return str(jobn)
	
	


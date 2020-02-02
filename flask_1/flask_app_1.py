# coding: utf-8
from flask import Flask,url_for,render_template,redirect,request
import os
from crt_csv import *
from dir_crt import *


app = Flask(__name__)

data_ = ["000100","FD-10056","4566"]
base = os.path.basename("upload")

test = 0
def ad():
	global test
	test = test+1
	return test

@app.route("/index",methods=['POST', 'GET'])
def index():
	global data_
	#ad()
	print (test)
	if request.method == 'POST':
		result = request.form
		
		pat_m = os.path.join(base,result.get("3","no_name"))
		
		tem_pat = mk_dir_(pat_m,result.get("4","no_name"))
		print(tem_pat)
		write_csv_2(tem_pat,result)
	return render_template("index.html",data=data_)
	
@app.route('/generate/<data_in>',methods=['POST', 'GET'])
def generate(data_in):
	global data_
	print (data_in)
	data_.insert(1,str(data_in))
	#data = [124,355]
	return redirect(url_for("index"))


if __name__ == '__main__':
	app.run()

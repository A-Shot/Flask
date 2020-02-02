from flask import Flask,render_template, request,redirect
import os
import csv 
from create_csv import *
from folder_crt import *

UPLOAD_FOLDER = os.path.basename('Client')

app = Flask(__name__)
num_l = [56,2566]

@app.route('/')
def main():
	return render_template('main.html')
	
@app.route('/gen/<data>',methods=['POST','GET'])
def gen(data):
	print data 
	
	return  render_template('other_project.html',num1 = num_l )#redirect(url_for('other_project.html'))

@app.route('/other_project',methods=['POST','GET'])
def other_project():
	#folder_creator(UPLOAD_FOLDER,"FD","FD")
	number = 1001
	return render_template('other_project.html',num = number)
	
@app.route("/Ring_Project",methods=['GET','POST'])
def Ring_Project():
    data = dict()
    data = request.form
    print data
    return render_template("Ring_Project.html")
	
@app.route('/new_client',methods=['GET','POST'])
def new_client():
	data = dict()
	data = request.form
	client_code = data.get("Client Code")
	if data:
		path_dir = dir_creator(UPLOAD_FOLDER,data.get("Client Code"))
		csv_c(data,path_dir)
		start_job_N(path_dir,client_code,101)

	return render_template('new_client.html')

app.run(host='0.0.0.0',debug=False)

  from flask import Flask,render_template, request,redirect,jsonify
import os
import csv 
from create_csv import *
from folder_crt import *

path_ = os.getcwd()


UPLOAD_FOLDER = os.path.join(path_,"static","Clients")

app = Flask(__name__)
num_l = [56,2566]

@app.route('/')
def main():
	return render_template('main.html')
	
@app.route("/Generate",methods=['GET', 'POST'])
def Generate():
    x = request.args.get("data_")
    print x
    return jsonify(res ="500000")
    

@app.route("/New_Project",methods=['GET', 'POST']) 
def new_project():
    data2 =    "000017"
    data = os.listdir(
UPLOAD_FOLDER) 
    select =request.form
    print select
    return render_template("New_Project.html",data=data,data_2=data2)


	

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
		path_dir = dir_creator( 
UPLOAD_FOLDER ,data.get("Client Code"))
		create_csv(data,path_dir)
		start_job_N(path_dir,client_code,101)

	return render_template('new_client.html')

app.run(host='0.0.0.0',debug=False)

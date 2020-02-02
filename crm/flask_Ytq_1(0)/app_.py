from flask import Flask,render_template, request,redirect,url_for
import os
import csv 
from create_csv import *
from folder_crt import *

UPLOAD_FOLDER = os.path.basename('Client')

app = Flask(__name__)
yt_num = "00000"

@app.route('/')
def main():
	return render_template('main.html')
	
@app.route('/gen/',methods=['POST','GET'])
def gen():
    global yt_num
    yt_num ="00001"
    return redirect(url_for("other_project"))

@app.route('/New_Project',methods=['POST','GET'])
def other_project():
            #folder_creator(UPLOAD_FOLDER,"FD","FD")
	number =[yt_num,"EL-5580"]
	data = dict()
	data = request.form
	print data
	return render_template('New_Project.html',num = number)
	
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

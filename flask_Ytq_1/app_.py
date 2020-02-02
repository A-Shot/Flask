from flask import Flask,render_template, request
import os
import csv 
from create_csv import *
from folder_crt import *

UPLOAD_FOLDER = os.path.basename('Client')

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('main.html')

@app.route('/New_Project')
def New_Project():
	return render_template('New_Project.html')
	
@app.route('/Ring_Project')
def Ring_Project():
	return render_template('Ring_Project.html')
	
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

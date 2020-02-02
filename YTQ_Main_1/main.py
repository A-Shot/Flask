
from flask import Flask, flash, redirect, render_template,request, url_for,send_from_directory,jsonify
import os



UPLOAD_FOLDER = os.getcwd()

folder = os.path.join(UPLOAD_FOLDER,"static","Clients")

app = Flask(__name__)

#app.config['UPLOAD_FOLDER']=os.path.join(os.path.basename(os.getcwd()),"static","Clients")

@app.route('/')
def index():
	
	return render_template('main.html')

@app.route("/Generate")
def generate():
	data = {'a' : 'one', 'b' : 'two'}
	return jsonify(data)

@app.route("/new_project_ajax",methods=['GET', 'POST']) 
def new_project():
	data = os.listdir(folder)
	select = request.form
	print("ok")
	
	return render_template("new_project_ajax.html",data=data)



		
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)
	
	

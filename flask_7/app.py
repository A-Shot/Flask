 
from flask import Flask, flash, redirect, render_template,request, url_for,send_from_directory,jsonify
import os



#UPLOAD_FOLDER = os.getcwd()

#folder = os.path.join(UPLOAD_FOLDER,"static")

app = Flask(__name__)

app.config['UPLOAD_FOLDER']=os.path.join(os.path.basename(os.getcwd()),"static")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/test',methods=['GET', 'POST']) 
def test():
	pat = os.path.join("static","Ct","bc")
	data = os.listdir(pat)
	
	for i in range(len(data)):
		data[i] = os.path.join(pat,data[i])
		print(data)
	return render_template("index2.html",data=data)


@app.route('/test1',methods=['GET', 'POST']) 
def test1():
	#data = os.path.join(app.config[])
	return send_from_directory("./YT",mdata) 


@app.route('/test2',methods=['GET', 'POST']) 
def test2():
	mdata = os.listdir("YT")
	print(mdata)
	return send_from_directory("./YT",mdata) 
	
@app.route('/test5')
def test5():
	print(app.config["UPLOAD_FOLDER"])
	data = os.path.join(app.config["UPLOAD_FOLDER"],"test1.JPG")
	return render_template('index3.html',data = data)
		
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)
	
	

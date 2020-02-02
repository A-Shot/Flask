
from flask import Flask, flash, redirect, render_template,request, url_for,send_from_directory,jsonify
import os


color = ["danger","primary","secondary","success","info"]




app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index4.html')

@app.route('/test',methods=['GET', 'POST']) 
def test():
	print ("hopa")
	if request.method == "POST":
		print ("post")
	x = request.args.get("data_")
	print (x)
	return jsonify(res=str(x))



	
	
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)
	
	

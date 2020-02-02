from flask import Flask, flash, redirect, render_template,request, url_for,send_from_directory,jsonify
import os



UPLOAD_FOLDER = os.getcwd()

folder = os.path.join(UPLOAD_FOLDER,"static","Clients")

app = Flask(__name__)

#app.config['UPLOAD_FOLDER']=os.path.join(os.path.basename(os.getcwd()),"static","Clients")

@app.route('/')
def index():
	
	return render_template('main.html')

@app.route("/Generate",methods=['GET', 'POST'])
def Generate():
    x = request.args.get("data_")
    print x
    return jsonify(res ="500000")
    

@app.route("/New_Project",methods=['GET', 'POST']) 
def new_project():
    data2 =    "000017"
    data = os.listdir(folder)
    select =request.form
    print select
    return render_template("New_Project.html",data=data,data_2=data2)


		
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)
	
	


from flask import Flask, flash, redirect, render_template,request, url_for,send_from_directory,Blueprint
import os






UPLOAD_FOLDER = os.getcwd()

folder = os.path.join(UPLOAD_FOLDER,"YT")


app = Flask()

simple_page = Blueprint('simple_page', __name__,template_folder='templates')

@simple_page.route('/test',methods=['GET', 'POST'])
def test():
	data = ""
	return render_template('index2.html')


	
	
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)
	
	

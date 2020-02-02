
from flask import Flask, jsonify, request,render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,RadioField
from wtforms.validators import DataRequired
import csv

def csv_c(mydict):
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
            writer.writerow([key, value])
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'DontTellAnyone'
myChoices = [('Banana', 'banana'), ('Pineapple', 'pineapple')]



class Inputs(FlaskForm):
   
    username = StringField('ProjectN', validators=[DataRequired()],default="0001-HW-5890782")
    password = StringField('password', validators=[DataRequired()],default="")
    myField = SelectField('ProjectN',validators=[DataRequired()] ,choices = myChoices)
    Ring_Style = RadioField('Ring_Style', choices = [('S','Solitare'),('3st','3Stone')])

@app.route('/', methods=['GET', 'POST'])
def index():
	#form = LoginForm()
	form = Inputs()
	x=dict(request.form)
	x.pop("csrf_token", None)
	csv_c(x)
	print (x)
	if form.validate_on_submit():
		return 'Form Successfully Submitted!'
	return render_template('index.html', form=form)


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False)

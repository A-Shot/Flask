from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CheckBox(SelectMultipleField):
    widget=widgets.ListWidget(prefix_label=True)
    option_widget=widgets.CheckboxInput()

class NumberForm(Form):
    data = CheckBox(label='Choose an option', choices=data_choices)
    email = TextField('What is your email?', validators=[Required()])
    submit = SubmitField('Submit') 


app = Flask(__name__)
Bootstrap(app)


@app.route("/",methods=['GET', 'POST']) 
def index():
    return render_template("index.html")
)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port = 5006,debug=False)

#########################################################################
#                      IMPORT

from flask import Flask , render_template, jsonify, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

import pandas as pd

import my_random

#########################################################################
#                     GLOBAL VARIABLES

global data_filename

global db

global flag

#########################################################################
#                      PARAMETERS

#########################################################################
#                      CLASSES



#------------------------------------------------------------------------

#########################################################################
#                      FUNCTIONS
#************************************************************************

def data_to_db():
	data_to_db1(db, data_filename)

#------------------------------------------------------------------------

def data_to_db1(db, filename):
	df = pd.read_csv(filename)
	for name in df.Nomi:
		new_data = User(name)
		db.session.add(new_data)
	db.session.commit()

#------------------------------------------------------------------------


#########################################################################
#                      INSTRUCTIONS

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://msuwqkjoczojtx:0a57d22c2fee546d924dc2c8198cd83b911c619f31ef3829d502b60cfdf6ba16@ec2-52-205-61-230.compute-1.amazonaws.com:5432/dld6b0qq4c9fh'

#------------------------------------------------------------------------

db = SQLAlchemy(app)


class User(db.Model):
	# Defines the Table Name user
	__tablename__ = "user"

	# Makes three columns into the table id, name, email
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)

	# A constructor function where we will pass the name and email of a user and it gets add as a new entry in the table.
	def __init__(self, name):
		self.name = name



data_filename = 'data.csv'

flag = 0

#------------------------------------------------------------------------

# Control will come here and then gets redirect to the index function
@app.route("/")
def home():
	return redirect(url_for('index'))

@app.route('/index')
def index():
	return render_template('index.html')  


@app.route("/1aord", methods = ["GET", "POST"])
def class_1aord():
	global flag
	if request.method == 'POST':
		data = request.form
		if flag == 1:
			user_data = User.query.all()
			user_data1 = my_random.randomize_list(user_data)
			return render_template("1aord.html", user_data = user_data1) # passes user_data variable into the index.html file.  
	else:
		if flag == 0:
			data_to_db()
			db.session.commit()
			flag = 1
		user_data = User.query.all()
		return render_template("1aord.html", user_data = user_data) # passes user_data variable into the index.html file.

#------------------------------------------------------------------------

if __name__=="__main__":
	db.create_all()
	app.run(debug=True)
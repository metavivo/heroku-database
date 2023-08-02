#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alessandro Valitutti

# Last version date: 

#########################################################################
#                      IMPORT

from flask import Flask , render_template, jsonify, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

#########################################################################
#                      INSTRUCTIONS
#------------------------------------------------------------------------

# creation of the app object
app = Flask(__name__)

#------------------------------------------------------------------------

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gdhpwphsvckmcm:94baed95dc547e59f64e8eeda1694bd0f9a2b65601bb478ab85f8fcf99ab66af@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d2ffvcg3n7usjp'

#------------------------------------------------------------------------

# creation of the database
db = SQLAlchemy(app)

#------------------------------------------------------------------------

class Table(db.Model):
   __tablename__ = "table"
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(100), nullable=False)
   def __init__(self, name):
      self.name = name

#------------------------------------------------------------------------

# Control will come here and then gets redirect to the index function
@app.route("/")
def home():
        name = "Alessandro"
        new_data = Table(name)
        db.session.add(new_data)
        db.session.commit()
        user_data = Table.query.all()
        return user_data[0].name

#------------------------------------------------------------------------

if __name__=="__main__":
	db.create_all()
	app.run(debug=True)


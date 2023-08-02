from flask import Flask, render_template, request, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#------------------------------------------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Word.sqlite3'

db = SQLAlchemy(app)

#------------------------------------------------------------------------

class Word(db.Model):
	__tablename__ = "words"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)

	def __init__(self, name):
		self.name = name

#------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template('input.html') 


@app.route('/input', methods = ["POST"])
def input():
#    return "Input word inserted!"
    if request.method == 'POST':
        word = request.form['word']
        data = Word(word)
        db.session.add(data)
        db.session.commit()
        out = Word.query.all()
        return render_template("output.html", word_data = out)

#------------------------------------------------------------------------

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

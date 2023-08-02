# import the Flask class from the flask module
from flask import Flask, render_template, request, jsonify

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/post', methods=['POST'])
def my_post():
    if request.method == 'POST':
        return render_template('welcome.html') 



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(port=9000,debug=True)



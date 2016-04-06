"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login' , methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	print request.form['Firstname']
        if len(request.form['Firstname']) and len(request.form['Lastname']) and len(request.form['Age']) and len(request.form['Favorite Dessert']):
            return render_template('login.html', error=error,Firstname=request.form['Firstname'],
    	Lastname=request.form['Lastname'],Age=request.form['Age'],Dessert=request.form['Favorite Dessert'] )
        else:
            error = 'Invalid input'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)

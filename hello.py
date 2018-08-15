from flask import render_template
from flask import Flask
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sub')
def sub():
    return render_template('hello.html')

# @app.route('/munch')
# def munchkin():
#     with open('data.csv') as csvfile:
# 	    readCSV = csv.reader(csvfile, delimiter=';')

# 	    dataSet = []
# 	    i = 0

# 	    for row in readCSV:
# 	        dataSet[i] = row
# 	        i = i + 1

#     return render_template('hello.html', data = dataSet)


if __name__ == '__main__':
    app.run()

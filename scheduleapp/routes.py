from flask import request, redirect, render_template, jsonify
from scheduleapp import app
# import yaml
import json

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/random_thing_meh')
def random():
	return "some random text"

# @app.route('/receiveU2000',methods=['POST','GET'])
# def receiveU2000_statistics():
# 	request_data = request.data
# 	rawData = yaml.load(request_data)
# 	f = file('u2000input.txt','w')
# 	f.write(str(rawData))
# 	f.close()
# 	dm.handleU2000DataHourly(rawData)
# 	return 'received'

# @app.route('/ttt',methods=['GET'])
# def ttt():
# 	a = str(request.args.get('a'))
# 	b = str(request.args.get('b'))
# 	c = str(request.args.get('c'))
# 	print a,b,c
# 	return 'wehhhh'

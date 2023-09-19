#!/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/")
#This is called a python decorator, next is the app variable.
def index():
    return "Testing Flask Application"


app.run(host="0.0.0.0",port=5001)
#telling it to run on our host and port 80/5001 

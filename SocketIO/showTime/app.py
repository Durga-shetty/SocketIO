from datetime import time
from flask import Flask,render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS,cross_origin
import os
import sys
import time

from werkzeug import debug

app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio=SocketIO(app)

@socketio.on('connect')
def connect():
        serverTime = time.strftime('%A %B, %d %Y %H:%M:%S')
        emit('serverTime',serverTime,broadcast=True)
        #display()

@socketio.on('disconnect')
def disconnect():
    print("disconnected")

def display():
    while True:
       serverTime = time.strftime('%A %B, %d %Y %H:%M:%S')
       emit('serverTime',serverTime,broadcast=True)
       time.sleep(5000)


@app.route('/',methods=['GET'])
def home():
    serverTime = time.strftime('%A %B, %d %Y %H:%M:%S')
    return render_template("index.html",serverTime=serverTime)
@app.after_request
def before_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == "__main__":
    socketio.run(app,debug=True)



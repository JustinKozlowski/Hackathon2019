import GridLgic.py
import METsMath.py
from PIL import Image
import numpy as np

#from flask import Flask, send_from_directory, request
#from flask_socketio import SocketIO
import eventlet
import socket
import json
from threading import Thread

eventlet.monkey_patch()
#app = Flask(__name__)
socket_server = SocketIO(app)
model_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
model_socket.connect(('localhost', 81)) #only if main is active


def listen_to_model(the_socket):
    delimiter = "~"
    buffer = ""
    while True:
        buffer += the_socket.recv(1024).decode()
        while delimiter in buffer:
            message = buffer[:buffer.find(delimiter)]
            buffer = buffer[buffer.find(delimiter)+1:]
            #do something with message
            dataJson = json.loads(message)
            start(dataJson)
            toAll = {
                        'items': orderedItems,
                        'path': pathlist

                    }
            jsonOut = json.dumps(toAll)
            socket_server.emit('message', jsonToAll, broadcast=True)


Thread(target=listen_to_model, args=(model_socket,)).start()


#@app.route('/')
#def index():
#    return send_from_directory('../frontend', 'web.html')
#
#
#@socket_server.on('Jason')
#def got_message(jason):
#    data = {"action": "regular", "data": json.loads(jason)}
#    delimiter = "~"
#    model_socket.sendall((json.dumps(data) + delimiter).encode())
#
#
#app_port = 8505
#print("server at localhost:" + str(app_port))
#socket_server.run(app, port=app_port)
#
#
#
img = Image.open('bw_wegmans.png').convert('L')

np_img = np.array(img)
np_img[np_img > 0] = 1


def getNewGrid():
    return np_img


def start(dataJson):
    items = dataJson['items']
    sortedList = mySort(dataJson['items'], dataJson['workout']}
    Node1 = nodeLoc(items[0]['aisle'], items[0]['sort'], items[0]['side'])
    for x in range(1,len(items)):
        Node2 = nodeLoc(items[x]['aisle'], items[x]['sort'], items[x]['side'])







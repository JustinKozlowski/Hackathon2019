import GridLogic
import METsMath
from PIL import Image
import numpy as np
import requests

#from flask import Flask, send_from_directory, request
#from flask_socketio import SocketIO
import eventlet
import socket
import json
from threading import Thread

eventlet.monkey_patch()
#app = Flask(__name__)
#socket_server = SocketIO(app)
model_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
model_socket.connect(('localhost', 8000)) #only if main is active


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
            output = start(dataJson)
            jsonOut = json.dumps(output)
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
img = Image.open('wegmans.PNG').convert('L')

np_img = np.array(img)
np_img[np_img > 0] = 1


APIurl = 'https://api.wegmans.io/products/'
APIurl2 = '/locations/83?api-version=2018-10-18&subscription-key=ac6e23a3e7b843d6a92a0668aa012037'
APIurl3 = '?api-version=2018-10-18&subscription-key=ac6e23a3e7b843d6a92a0668aa012037'



def getNewGrid():
    return np_img

def itemList(items):
    itemList = []
    for x in items:
        locinfo = (requests.get(APIurl + x['sku'] + APIurl2)).json()
        weight = (requests.get(APIurl + x['sku'] + APIurl3)).json()['trafeIdentifiers'][0]['weight']
        node = {'item': x['item'],
                'aisle':locinfo['locations'][0]['name'],
                'side':locinfo['locations'][0]['aisleSide'],
                'sort':locinfo['locations'][0]['sort'],
                'weight':weight
                }
        itemList+=node
    return itemList

def getItemWeight(weight):
    measure = weight['unitOfMeasure']
    if measure == 'OZ' or measure == 'ONZ':
        return weight['value']/16
    else:
        return weight['value']

def start(dataJson):
    items = itemList(dataJson['items'])
    sortedList = GridLogic.mySort(items, dataJson['workout'])
    Node1 = (84,67)
    path = []
    caloriesBurned = 0
    weight = 0
    for x in range(len(items)):
        Node2 = nodeLoc(items[x]['aisle'], items[x]['sort'], items[x]['side'])
        tempPath = bfs(np_img, Node1, Node2)
        path+=tempPath
        itemWeight = getItemWeight()
        caloriesBurned += MetsMath(dataJson['carttype'],weight, tempPath)
        weight += itemWeight
    return {'paths':path,'calories':caloriesBurned}



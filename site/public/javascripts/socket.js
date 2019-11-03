var socket = require('socket.io-client')('http://localhost:8110', {transports:['websocket']});
 //transports: ['websocket']
socket.on('connect', function (event) {
    console.log("connected")
    socket.emit("register", "testing", JSON.stringify({"test":True})
});
socket.on('message', function (event) {
    // received a message from the server
    // console.log(event);
    message = JSON.parse(event)
    console.log(message)
});
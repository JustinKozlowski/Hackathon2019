var socket = io.connect({transports: ['websocket']});
socket.on('connect', function (event) {
    // console.log("connected")
});
socket.on('message', function (event) {
    // received a message from the server
    // console.log(event);
    message = JSON.parse(event)
    console.log(messaage)
});
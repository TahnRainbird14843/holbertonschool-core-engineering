#!/usr/bin/node

const socket = new WebSocket("ws://localhost:8000/ws");
const message = document.getElementById("msg");
const response = document.getElementById("response");

function send_data () {
    socket.send(message.textContent);
}

socket.onmessage = (event) => {
    console.log(event.data)
    response.textContent = event.data
}

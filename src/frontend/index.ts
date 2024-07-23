import { io } from "socket.io-client";
import { Canvas } from "./canvas";

const socket = io();
const my_client_id = prompt('Enter your client ID')

const canvas = new Canvas(document.getElementById('canvas') as HTMLCanvasElement)

socket.on('connect', function () {

    if (!my_client_id) return
    socket.emit('client-connected', { client_id: my_client_id })
})

socket.on('update-sprites', function (data) {

    const { sprites, client_id, canvas_width, canvas_height, canvas_bg_color} = JSON.parse(data)
    if (client_id !== my_client_id) return

    canvas.setWidth(canvas_width)
    canvas.setHeght(canvas_height)
    canvas.setBgColor(canvas_bg_color)
    canvas.reDrawAll(sprites)
})


window.onkeydown = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'down' })
}

window.onkeyup = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'up' })
}

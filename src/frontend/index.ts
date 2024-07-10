import { io } from "socket.io-client";
import { Canvas } from "./canvas";

const my_client_id = 'c1'
const socket = io();

const canvas = new Canvas(document.getElementById('canvas') as HTMLCanvasElement)

socket.on('connect', function () {
    
    socket.emit('client-connected', { client_id: my_client_id })
})

socket.on('update-sprites', function (data) {

    const { sprites, client_id, canvas_width, canvas_height, canvas_bg_color} = JSON.parse(data)

    
    if (client_id !== my_client_id) return

    canvas.setWidth(canvas_width)
    canvas.setHeght(canvas_height)
    canvas.setBgColor(canvas_bg_color)
    
    //@ts-ignore
    sprites.forEach(s=>{
        canvas.drawSprite(s)
    })
})


window.onkeydown = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'down' })
}

window.onkeyup = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'up' })
}

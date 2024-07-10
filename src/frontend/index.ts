import { io } from "socket.io-client";


const my_client_id = prompt('Insert your client ID:')

const socket = io();

socket.on('connect', function () {
    socket.emit('message', { data: 'connected!' })
})

socket.on('screen-update', function (data) {

    const { image_base64, client_id } = data

    if (client_id !== my_client_id) return

    const canvas = document.getElementById('canvas') as HTMLCanvasElement
    const ctx = canvas.getContext('2d')!
    const img = new Image()
    img.src = image_base64
    ctx.drawImage(img, 0, 0)
})

window.onkeydown = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'down' })
}

window.onkeyup = e => {
    socket.emit('keyevent', { client_id: my_client_id, key: e.key, state: 'up' })
}

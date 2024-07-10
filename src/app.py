import os
from threading import Thread
from flask import Flask
from canvas import Canvas
from core.KeyEvent import KeyEvent
from io import BytesIO
import base64
from flask import Flask
from flask_socketio import SocketIO
from time import sleep
import logging
from core.World import World

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'buruf'
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def index():
    path_index = os.path.split(os.path.abspath(__file__))[0]+'/frontend/index.html'
    return open(path_index).read()

@socketio.on('message')
def handle_message(data):
    print(f'received message: {data}')

@socketio.on('keyevent')
def handle_keyevent(data):

    client_id = data['client_id']
    key = data['key']
    state = data['state']
    e = KeyEvent(client_id, key, state)
    app.config['world'].put_event(e)


def update_screen_loop(world:World):

    while True:

        for client in world.get_clients():

            canvas = Canvas(500, 500, 'white')
            client.look_at_world(world, canvas)
            image = canvas.get_rendered()
            buffered = BytesIO()
            image.save(buffered, format="png")
            out = base64.b64encode(buffered.getvalue()).decode('utf-8')
            out = 'data:image/png;base64,' + out
            socketio.emit('screen-update', {'client_id': client.name, 'image_base64' : out})

        sleep(0.1)

def start_update_screen(world:World):

    Thread(target=update_screen_loop, args=[world]).start()


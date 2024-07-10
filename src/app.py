import os
from threading import Thread
from flask import Flask, json
from core.KeyEvent import KeyEvent
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

@socketio.on('client-connected')
def handle_message(data):

    client_id = data['client_id']
    print('client connected!', client_id)
    send_updated_sprites(client_id, include_image=True)

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
            send_updated_sprites(client.name, include_image=False)

        sleep(0.1)

def start_update_screen(world:World):

    Thread(target=update_screen_loop, args=[world]).start()


def send_updated_sprites(client_id:str, include_image:bool=False):

    world = app.config['world']
    assert isinstance(world, World)
    client = world.get_client(client_id)
    sprites_data = client.get_sprite_data_from_own_perspective(world, include_image)

    response = {
        'sprites': sprites_data, 
        'client_id': client_id,  
        'canvas_width': world.get_canvas_width(), 
        'canvas_height': world.get_canvas_height(), 
        'canvas_bg_color': world.get_canvas_bg_color(),
    }
    
    socketio.emit('update-sprites', json.dumps(response))

